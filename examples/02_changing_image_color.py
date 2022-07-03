from GameBEye.gbcamimage import gbcamimage
from GameBEye.gbcamcolors.gbcamcolors import GBColorPalettes
import cv2

# Path to the image
image_filepath = 'images\\originalImage.png'
img = cv2.imread(image_filepath)

# Creation of an GCCamImage object
gb_image = gbcamimage.GBCamImage()
# Reading of the file
gb_image.read(image_filepath)

# Displaying the original image
original_title = 'Original image with {} color palette'.format(
    gb_image.color_palette.name)
cv2.imshow(original_title, gb_image.data)
print('Original color palette : {}'.format(gb_image.color_palette))

# Changing image color palette
gb_color_palette = GBColorPalettes.AZC
gb_image.change_color(color_palette=gb_color_palette)

# Displaying the colorized image
color_title = 'Colorized image with {} color palette'.format(
    gb_image.color_palette.name)
cv2.imshow(color_title, gb_image.data)
print('Colorized image color palette : {}\nRequired color palette : {}'.format(
    gb_image.color_palette, gb_color_palette))

cv2.waitKey()
cv2.destroyWindow(original_title)
cv2.destroyWindow(color_title)
