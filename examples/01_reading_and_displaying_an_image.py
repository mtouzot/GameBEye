"""An example to show an image, to log its name and color palette."""

from GameBEye.gbcamimage import gbcamimage
import cv2

# Path to the image
image_filepath = "images\\originalImage.png"

# Creation of an GCCamImage object
gb_img = gbcamimage.GBCamImage()

# Reading of the file
gb_img.read(image_filepath)

# Logging some info
print("Image filename : {}".format(image_filepath))
print("GBColorPalette name : {}".format(gb_img.color_palette))

# Displaying the image
title = "GB image with {} color palette".format(gb_img.color_palette.name)
cv2.imshow(title, gb_img.data)
cv2.waitKey()
cv2.destroyWindow(title)
