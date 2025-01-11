"""Defines the GBColorPalettes enum."""

from enum import Enum, unique
from typing import Tuple, List
from .color_helpers import hex_to_rgb


# Class decorator @unique ensure each enum value is unique
@unique
class GBColorPalettes(Enum):
    """
    56 Pre-defined color palettes based upon Game Boy Camera known palettes.

    The GBColorPalettes class inherits from Enum class where the keys are
    the color palette names and the valuea 4 elements array whose values
    represent a color coded in hexadecimal basis.
    """

    #: .. image:: ../_static/colorPalettes/BW.png
    BW = ["#FFFFFF", "#A8A8A8", "#545454", "#000000"]

    #: .. image:: ../_static/colorPalettes/DMG.png
    DMG = ["#9BBC0F", "#77A112", "#306230", "#0F380F"]

    #: .. image:: ../_static/colorPalettes/GBPOCKET.png
    GBPOCKET = ["#C4CFA1", "#8B956D", "#4D533C", "#1F1F1F"]

    #: .. image:: ../_static/colorPalettes/BGB.png
    BGB = ["#E0F8D0", "#88C070", "#346856", "#081820"]

    #: .. image:: ../_static/colorPalettes/GBLIT.png
    GBLIT = ["#1DDECE", "#19C7B3", "#16A596", "#0B7A6D"]

    #: .. image:: ../_static/colorPalettes/GRAFIXKIDGRAY.png
    GRAFIXKIDGRAY = ["#E0DBCD", "#A89F94", "#706B66", "#2B2B26"]

    #: .. image:: ../_static/colorPalettes/GRAFIXKIDGREEN.png
    GRAFIXKIDGREEN = ["#DBF4B4", "#ABC396", "#7B9278", "#4C625A"]

    #: .. image:: ../_static/colorPalettes/BLACKZERO.png
    BLACKZERO = ["#7E8416", "#577B46", "#385D49", "#2E463D"]

    #: .. image:: ../_static/colorPalettes/GBCJP.png
    GBCJP = ["#FFFFFF", "#FFAD63", "#833100", "#000000"]

    #: .. image:: ../_static/colorPalettes/GBCUA.png
    GBCUA = ["#FFFFFF", "#FF8F84", "#943A3A", "#000000"]

    #: .. image:: ../_static/colorPalettes/GBCUC.png
    GBCUC = ["#FFE7C5", "#CE9C85", "#846B29", "#5B3109"]

    #: .. image:: ../_static/colorPalettes/GBCL.png
    GBCL = ["#FFFFFF", "#65A49B", "#0000FE", "#000000"]

    #: .. image:: ../_static/colorPalettes/GBCLA.png
    GBCLA = ["#FFFFFF", "#8B8CDE", "#53528C", "#000000"]

    #: .. image:: ../_static/colorPalettes/GBCLB.png
    GBCLB = ["#FFFFFF", "#A5A5A5", "#525252", "#000000"]

    #: .. image:: ../_static/colorPalettes/GBCD.png
    GBCD = ["#FFFFA5", "#FE9494", "#9395FE", "#000000"]

    #: .. image:: ../_static/colorPalettes/GBCDA.png
    GBCDA = ["#FFFFFF", "#FFFF00", "#FE0000", "#000000"]

    #: .. image:: ../_static/colorPalettes/GBCDB.png
    GBCDB = ["#FFFFFF", "#FFFF00", "#7D4900", "#000000"]

    #: .. image:: ../_static/colorPalettes/GBCR.png
    GBCR = ["#FFFFFF", "#51FF00", "#FF4200", "#000000"]

    #: .. image:: ../_static/colorPalettes/GBCEUUS.png
    GBCEUUS = ["#FFFFFF", "#7BFF30", "#0163C6", "#000000"]

    #: .. image:: ../_static/colorPalettes/GBCRB.png
    GBCRB = ["#000000", "#008486", "#FFDE00", "#FFFFFF"]

    #: .. image:: ../_static/colorPalettes/CYBL.png
    CYBL = ["#9EFBE3", "#21AFF5", "#1E4793", "#0E1E3D"]

    #: .. image:: ../_static/colorPalettes/AQPP.png
    AQPP = ["#EBEEE7", "#868779", "#FA2B25", "#2A201E"]

    #: .. image:: ../_static/colorPalettes/WTFP.png
    WTFP = ["#CECECE", "#6F9EDF", "#42678E", "#102533"]

    #: .. image:: ../_static/colorPalettes/CHIG.png
    CHIG = ["#D0D058", "#A0A840", "#708028", "#405010"]

    #: .. image:: ../_static/colorPalettes/RCS.png
    RCS = ["#EDB4A1", "#A96868", "#764462", "#2C2137"]

    #: .. image:: ../_static/colorPalettes/FSIL.png
    FSIL = ["#EAF5FA", "#5FB1F5", "#D23C4E", "#4C1C2D"]

    #: .. image:: ../_static/colorPalettes/SHZOL.png
    SHZOL = ["#F8E3C4", "#CC3495", "#6B1FB1", "#0B0630"]

    #: .. image:: ../_static/colorPalettes/TDOYC.png
    TDOYC = ["#B5FF32", "#FF2261", "#462917", "#1D1414"]

    #: .. image:: ../_static/colorPalettes/CFP.png
    CFP = ["#CF9255", "#CF7163", "#B01553", "#3F1711"]

    #: .. image:: ../_static/colorPalettes/SFH.png
    SFH = ["#FFFF55", "#FF5555", "#881400", "#000000"]

    #: .. image:: ../_static/colorPalettes/DHG.png
    DHG = ["#A1D909", "#467818", "#27421F", "#000000"]

    #: .. image:: ../_static/colorPalettes/YIRL.png
    YIRL = ["#CEF7F7", "#F78E50", "#9E0000", "#1E0000"]

    #: .. image:: ../_static/colorPalettes/CCTR.png
    CCTR = ["#E6AEC4", "#E65790", "#8F0039", "#380016"]

    #: .. image:: ../_static/colorPalettes/D2KR.png
    D2KR = ["#FCF1CD", "#C09E7D", "#725441", "#000000"]

    #: .. image:: ../_static/colorPalettes/SHMGY.png
    SHMGY = ["#F7E7C6", "#D68E49", "#A63725", "#331E50"]

    #: .. image:: ../_static/colorPalettes/LLAWK.png
    LLAWK = ["#FFFFB5", "#7BC67B", "#6B8C42", "#5A3921"]

    #: .. image:: ../_static/colorPalettes/CGA1.png
    CGA1 = ["#FFFFFF", "#55FFFF", "#FF55FF", "#000000"]

    #: .. image:: ../_static/colorPalettes/CGA2.png
    CGA2 = ["#FFFFFF", "#55FFFF", "#FF5555", "#000000"]

    #: .. image:: ../_static/colorPalettes/MARMX.png
    MARMX = ["#AEDF1E", "#047E60", "#B62558", "#2C1700"]

    #: .. image:: ../_static/colorPalettes/SLMEM.png
    SLMEM = ["#869AD9", "#6D53BD", "#6F2096", "#4F133F"]

    #: .. image:: ../_static/colorPalettes/DATN.png
    DATN = ["#A9B0B3", "#586164", "#20293F", "#030C22"]

    #: .. image:: ../_static/colorPalettes/TSK.png
    TSK = ["#F5DB37", "#37CAE5", "#0F86B6", "#123F77"]

    #: .. image:: ../_static/colorPalettes/PPR.png
    PPR = ["#ADFFFC", "#8570B2", "#FF0084", "#68006A"]

    #: .. image:: ../_static/colorPalettes/CMYK.png
    CMYK = ["#FFFF00", "#0BE8FD", "#FB00FA", "#373737"]

    #: .. image:: ../_static/colorPalettes/VB85.png
    VB85 = ["#FF0000", "#DB0000", "#520000", "#000000"]

    #: .. image:: ../_static/colorPalettes/AZC.png
    AZC = ["#47FF99", "#32B66D", "#124127", "#000000"]

    #: .. image:: ../_static/colorPalettes/GELC.png
    GELC = ["#FF9C00", "#C27600", "#4F3000", "#000000"]

    #: .. image:: ../_static/colorPalettes/ROGA.png
    ROGA = ["#EBC4AB", "#649A57", "#574431", "#323727"]

    #: .. image:: ../_static/colorPalettes/KDITW.png
    KDITW = ["#FFFE6E", "#D5690F", "#3C3CA9", "#2C2410"]

    #: .. image:: ../_static/colorPalettes/DIMWM.png
    DIMWM = ["#FFDBCB", "#F27D7A", "#558429", "#222903"]

    #: .. image:: ../_static/colorPalettes/SPEZI.png
    SPEZI = ["#FEDA1B", "#DF7925", "#B60077", "#382977"]

    #: .. image:: ../_static/colorPalettes/FFS.png
    FFS = ["#E9D9CC", "#C5C5CE", "#75868F", "#171F62"]

    #: .. image:: ../_static/colorPalettes/BANANA.png
    BANANA = ["#FDFE0A", "#FED638", "#977B25", "#221A09"]

    #: .. image:: ../_static/colorPalettes/HIPSTER.png
    HIPSTER = ["#FDFEF5", "#DEA963", "#9E754F", "#241606"]

    #: .. image:: ../_static/colorPalettes/NC.png
    NC = ["#FCFE54", "#54FEFC", "#04AAAC", "#0402AC"]

    #: .. image:: ../_static/colorPalettes/GLMO.png
    GLMO = ["#FFBF98", "#A1A8B8", "#514F6C", "#2F1C35"]

    #: .. image:: ../_static/colorPalettes/TPA.png
    TPA = ["#F3C677", "#E64A4E", "#912978", "#0C0A3E"]

    def describe(self) -> Tuple[str, list]:
        """
        Describe itself. Return as a tuple the color palette name and colors.

        :returns: a 2-values tuple containing the color name and its values
        :rtype: str, list

        >>> from GameBEye.gbcamcolors.gbcamcolors import GBColorPalettes
        >>> GBColorPalettes.BW.describe()
        ('BW', ['#FFFFFF', '#A8A8A8', '#545454', '#000000'])
        """
        return self.name, self.value

    def __str__(self) -> str:
        """
        Convert the enum member to a formatted string.

        :returns: the enum member as a string
        :rtype: str

        >>> from GameBEye.gbcamcolors.gbcamcolors import GBColorPalettes
        >>> str(GBColorPalettes.BW)
        "BW : ['#FFFFFF', '#A8A8A8', '#545454', '#000000']"
        """
        return "{} : {}".format(self.name, str(self.value))

    @property
    def rgb_colors(self) -> List[List[int]]:
        """
        Return the 4 color values of the enum in RGB space.

        :return: the 4 colors values in the RGB space
        :rtype: list[list[int]]

        >>> from GameBEye.gbcamcolors.gbcamcolors import GBColorPalettes
        >>> GBColorPalettes.BW.rgb_colors
        [[255, 255, 255], [168, 168, 168], [84, 84, 84], [0, 0, 0]]
        """
        return [
            [channel_val for channel_val in hex_to_rgb(hex_value)]
            for hex_value in self.value
        ]
