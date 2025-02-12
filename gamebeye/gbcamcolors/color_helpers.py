"""Define color conversions and methods related to 8-bits colorspaces."""

import numpy as np
import numpy.typing as npt


def clamp(val: int) -> int:
    """
    Ensure that val is between 0 and 255.

    Clamp each out of bound value.

    :param int val: an int value

    :returns: the clamped value
    :rtype: int

    >>> from gamebeye.gbcamcolors.color_helpers import clamp
    >>> clamp(-125)
    0
    >>> clamp(0)
    0
    >>> clamp(125)
    125
    >>> clamp(255)
    255
    >>> clamp(512)
    255
    """
    return max(0, min(val, 255))


def is_clamped(val: int) -> bool:
    """
    Check if val is clamped between 0 and 255.

    If val is out of boundaries, returns False. True otherwise.

    :param int val: the value to be checked

    :returns: the comparison result
    :rtype: bool

    >>> from gamebeye.gbcamcolors.color_helpers import is_clamped
    >>> is_clamped(-125)
    False
    >>> is_clamped(0)
    True
    >>> is_clamped(125)
    True
    >>> is_clamped(255)
    True
    >>> is_clamped(512)
    False

    """
    return 0 <= val <= 255


def clamp_rgb(rgb_val: npt.ArrayLike) -> np.ndarray:
    """
    Ensure that all RGB values are between 0 and 255.

    Clamp each out of bound value.

    :param List[int] rgb_val: 3-channels list for R, G, B

    :raises ValueError: rgb_val argument must be a 3 values list

    :returns: the clamped list
    :rtype: List[int]

    >>> from gamebeye.gbcamcolors.color_helpers import clamp_rgb
    >>> clamp_rgb([0, 0, 0])
    [0, 0, 0]
    >>> clamp_rgb([255, 255, 255])
    [255, 255, 255]
    >>> clamp_rgb([512, 0, 0])
    [255, 0, 0]
    >>> clamp_rgb([255, 255, 255, 0])
    Traceback (most recent call last):
        ...
    ValueError: rgb_val argument must be a 3 values list
    """
    if len(rgb_val) != 3:
        raise ValueError("rgb_val argument must be a 3 values list")
    if isinstance(rgb_val, np.ndarray):
        rgb_val = rgb_val.tolist()
    return np.array([clamp(val) for val in rgb_val])


def is_clamped_rgb(rgb_val: npt.ArrayLike) -> bool:
    """
    Check if the RGB color values are clamped between 0 and 255.

    If val is out of boundaries, returns False. True otherwise.

    :param List[int] rgb_val: 3-channels list for R, G, B

    :raises ValueError: rgb_val argument must be a 3 values list

    :returns: the comparison result
    :rtype: bool

    >>> from gamebeye.gbcamcolors.color_helpers import is_clamped_rgb
    >>> is_clamped_rgb([0, 0, 0])
    True
    >>> is_clamped_rgb([255, 255, 255])
    True
    >>> is_clamped_rgb([512, 0, 0])
    False
    >>> is_clamped_rgb([255, 255, 255, 0])
    Traceback (most recent call last):
        ...
    ValueError: rgb_val argument must be a 3 values list
    """
    if len(rgb_val) != 3:
        raise ValueError("rgb_val argument must be a 3 values list")
    if isinstance(rgb_val, np.ndarray):
        rgb_val = rgb_val.tolist()
    return sum([is_clamped(val) for val in rgb_val]) == 3


def clamp_hex(hex_val: str) -> str:
    """
    Ensure that val is between '0x000000' and '0xFFFFFF'.

    Clamp each out of bound value.

    :param str hex_val: an hexadecimal string value

    :returns: the hex clamped value
    :rtype: str

    >>> from gamebeye.gbcamcolors.color_helpers import clamp_hex
    >>> clamp_hex('#000000')
    '#000000'
    >>> clamp_hex('#FFFFFF')
    '#FFFFFF'
    >>> clamp_hex('#00FF00')
    '#00FF00'
    >>> clamp_hex('#F000000')
    '#FFFFFF'
    """
    hex_val = int(hex_val.replace("#", "0x"), 0)
    hex_val = "0x{0:0{1}X}".format(max(0, min(int("0xFFFFFF", 0), hex_val)), 6)
    return hex_val.replace("0x", "#")


def is_clamped_hex(hex_val: str) -> bool:
    """
    Ensure that val is between '#000000' and '#FFFFFF'.

    If val is out of boundaries, returns False. True otherwise.

    :param str hex_val: an hexadecimal value

    :returns: the comparison result
    :rtype: bool

    >>> from gamebeye.gbcamcolors.color_helpers import is_clamped_hex
    >>> is_clamped_hex('#000000')
    True
    >>> is_clamped_hex('#FFFFFF')
    True
    >>> is_clamped_hex('#00FF00')
    True
    >>> is_clamped_hex('#F000000')
    False
    """
    hex_val = hex_val.replace("#", "0x")
    return int("0x000000", 0) <= int(hex_val, 0) <= int("0xFFFFFF", 0)


