Convert an image to the closest GBColorPalettes
-----------------------------------------------

In this example, the `originalImage.jpg` has been converted from the `png` one to `jpg` format. The conversion has altered the color palette. This example shows how to be sure that the read image has a valid color palette, by setting the `convert` boolean to `True`.

Here are the `jpg` image first, followed by the `png` one, then by the converted one (visual color difference may be visually difficult to see):

.. container:: centered-grid

   .. raw:: html

      <div class="grid-item">
         <img src="https://media.githubusercontent.com/media/mtouzot/GameBEye/master/examples/images/originalImage.jpg" alt="Original Game Boy Camera Image (JPG format)">
         <p>Original Game Boy Camera Image (JPG format)</p>
      </div>
      <div class="grid-item">
         <img src="https://media.githubusercontent.com/media/mtouzot/GameBEye/master/examples/images/originalImage.png" alt="Original Game Boy Camera Image (PNG format)">
         <p>Original Game Boy Camera Image (PNG format)</p>
      </div>
      <div class="grid-item">
         <img src="https://media.githubusercontent.com/media/mtouzot/GameBEye/master/examples/images/convertedOriginalImage.jpg" alt="Converted original Game Boy Camera Image (JPG format)">
         <p>Converted original Game Boy Camera Image (JPG format)</p>
      </div>
      <div class="grid-item">
         <img src="https://media.githubusercontent.com/media/mtouzot/GameBEye/master/examples/images/convertedOriginalImage.png" alt="Converted original Game Boy Camera Image (PNG format)">
         <p>Converted original Game Boy Camera Image (PNG format)</p>
      </div>

.. code-block:: python
   :linenos:

   """An example to show an image, to log its name and color palette."""

    import cv2

    from gamebeye.gbcamimage.gbcamimage import GBCamImage

    # Path to the image
    image_filepath = "images\\originalImage.jpg"

    # Creation of an GCCamImage object
    gb_img = GBCamImage()

    # Reading of the file
    gb_img.read(image_filepath, convert=True)

    # Logging some info
    print("Image filename : {}".format(image_filepath))
    print("GBColorPalette name : {}".format(gb_img.color_palette))

    # Displaying the image
    title = "GB image with {} color palette".format(gb_img.color_palette.name)
    cv2.imshow(title, gb_img.data)
    cv2.waitKey()
    cv2.destroyWindow(title)
