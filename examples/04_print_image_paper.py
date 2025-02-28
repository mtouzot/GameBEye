"""An example to use the thermal printer effect on an image."""

import cv2

import gamebeye.gbcamimage.gbcamfilters as gbcamfilters
from gamebeye.gbcamimage.gbcamimage import GBCamImage

# Path to the image
image_filepath = "images\\originalImage.png"
img = cv2.imread(image_filepath)

# Creation of an GCCamImage object
gb_img = GBCamImage()
# Reading of the file
gb_img.read(image_filepath)

# Displaying the original image
original_title = "Original image with {} color palette".format(
    gb_img.color_palette.name
)
cv2.imshow(original_title, gb_img.data)
print("Original color palette : {}".format(gb_img.color_palette))

printed_image = gbcamfilters.to_thermal_printer(gb_img)
printed_title = "Printed image"
cv2.imshow(printed_title, printed_image)


cv2.waitKey()
cv2.destroyAllWindows()
