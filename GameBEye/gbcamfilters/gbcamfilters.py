import os
import typing

import cv2
import numpy as np

from GameBEye.gbcamcolors.color_helpers import bgr_to_hex
from GameBEye.gbcamimage.gbcamimage import GBCamImage
from .filter_helpers import generate_vstripes


def to_thermal_printer(image: GBCamImage) -> np.array:
    """
    Emulate a Game Boy thermal printer and return the image as if it was printed on paper.

    :param image: A Game Boy Camera Image
    :type: GBCamImage

    :return: the printed image
    :rtype: np.array
    """

    mask_size = 20
    overlapping = 4

    pixel_sample = os.path.join(os.path.dirname(__file__), "images\\sample\\pixel_sample.png")
    pixel_sample = cv2.imread(pixel_sample)
    nb_pixel_samples = 49

    vstripes_img = generate_vstripes(image.shape)
    speckles_img = 255 * np.ones((image.IMAGE_WIDTH*(mask_size - overlapping) + overlapping,
                           image.IMAGE_HEIGHT*(mask_size - overlapping) + overlapping,
                           image.IMAGE_CHANNEL), dtype=np.uint8)

    for y in range(image.IMAGE_HEIGHT):
        for x in range(image.IMAGE_WIDTH):
            a = x * (mask_size - overlapping)
            b = a + mask_size
            c = y * (mask_size - overlapping)
            d = c + mask_size

            j = np.random.choice(nb_pixel_samples)
            i = image.color_palette.value.index(bgr_to_hex(image.data[x, y]))

            dot = pixel_sample[mask_size*i:mask_size*(i+1), mask_size*j:mask_size*(j+1), :]

            if bgr_to_hex(image.data[x, y]) != image.color_palette.value[3]:
                if np.random.rand() < 0.5:
                    dot = np.flip(dot, int(np.ceil(2 * np.random.rand())))
                dot = np.rot90(dot, int(np.ceil(2 * np.random.rand())) - 2)

                if (vstripes_img[x, y, :] == [0, 0, 0]).all():
                    dot = cv2.add(dot, 30*np.ones_like(dot))

                speckles_img[a:b, c:d, :] = np.minimum(dot, speckles_img[a:b, c:d, :])

    return speckles_img
