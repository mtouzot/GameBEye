"""All relative tests to gamebeye.gbcamimage.gbcamimage file."""

import numpy as np
import pytest

import gamebeye.gbcamimage as gbcamimage


def test_gbcamimage():
    """Test gbcamimage.GBCamImage object."""
    image = gbcamimage.GBCamImage()
    assert image.shape == (
        gbcamimage.GBCamImage.HEIGHT,
        gbcamimage.GBCamImage.WIDTH,
        gbcamimage.GBCamImage.CHANNEL,
    )
    np.testing.assert_equal(
        image.data,
        np.zeros(
            (
                gbcamimage.GBCamImage.HEIGHT,
                gbcamimage.GBCamImage.WIDTH,
                gbcamimage.GBCamImage.CHANNEL,
            )
        ),
    )
    assert image.color_palette == gbcamimage.GBColorPalettes.BW


@pytest.mark.parametrize(
    "args, kwargs, expected",
    [
        ([], {}, gbcamimage.GBColorPalettes.BW),
        ([gbcamimage.GBColorPalettes.BW], {}, gbcamimage.GBColorPalettes.BW),
        (
            [],
            {"color_palette": gbcamimage.GBColorPalettes.BANANA},
            gbcamimage.GBColorPalettes.BANANA,
        ),
    ],
)
def test_change_color(args, kwargs, expected):
    """Test the change of color."""
    image = gbcamimage.GBCamImage()
    image.change_color(*args, **kwargs)
    assert image.color_palette == expected