def hex_to_rgb(hex_val: str) -> np.ndarray:
    """
    Convert a hexadecimal value to RGB values.

    All values are clamped between 0 and 255.

    The 2 left digits code the red value, the 2 middle digits the blue
    and the 2 left digits the green.

    :param str hex_val: hexadecimal value.

    :returns: a list containing R, G, B values.
    :rtype: a list of integer

    >>> from gamebeye.gbcamcolors.color_helpers import hex_to_rgb
    >>> hex_to_rgb('#000000')
    [0, 0, 0]
    >>> hex_to_rgb('#FF0000')
    [255, 0, 0]
    >>> hex_to_rgb('#00FF00')
    [0, 255, 0]
    >>> hex_to_rgb('#0000FF')
    [0, 0, 255]
    >>> hex_to_rgb('#FFFFFF')
    [255, 255, 255]
    >>> hex_to_rgb('#F000000')
    [255, 255, 255]
    """
    hex_val = clamp_hex(hex_val).replace("#", "0x")
    return np.array([((int(hex_val, 0) >> idx * 8) & 255) for idx in range(2, -1, -1)])


def hex_to_bgr(hex_val: str) -> np.ndarray:
    """
    Convert a hexadecimal value to BGR values.

    All values are clamped between 0 and 255.

    The 2 left digits code the green value, the 2 middle digits the blue and
    the 2 left digits the red.

    :param str hex_val: hexadecimal value.

    :returns: a list containing B, G, R values
    :rtype: a list of integer

    >>> from gamebeye.gbcamcolors.color_helpers import hex_to_bgr
    >>> hex_to_bgr('#000000')
    [0, 0, 0]
    >>> hex_to_bgr('#FF0000')
    [0, 0, 255]
    >>> hex_to_bgr('#00FF00')
    [0, 255, 0]
    >>> hex_to_bgr('#0000FF')
    [255, 0, 0]
    >>> hex_to_bgr('#FFFFFF')
    [255, 255, 255]
    >>> hex_to_bgr('#F000000')
    [255, 255, 255]
    """
    hex_val = clamp_hex(hex_val).replace("#", "0x")
    return np.array([((int(hex_val, 0) >> idx * 8) & 255) for idx in range(0, 3, 1)])


def rgb_to_hex(rgb_val: npt.ArrayLike) -> str:
    """
    Convert a (R, G, B) array to hexadecimal integer.

    All values are clamped between 0 and 255.

    :param list rgb_val: (R, G, B) list to convert

    :raises ValueError: rgb_val argument must be a 3 values list

    :returns: an hexadecimal value
    :rtype: str

    >>> from gamebeye.gbcamcolors.color_helpers import rgb_to_hex
    >>> rgb_to_hex([0, 0, 0])
    '#000000'
    >>> rgb_to_hex([0, 0, 255])
    '#0000FF'
    >>> rgb_to_hex([255, 0, 0])
    '#FF0000'
    >>> rgb_to_hex([512, 128, 0])
    '#FF8000'
    >>> rgb_to_hex([0, 0, 0, 0])
    Traceback (most recent call last):
        ...
    ValueError: rgb_val argument must be a 3 values list
    """
    if len(rgb_val) != 3:
        raise ValueError("rgb_val argument must be a 3 values list")
    if not isinstance(rgb_val, tuple):
        rgb_val = tuple(clamp_rgb(rgb_val))
    return "#%02X%02X%02X" % rgb_val


def bgr_to_hex(bgr_val: npt.ArrayLike) -> str:
    """
    Convert a (B, G, R) array to hexadecimal integer.

    All values are clamped between 0 and 255.

    :param list bgr_val: (B, G, R) to convert

    :raises ValueError: rgb_val argument must be a 3 values list

    :returns: an hexadecimal value
    :rtype: str

    >>> from gamebeye.gbcamcolors.color_helpers import bgr_to_hex
    >>> bgr_to_hex([0, 0, 0])
    '#000000'
    >>> bgr_to_hex([0, 0, 255])
    '#FF0000'
    >>> bgr_to_hex([255, 0, 0])
    '#0000FF'
    >>> bgr_to_hex([512, 128, 0])
    '#0080FF'
    >>> bgr_to_hex([0, 0, 0, 0])
    Traceback (most recent call last):
        ...
    ValueError: bgr_val argument must be a 3 values list
    """
    if len(bgr_val) != 3:
        raise ValueError("bgr_val argument must be a 3 values list")
    if not isinstance(bgr_val, tuple):
        bgr_val = tuple(clamp_rgb(bgr_val))
    return "#%02X%02X%02X" % bgr_val[::-1]
