"""Define the GBCamImage class."""

import os
from typing import List, NoReturn, Tuple

import cv2
import numpy as np

from gamebeye.gbcamcolors.color_helpers import (
    bgr_to_hex,
    hex_to_bgr,
    hex_to_rgb,
)
from gamebeye.gbcamcolors.gbcolorpalettes import GBColorPalettes

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
        return self.__data.shape

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

    def read(self, image_filepath: str, convert: bool = False) -> NoReturn:
        """
        Open filepath to read the file contents to populate the object.

        Read filepath content, change color to GBColorPalettes.BW if unknown.

        :raises FileNotFoundError: The input filepath must exist to be read
        :raises ValueError: The read image is a standard Game Boy Camera Image.

        :param image_filepath: filepath to image
        :type image_filepath: a string
        :param convert: turn on color convertion to the closest GBColorPalette
        :type convert: bool
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
            np.unique(img.view(np.dtype((np.void, img.dtype.itemsize * img.shape[2]))))
            .view(img.dtype)
            .reshape(-1, img.shape[2])
        )

        if convert:
            gb_color_palette = GBColorPalettes.nearest_palette(bgr_colors)
            bgr_colors = self.convert_to_palette(bgr_colors, gb_color_palette)

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
            if np.array_equal(np.sort(hex_colors), sorted(palette.hex_colors))
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
        for idx, color in enumerate(color_palette.value):
            thresh = hex_to_bgr(color.value)
            current_color = hex_to_rgb(self.__colors.value[idx].value)
            img_temp = np.where(self.__data == current_color, thresh, img_temp)

        self.__data[:] = img_temp
        self.__colors = color_palette

    def convert_to_palette(
        self, src_color_palette: List[List[int]], dest_color_palette: GBColorPalettes
    ):
        """
        Convert the data to the nearest GBColorPalettes.

        :param src_color_palette: original color palatte
        :type src_color_palette: List of List of int
        :param dest_color_palette: final GBColorPalettes
        :type dest_color_palette: GBColorPalettes

        :return: the final color palette in the BGR color space
        :rtype: List of List of int
        """
        color_map = GBColorPalettes.convert_to_palette(
            src_color_palette, dest_color_palette
        )

        bgr_colors = []
        img_temp = np.empty_like(self.__data)
        for color in color_map.keys():
            bgr_color = hex_to_bgr(color_map[color].value).tolist()
            bgr_colors.append(bgr_color)

            src_color = hex_to_rgb(color)
            dest_color = hex_to_rgb(color_map[color].value)
            img_temp = np.where(self.__data == src_color, dest_color, img_temp)

        self.__data[:] = img_temp
        self.__colors = dest_color_palette
        return [{tuple(color) for color in bgr_colors}]
