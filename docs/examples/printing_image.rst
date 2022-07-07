Printing a GBCamImage
---------------------

Thanks to `Raphael BOICHOT <https://github.com/Raphael-Boichot>`_ who works on a `Game Boy Printer Paper Simulation <https://github.com/Raphael-Boichot/GameboyPrinterPaperSimulation>`_,
here's an example of how looks a printed image

.. code-block:: python
   :linenos:

   from GameBEye.gbcamimage import gbcamimage
   from GameBEye.gbcamfilters import gbcamfilters
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

   printed_image = gbcamfilters.to_thermal_printer(gb_img)
   printed_title = "Printed image"
   cv2.imshow(printed_title, printed_image)


   cv2.waitKey()
   cv2.destroyWindow(original_title)
   cv2.destroyWindow(printed_title)


So from this input :

.. figure:: ../_static/gameBoyCamera.png
   :alt: Original Game Boy Camera image
   :align: center

   Original Game Boy Camera image

The output image is the following one :

.. figure:: ../_static/printedGameBoyCamera.png
   :alt: Printed original Game Boy Camera image
   :align: center

   Printed original Game Boy Camera image