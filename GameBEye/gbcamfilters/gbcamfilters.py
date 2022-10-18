import os
import cv2
import numpy as np

from GameBEye.gbcamcolors.color_helpers import bgr_to_hex
from GameBEye.gbcamimage.gbcamimage import GBCamImage
from .filter_helpers import generate_vstripes


def to_thermal_printer(src: GBCamImage) -> np.array:
    """
    Emulate a Game Boy thermal printer and
    Return the image as if it was printed on paper.

    :param src: A Game Boy Camera Image
    :type: GBCamImage

    :return: the printed image
    :rtype: np.ndarray
    """

    mask_size = 20
    overlap = 4

    pixel_sample = os.path.join(
        os.path.dirname(__file__), "images\\sample\\pixel_sample.png"
    )
    pixel_sample = cv2.imread(pixel_sample)
    nb_pixel_samples = 49

    temp = generate_vstripes(src.shape)
    dst = 255 * np.ones(
        (
            src.WIDTH * (mask_size - overlap) + overlap,
            src.HEIGHT * (mask_size - overlap) + overlap,
            src.CHANNEL,
        ),
        dtype=np.uint8,
    )

    for y in range(src.HEIGHT):
        for x in range(src.WIDTH):
            a = x * (mask_size - overlap)
            b = a + mask_size
            c = y * (mask_size - overlap)
            d = c + mask_size

            if bgr_to_hex(src.data[x, y]) != src.color_palette.value[0]:
                j = np.random.choice(nb_pixel_samples)
                i = src.color_palette.value.index(bgr_to_hex(src.data[x, y]))

                dot = pixel_sample[
                    mask_size * i : mask_size * (i + 1),
                    mask_size * j : mask_size * (j + 1),
                    :,
                ]

                if np.random.rand() < 0.5:
                    dot = np.flip(dot, int(np.ceil(2 * np.random.rand())))
                dot = np.rot90(dot, int(np.ceil(2 * np.random.rand())) - 2)

                if (temp[x, y, :] == [0, 0, 0]).all():
                    dot = cv2.add(dot, 30 * np.ones_like(dot))

                dst[a:b, c:d, :] = np.minimum(dot, dst[a:b, c:d, :])

    return dst
