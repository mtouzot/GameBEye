"""An example to display both image and its corresponding color palette."""

from GameBEye.gbcamimage import GBCamImage
from GameBEye.color_helpers import hex_to_rgb
import numpy as np
import cv2
import os

input_folder = os.path.join("images", "colorizedImages")
images_filepath = sorted(
    [
        os.path.join(input_folder, filename)
        for filename in os.listdir(input_folder)
    ]
)

for image_filepath in images_filepath:
    print(f"Processing {image_filepath}")
    gb_image = GBCamImage()

    # Reading of the file
    gb_image.read(image_filepath)

    # Displaying the colorized image
    image_title = "Colorized image with {} color palette".format(
        gb_image.color_palette.name
    )
    cv2.imshow(image_title, gb_image.data)

    # Create a numpy image with each color of the gb_image color palette
    # Join them to have a 4-elements array to print the color palette
    color_palettes = []
    for color in gb_image.color_palette.value:
        rgb_color = hex_to_rgb(color)
        red = rgb_color[0] * np.ones((112, 128)).astype("uint8")
        green = rgb_color[1] * np.ones((112, 128)).astype("uint8")
        blue = rgb_color[2] * np.ones((112, 128)).astype("uint8")
        color_palettes.append(cv2.merge([blue, green, red]))
    color_palettes = cv2.hconcat(color_palettes)

    color_palette_title = "Color palettes {}".format(
        gb_image.color_palette.name
    )
    cv2.imshow(color_palette_title, color_palettes)

    cv2.waitKey()
    cv2.destroyWindow(image_title)
    cv2.destroyWindow(color_palette_title)
