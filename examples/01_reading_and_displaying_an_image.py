from GameBEye.gbcamimage import gbcamimage
import cv2

# Path to the image
image_filepath = 'images\\originalImage.png'

# Creation of an GCCamImage object
gb_image = gbcamimage.GBCamImage()

# Reading of the file
gb_image.read(image_filepath)

# Logging some info
print("Image filename : {}".format(image_filepath))
print("GBColorPalette name : {}".format(gb_image.color_palette))

# Displaying the image
title = 'Original image with {} color palette'.format(
    gb_image.color_palette.name)
cv2.imshow(title, gb_image.data)
cv2.waitKey()
cv2.destroyWindow(title)
