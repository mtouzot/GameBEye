"""Define filter-related unitary methods."""

import typing

import numpy as np

Size = typing.Tuple[int, int]


def generate_vstripes(size: Size) -> np.ndarray:
    """
    Generate an image with vertical stripes.

    :param size: Size of the output image
    :type size: tuple of two int

    :return: the striped image
    :rtype: np.ndarray
    """
    stripes = np.empty(size, dtype=float)
    for i in range(size[1]):
        start = np.ceil(2 * np.random.rand()) - 1
        for j in range(size[0]):
            stripes[:, j] = start
            if np.random.rand() < 0.2:
                start = np.ceil(2 * np.random.rand()) - 1
    return stripes


def generate_hstripes(size: Size) -> np.ndarray:
    """
    Generate an image with horizontal stripes.

    :param size: Size of the output image
    :type size: tuple of two int

    :return: the striped image
    :rtype: np.ndarray
    """
    stripes = np.empty(size, dtype=float)
    for i in range(size[0]):
        start = np.ceil(2 * np.random.rand()) - 1
        for j in range(size[1]):
            stripes[i, :] = start
            if np.random.rand() < 0.2:
                start = np.ceil(2 * np.random.rand()) - 1
    return stripes
