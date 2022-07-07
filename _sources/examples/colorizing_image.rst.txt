Colorizing a Black & White image
--------------------------------

You'll see in this example the result of updating the color palette of an original color image by using CCTR color palette.

+-----------------------------------------------------+------------------------------------------------------+
| Original image                                      | Output                                               |
+=====================================================+======================================================+
| .. image:: ../_static/gameBoyCamera.png             | .. image:: ../_static/colorizedGameBoyCamera_CCTR.png|
|    :class: align-center                             |    :class: align-center                              |
+-----------------------------------------------------+------------------------------------------------------+

.. code-block:: python
   :linenos:

   from GameBEye.gbcamimage import gbcamimage
   from GameBEye.gbcamcolors.gbcamcolors import GBColorPalettes
   import cv2

   # Path to the image
   image_filepath = "images\\originalImage.png"
   img = cv2.imread(image_filepath)

   # Creation of an GCCamImage object
   gb_img = gbcamimage.GBCamImage()
   # Reading of the file
   gb_img.read(image_filepath)

   # Displaying the original image
   original_title = "Original image with {} color palette".format(
       gb_img.color_palette.name
   )
   cv2.imshow(original_title, gb_img.data)
   print("Original color palette : {}".format(gb_img.color_palette))

   # Changing image color palette
   gb_color_palette = GBColorPalettes.AZC
   gb_img.change_color(color_palette=gb_color_palette)

   # Displaying the colorized image
   color_title = "Colorized image with {} color palette".format(
       gb_img.color_palette.name
   )
   cv2.imshow(color_title, gb_img.data)
   print(
       "Colorized image color palette : {}\nRequired color palette : {}".format(
           gb_img.color_palette, gb_color_palette
       )
   )

   cv2.waitKey()
   cv2.destroyWindow(original_title)
   cv2.destroyWindow(color_title)