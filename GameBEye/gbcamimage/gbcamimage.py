"""Defines the GBCamImage class."""

import os
import cv2
import numpy as np

from typing import NoReturn, Tuple
from GameBEye.gbcamcolors.color_helpers import (
    hex_to_rgb,
    hex_to_bgr,
    bgr_to_hex,
)
from GameBEye.gbcamcolors.gbcamcolors import GBColorPalettes

Shape = Tuple[int, int, int]


class GBCamImage:
    """
    The base class of Game Boy Camera images.

    A Game Boy Camera image is a nothing but a 4-colors 128x112 array.


    """

    HEIGHT: int = 128
    WIDTH: int = 112
    CHANNEL: int = 3
    BORDER: int = 16
    NB_COLORS: int = 4

    def __init__(self) -> NoReturn:
        """
        Class constructor.

        All members are set to O or their equivalent regarding their types.
        """
        self.__data = np.zeros(
            (GBCamImage.HEIGHT, GBCamImage.WIDTH, GBCamImage.CHANNEL)
        )
        self.__colors = GBColorPalettes.BW

    @property
    def shape(self) -> Shape:
        """
        Property to return the GBCamImage shape.

        :returns: the image shape
        :rtype: tuple
        """
        shape = (GBCamImage.WIDTH, GBCamImage.HEIGHT, GBCamImage.CHANNEL)

        return shape

    @property
    def data(self) -> np.ndarray:
        """
        Property to return the image data as a numpy array.

        :returns: the image data
        :rtype: numpy.ndarray
        """
        return self.__data

    @property
    def color_palette(self) -> GBColorPalettes:
        """
        Return the GBColorPalette of the image.

        :returns: a GBColorPalette value
        :rtype: GBColorPalettes
        """
        return self.__colors

    def read(self, image_filepath: str) -> NoReturn:
        """
        Open filepath to read the file contents to populate the object.

        :raises FileNotFoundError: The input filepath must exist to be read
        :raises ValueError: The read image is a standard Game Boy Camera Image.

        :param image_filepath: filepath to image
        :type image_filepath: a string
        """
        if not os.path.exists(image_filepath):
            raise FileNotFoundError("The input filepath does not exist")

        img = cv2.imread(image_filepath, cv2.IMREAD_COLOR)

        if img.shape[:2] not in [
            (GBCamImage.WIDTH, GBCamImage.HEIGHT),
            (
                GBCamImage.WIDTH + 2 * GBCamImage.BORDER,
                GBCamImage.HEIGHT + 2 * GBCamImage.BORDER,
            ),
        ]:
            raise ValueError("The shape doesn't fit the GBCamImage shape")

        bgr_colors = (
            np.unique(
                img.view(
                    np.dtype((np.void, img.dtype.itemsize * img.shape[2]))
                )
            )
            .view(img.dtype)
            .reshape(-1, img.shape[2])
        )

        if len(bgr_colors) != GBCamImage.NB_COLORS:
            raise ValueError("The read image have too many colors")

        hex_colors = np.array([bgr_to_hex(bgr_val=val) for val in bgr_colors])
        if img.shape[:2] == (
            GBCamImage.WIDTH + 2 * GBCamImage.BORDER,
            GBCamImage.HEIGHT + 2 * GBCamImage.BORDER,
        ):
            width_max = GBCamImage.WIDTH + GBCamImage.BORDER
            height_max = GBCamImage.HEIGHT + GBCamImage.BORDER
            self.__data = img[
                GBCamImage.BORDER : width_max,
                GBCamImage.BORDER : height_max,
                :,
            ]
        else:
            self.__data = img

        self.__colors = [
            palette
            for palette in GBColorPalettes
            if all(thresh in hex_colors for thresh in palette.value)
        ][0]

    def change_color(
        self, color_palette: GBColorPalettes = GBColorPalettes.BW
    ) -> NoReturn:
        """
        Change the color palette with a new one from GBColorPalettes values.

        :raises TypeError: The color parameter must be a GBColorPalettes.

        :param color_palette: the color palette to apply
        :type: a GBColorPalettes value
        """
        if not isinstance(color_palette, GBColorPalettes):
            raise TypeError("The color parameter must be a GBColorPalettes.")

        img_temp = np.empty_like(self.__data)
        for idx, thresh in enumerate(color_palette.value):
            thresh = hex_to_bgr(thresh)
            for x in np.arange(self.__data.shape[0]):
                for y in np.arange(self.__data.shape[1]):
                    current_color = hex_to_rgb(self.__colors.value[idx])
                    if all(self.__data[x, y] == current_color):
                        img_temp[x, y] = thresh

        self.__data[:] = img_temp
        self.__colors = color_palette
