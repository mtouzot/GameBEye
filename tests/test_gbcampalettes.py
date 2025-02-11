"""All relative tests to gamebeye.gbcampalettes file."""

from typing import List

import numpy as np
import pytest

import gamebeye.gbcamcolors.color_helpers as color_helpers
import gamebeye.gbcamcolors.gbcolorpalettes as gbcampalettes


@pytest.mark.parametrize(
    "color,name,value,rgb_colors",
    [
        (
            gbcampalettes.GBColorPalettes.BW,
            "BW",
            ["#FFFFFF", "#A8A8A8", "#545454", "#000000"],
            [[255, 255, 255], [168, 168, 168], [84, 84, 84], [0, 0, 0]],
        ),
        (
            gbcampalettes.GBColorPalettes.GBCEUUS,
            "GBCEUUS",
            ["#FFFFFF", "#7BFF30", "#0163C6", "#000000"],
            [[255, 255, 255], [123, 255, 48], [1, 99, 198], [0, 0, 0]],
        ),
    ],
)
def test_gbcolorpalettes(
    color: gbcampalettes.GBColorPalettes,
    name: str,
    value: List[str],
    rgb_colors: List[List[int]],
):
    """Test gbcampalettes.GBColorPalettes object."""
    assert color.value == value
    assert color.name == name
    assert str(color) == f"{name} : {value}"
    assert color.rgb_colors == rgb_colors
    assert color.describe() == (name, value)


@pytest.mark.parametrize(
    "value,excepted",
    [
        (0, (0, True)),
        (125, (125, True)),
        (255, (255, True)),
        (-255, (0, False)),
        (512, (255, False)),
    ],
)
def test_clamp_int(value, excepted):
    """Test `clamp` and `is_clampled` methods."""
    assert color_helpers.clamp(value) == excepted[0]
    assert color_helpers.is_clamped(value) == excepted[1]


@pytest.mark.parametrize(
    "value,excepted",
    [
        ([0, 0, 0], ([0, 0, 0], True)),
        ([255, 255, 255], ([255, 255, 255], True)),
        ([512, 0, 0], ([255, 0, 0], False)),
        (np.array([0, 0, 0]), ([0, 0, 0], True)),
        (np.array([255, 255, 255]), ([255, 255, 255], True)),
        (np.array([512, 0, 0]), ([255, 0, 0], False)),
    ],
)
def test_clamp_rgb(value, excepted):
    """Test `clamp_hex` and `is_clampled_hex` methods."""
    assert color_helpers.clamp_rgb(value) == excepted[0]
    assert color_helpers.is_clamped_rgb(value) == excepted[1]


@pytest.mark.parametrize(
    "value,message",
    [
        ([0, 0], "rgb_val argument must be a 3 values list"),
        ([0, 0, 0, 0], "rgb_val argument must be a 3 values list"),
        (np.array([0, 0]), "rgb_val argument must be a 3 values list"),
        (np.array([0, 0, 0, 0]), "rgb_val argument must be a 3 values list"),
    ],
)
def test_raises_clamp_rgb(value, message):
    """Test exception in `clamp_hex` and `is_clampled_hex` methods."""
    with pytest.raises(ValueError, match=message):
        color_helpers.clamp_rgb(value)


@pytest.mark.parametrize(
    "value,message",
    [
        ([0, 0], "rgb_val argument must be a 3 values list"),
        ([0, 0, 0, 0], "rgb_val argument must be a 3 values list"),
    ],
)
def test_raises_is_clamped_rgb(value, message):
    """Test exception in `clamp_hex` and `is_clampled_hex` methods."""
    with pytest.raises(ValueError, match=message):
        color_helpers.is_clamped_rgb(value)


@pytest.mark.parametrize(
    "value,excepted",
    [
        ("#000000", ("#000000", True)),
        ("#FFFFFF", ("#FFFFFF", True)),
        ("#00FF00", ("#00FF00", True)),
        ("#F000000", ("#FFFFFF", False)),
    ],
)
def test_clamp_hex(value, excepted):
    """Test `clamp_hex` and `is_clampled_hex` methods."""
    assert color_helpers.clamp_hex(value) == excepted[0]
    assert color_helpers.is_clamped_hex(value) == excepted[1]


@pytest.mark.parametrize(
    "value,expected",
    [
        ("#000000", [0, 0, 0]),
        ("#FF0000", [255, 0, 0]),
        ("#F000000", [255, 255, 255]),
    ],
)
def test_hex_to_rgb(value, expected):
    """Test `hex_to_rgb` conversion."""
    assert color_helpers.hex_to_rgb(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ("#000000", [0, 0, 0]),
        ("#FF0000", [0, 0, 255]),
        ("#F000000", [255, 255, 255]),
    ],
)
def test_hex_to_bgr(value, expected):
    """Test `hex_to_bgr` method."""
    assert color_helpers.hex_to_bgr(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ([0, 0, 0], "#000000"),
        ([255, 0, 0], "#FF0000"),
        ([255, 255, 255], "#FFFFFF"),
    ],
)
def test_(value, expected):
    """Test `rgb_to_hex` method."""
    assert color_helpers.rgb_to_hex(value) == expected


@pytest.mark.parametrize(
    "value,message",
    [
        ([0, 0], "rgb_val argument must be a 3 values list"),
        ([0, 0, 0, 0], "rgb_val argument must be a 3 values list"),
    ],
)
def test_raises_rgb_to_hex(value, message):
    """Test exception in `rgb_to_hex` method."""
    with pytest.raises(ValueError, match=message):
        color_helpers.rgb_to_hex(value)


@pytest.mark.parametrize(
    "value,expected",
    [
        ([0, 0, 0], "#000000"),
        ([0, 0, 255], "#FF0000"),
        ([255, 255, 255], "#FFFFFF"),
    ],
)
def test_bgr_to_hex(value, expected):
    """Test `bgr_to_hex` method."""
    assert color_helpers.bgr_to_hex(value) == expected


@pytest.mark.parametrize(
    "value,message",
    [
        ([0, 0], "bgr_val argument must be a 3 values list"),
        ([0, 0, 0, 0], "bgr_val argument must be a 3 values list"),
    ],
)
def test_raises_bgr_to_hex(value, message):
    """Test exception in `bgr_to_hex` method."""
    with pytest.raises(ValueError, match=message):
        color_helpers.bgr_to_hex(value)
