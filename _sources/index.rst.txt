Welcome to GameBEye's documentation!
====================================

|Github| |License| |Issues| |Release|

GameBEye is a **Python library** to process `Game Boy Camera <https://en.wikipedia.org/wiki/Game_Boy_Camera>`_ images.

Here are what a Game Boy camera can capture:

.. container:: centered-grid

   .. raw:: html

      <div class="grid-item">
         <img src="./_static/gameBoyCamera.png" alt="Original Game Boy Camera Image">
         <p>Original Game Boy Camera Image</p>
      </div>
      <div class="grid-item">
         <img src="_static/borderlessGameBoyCamera.png" alt="Borderless Game Boy Camera Image">
         <p>Borderless Game Boy Camera Image</p>
      </div>
      <div class="grid-item">
         <img src="_static/colorizedGameBoyCamera.gif" alt="Animated GIF made of colorized images">
         <p>Animated GIF made of colorized images</p>
      </div>
      <div class="grid-item">
         <img src="_static/printedGameBoyCamera.png" alt="Printed Game Boy Camera Image">
         <p>Printed Game Boy Camera Image</p>
      </div>

Here are some infos about the hardware and the Gam Boy Camera images that drive the library construction:

 * the CMOS sensor of the camera cartridge is *only* 128x128 pixels but the images are cropped to **128x112 pixels**. This means all images are Nintendo borderless.
 * the image can be framed with a Nintendo border increasing the image size to **160x144 pixels**.
 * the images use a **4-grayscale palette**:

.. container:: centered-grid

   .. raw:: html

      <div class="grid-item">
         <img src="./_static/colorPalettes/BW.png" alt="Original color palette for Game Boy Camera Images">
         <p>Original color palette for Game Boy Camera Images</p>
      </div>

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: Contents:

   ./hardware.rst
   ./installation.rst
   ./GameBEye.rst
   ./examples.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. |Github| image:: https://img.shields.io/github/stars/mtouzot/GameBEye?label=Github&logo=github
   :target: https://github.com/mtouzot/GameBEye

.. |License| image:: https://img.shields.io/github/license/mtouzot/GameBEye
   :target: https://github.com/mtouzot/GameBEye/blob/master/LICENSE

.. |Issues| image:: https://img.shields.io/github/issues/mtouzot/GameBEye
   :target: https://github.com/mtouzot/GameBEye/issues

.. |Release| image:: https://img.shields.io/github/v/release/mtouzot/GameBEye
   :target: https://github.com/mtouzot/GameBEye/releases

.. |BWpalette| image:: ./_static/colorPalettes/BW.png
   :class: align-center
   :alt: Original BW color palette
