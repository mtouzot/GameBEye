"""An example to use the thermal printer effect on an image."""

from GameBEye.gbcamimage import GBCamImage
import GameBEye.gbcamfilters as gbcamfilters
import cv2

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
cv2.destroyWindow(original_title)
cv2.destroyWindow(printed_title)
