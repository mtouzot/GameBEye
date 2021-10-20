import os
import typing

import cv2
import numpy as np

from GameBEye.gbcamcolors import color_helpers
from GameBEye.gbcamcolors.gbcamcolors import GBColorPalettes

Shape = typing.Tuple[int, int, int]


class GBCamImage:
    """
    The base class of Game Boy Camera images.

    A Game Boy Camera image is a nothing but a 4-colors 128x112 array.


    """

    IMAGE_HEIGHT: int = 128
    IMAGE_WIDTH: int = 112
    IMAGE_CHANNEL: int = 3
    BLACK_NINTENDO_BORDER: int = 16
    COLOR_PALETTE_SIZE: int = 4

    def __init__(self) -> typing.NoReturn:
        """
        Class constructor.

        All members are set to O or their equivalent regarding their types.
        """
        self.__data = np.zeros((GBCamImage.IMAGE_HEIGHT, GBCamImage.IMAGE_WIDTH, GBCamImage.IMAGE_CHANNEL))
        self.__color_palette = GBColorPalettes.BW

    @property
    def shape(self) -> Shape:
        """
        Property to return the image shape.

        As the Game Boy Camera has a fixed size, it will always return (112, 128, 3).

        :returns: the image shape
        :rtype: tuple
        """
        return GBCamImage.IMAGE_WIDTH, GBCamImage.IMAGE_HEIGHT, GBCamImage.IMAGE_CHANNEL

    @property
    def data(self) -> np.array:
        """
        Property to return the image data as a numpy array.

        :returns: the image data
        :rtype: numpy.array
        """
        return self.__data

    @property
    def color_palette(self) -> GBColorPalettes:
        """
        Return the GBColorPalette of the image.

        :returns: a GBColorPalette value
        :rtype: GBColorPalettes
        """
        return self.__color_palette

    def read(self, filepath: str) -> typing.NoReturn:
        """
        Open filepath to read the file contents and store the image into the data member.

        :raises FileNotFoundError: The input filepath must exist to be read
        :raises ValueError: Once read, the filepath must point to a standard Game Boy Camera Image : 128*112 pixels and 4 colors

        :param filepath: filepath to image
        :type filepath: a string
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError('The input filepath does not exist')

        img = cv2.imread(filepath, cv2.IMREAD_COLOR)

        if img.shape[:2] not in [(GBCamImage.IMAGE_WIDTH, GBCamImage.IMAGE_HEIGHT),  # Original image size
                                 (GBCamImage.IMAGE_WIDTH + 2 * GBCamImage.BLACK_NINTENDO_BORDER,
                                  GBCamImage.IMAGE_HEIGHT + 2 * GBCamImage.BLACK_NINTENDO_BORDER)]:  # Image + border
            raise ValueError('The image is too big to be a Game Boy Camera Image')

        bgr_colors = np.unique(
            img.view(np.dtype((np.void, img.dtype.itemsize * img.shape[2])))
        ).view(img.dtype).reshape(-1, img.shape[2])
        hex_colors = np.array([color_helpers.bgr_to_hex(bgr_val=val) for val in bgr_colors])

        if len(hex_colors) != GBCamImage.COLOR_PALETTE_SIZE:
            raise ValueError('The image contains more than {} colors'.format(GBCamImage.COLOR_PALETTE_SIZE))

        if img.shape[:2] == (GBCamImage.IMAGE_WIDTH + 2 * GBCamImage.BLACK_NINTENDO_BORDER,
                             GBCamImage.IMAGE_HEIGHT + 2 * GBCamImage.BLACK_NINTENDO_BORDER):
            self.__data = img[
                          GBCamImage.BLACK_NINTENDO_BORDER:GBCamImage.IMAGE_WIDTH + GBCamImage.BLACK_NINTENDO_BORDER,
                          GBCamImage.BLACK_NINTENDO_BORDER:GBCamImage.IMAGE_HEIGHT + GBCamImage.BLACK_NINTENDO_BORDER,
                          :]
        else:
            self.__data = img

        self.__color_palette = [palette for palette in GBColorPalettes
                                if all(thresh in hex_colors for thresh in palette.value)][0]

    def change_color(self, color_palette: GBColorPalettes = GBColorPalettes.BW) -> typing.NoReturn:
        """
        Change the color palette of an image with a new one from a GBColorPalettes selection.

        :raises TypeError: The color parameter must be a GBColorPalettes.

        :param color_palette: the color palette to apply
        :type: a GBColorPalettes value
        """

        if not isinstance(color_palette, GBColorPalettes):
            raise TypeError("The color parameter must be a GBColorPalettes.")

        img_temp = np.empty_like(self.__data)
        for idx, thresh in enumerate(color_palette.value):
            thresh = color_helpers.hex_to_bgr(thresh)
            for x in np.arange(self.__data.shape[0]):
                for y in np.arange(self.__data.shape[1]):
                    if all(self.__data[x, y] == color_helpers.hex_to_rgb(self.color_palette.value[idx])):
                        img_temp[x, y] = thresh

        self.__data[:] = img_temp
        self.__color_palette = color_palette
