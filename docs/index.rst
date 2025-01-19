Welcome to GameBEye's documentation!
====================================

|Github| |License| |Issues| |Release|

GameBEye is a **Python library** to process `Game Boy Camera <https://en.wikipedia.org/wiki/Game_Boy_Camera>`_ images.

+-----------------------------------------------------+-----------------------------------------------------+-----------------------------------------------------+-----------------------------------------------------+
| Original image                                      | Borderless image                                    | Animated GIF made of colorized images               | Printed Game Boy Camera image                       |
+=====================================================+=====================================================+=====================================================+=====================================================+
| .. image:: ./_static/gameBoyCamera.png              | .. image:: ./_static/borderlessGameBoyCamera.png    | .. image:: ./_static/colorizedGameBoyCamera.gif     | .. image:: ./_static/printedGameBoyCamera.png       |
|    :class: align-center                             |    :class: align-center                             |    :class: align-center                             |    :class: align-center                             |
+-----------------------------------------------------+-----------------------------------------------------+-----------------------------------------------------+-----------------------------------------------------+

Here are some infos about the hardware and the Gam Boy Camera images that drive the library construction:

 * the CMOS sensor of the camera cartridge is *only* 128x128 pixels but the images are cropped to **128x112 pixels**. This means all images are Nintendo borderless.
 * the image can be framed with a Nintendo border increasing the image size to **160x144 pixels**.
 * the images use a **4-color palette**.

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: Contents:

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