"""Define the GBColorPalettes enum."""

from enum import Enum, unique
from typing import List, Tuple

from gamebeye.color_helpers import hex_to_rgb


# Class decorator @unique ensure each enum value is unique
@unique
class GBColorPalettes(Enum):
    """
    56 Pre-defined color palettes based upon Game Boy Camera known palettes.

    The GBColorPalettes class inherits from Enum class where the keys are
    the color palette names and the valuea 4 elements array whose values
    represent a color coded in hexadecimal basis.
    """

    BW = ["#FFFFFF", "#A8A8A8", "#545454", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/BW.png">
        <p>BW color palette</p>
        </div>
        </div>
    """

    DMG = ["#9BBC0F", "#77A112", "#306230", "#0F380F"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/DMG.png">
        <p>DMG color palette</p>
        </div>
        </div>
    """

    GBPOCKET = ["#C4CFA1", "#8B956D", "#4D533C", "#1F1F1F"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBPOCKET.png">
        <p>GBPOCKET color palette</p>
        </div>
        </div>
    """

    BGB = ["#E0F8D0", "#88C070", "#346856", "#081820"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/BGB.png">
        <p>BGB color palette</p>
        </div>
        </div>
    """

    GBLIT = ["#1DDECE", "#19C7B3", "#16A596", "#0B7A6D"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBLIT.png">
        <p>GBLIT color palette</p>
        </div>
        </div>
    """

    GRAFIXKIDGRAY = ["#E0DBCD", "#A89F94", "#706B66", "#2B2B26"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GRAFIXKIDGRAY.png">
        <p>GRAFIXKIDGRAY color palette</p>
        </div>
        </div>
    """

    GRAFIXKIDGREEN = ["#DBF4B4", "#ABC396", "#7B9278", "#4C625A"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GRAFIXKIDGREEN.png">
        <p>GRAFIXKIDGREEN color palette</p>
        </div>
        </div>
    """

    BLACKZERO = ["#7E8416", "#577B46", "#385D49", "#2E463D"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/BLACKZERO.png">
        <p>BLACKZERO color palette</p>
        </div>
        </div>
    """

    GBCJP = ["#FFFFFF", "#FFAD63", "#833100", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCJP.png">
        <p>GBCJP color palette</p>
        </div>
        </div>
    """

    GBCUA = ["#FFFFFF", "#FF8F84", "#943A3A", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCUA.png">
        <p>GBCUA color palette</p>
        </div>
        </div>
    """

    GBCUC = ["#FFE7C5", "#CE9C85", "#846B29", "#5B3109"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCUC.png">
        <p>GBCUC color palette</p>
        </div>
        </div>
    """

    GBCL = ["#FFFFFF", "#65A49B", "#0000FE", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCL.png">
        <p>GBCL color palette</p>
        </div>
        </div>
    """

    GBCLA = ["#FFFFFF", "#8B8CDE", "#53528C", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCLA.png">
        <p>GBCLA color palette</p>
        </div>
        </div>
    """

    GBCLB = ["#FFFFFF", "#A5A5A5", "#525252", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCLB.png">
        <p>GBCLB color palette</p>
        </div>
        </div>
    """

    GBCD = ["#FFFFA5", "#FE9494", "#9395FE", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCD.png">
        <p>GBCD color palette</p>
        </div>
        </div>
    """

    GBCDA = ["#FFFFFF", "#FFFF00", "#FE0000", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCDA.png">
        <p>GBCDA color palette</p>
        </div>
        </div>
    """

    GBCDB = ["#FFFFFF", "#FFFF00", "#7D4900", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCDB.png">
        <p>GBCDB color palette</p>
        </div>
        </div>
    """

    GBCR = ["#FFFFFF", "#51FF00", "#FF4200", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCR.png">
        <p>GBCR color palette</p>
        </div>
        </div>
    """

    GBCEUUS = ["#FFFFFF", "#7BFF30", "#0163C6", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCEUUS.png">
        <p>GBCEUUS color palette</p>
        </div>
        </div>
    """

    GBCRB = ["#000000", "#008486", "#FFDE00", "#FFFFFF"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCRB.png">
        <p>GBCRB color palette</p>
        </div>
        </div>
    """

    CYBL = ["#9EFBE3", "#21AFF5", "#1E4793", "#0E1E3D"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CYBL.png">
        <p>CYBL color palette</p>
        </div>
        </div>
    """

    AQPP = ["#EBEEE7", "#868779", "#FA2B25", "#2A201E"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/AQPP.png">
        <p>AQPP color palette</p>
        </div>
        </div>
    """

    WTFP = ["#CECECE", "#6F9EDF", "#42678E", "#102533"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/WTFP.png">
        <p>WTFP color palette</p>
        </div>
        </div>
    """

    CHIG = ["#D0D058", "#A0A840", "#708028", "#405010"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CHIG.png">
        <p>CHIG color palette</p>
        </div>
        </div>
    """

    RCS = ["#EDB4A1", "#A96868", "#764462", "#2C2137"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/RCS.png">
        <p>RCS color palette</p>
        </div>
        </div>
    """

    FSIL = ["#EAF5FA", "#5FB1F5", "#D23C4E", "#4C1C2D"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/FSIL.png">
        <p>FSIL color palette</p>
        </div>
        </div>
    """

    SHZOL = ["#F8E3C4", "#CC3495", "#6B1FB1", "#0B0630"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/SHZOL.png">
        <p>SHZOL color palette</p>
        </div>
        </div>
    """

    TDOYC = ["#B5FF32", "#FF2261", "#462917", "#1D1414"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/TDOYC.png">
        <p>TDOYC color palette</p>
        </div>
        </div>
    """

    CFP = ["#CF9255", "#CF7163", "#B01553", "#3F1711"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CFP.png">
        <p>CFP color palette</p>
        </div>
        </div>
    """

    SFH = ["#FFFF55", "#FF5555", "#881400", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/SFH.png">
        <p>SFH color palette</p>
        </div>
        </div>
    """

    DHG = ["#A1D909", "#467818", "#27421F", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/DHG.png">
        <p>DHG color palette</p>
        </div>
        </div>
    """

    YIRL = ["#CEF7F7", "#F78E50", "#9E0000", "#1E0000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/YIRL.png">
        <p>YIRL color palette</p>
        </div>
        </div>
    """

    CCTR = ["#E6AEC4", "#E65790", "#8F0039", "#380016"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CCTR.png">
        <p>CCTR color palette</p>
        </div>
        </div>
    """

    D2KR = ["#FCF1CD", "#C09E7D", "#725441", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/D2KR.png">
        <p>D2KR color palette</p>
        </div>
        </div>
    """

    SHMGY = ["#F7E7C6", "#D68E49", "#A63725", "#331E50"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/SHMGY.png">
        <p>SHMGY color palette</p>
        </div>
        </div>
    """

    LLAWK = ["#FFFFB5", "#7BC67B", "#6B8C42", "#5A3921"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/LLAWK.png">
        <p>LLAWK color palette</p>
        </div>
        </div>
    """

    CGA1 = ["#FFFFFF", "#55FFFF", "#FF55FF", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CGA1.png">
        <p>CGA1 color palette</p>
        </div>
        </div>
    """

    CGA2 = ["#FFFFFF", "#55FFFF", "#FF5555", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CGA2.png">
        <p>CGA2 color palette</p>
        </div>
        </div>
    """

    MARMX = ["#AEDF1E", "#047E60", "#B62558", "#2C1700"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/MARMX.png">
        <p>MARMX color palette</p>
        </div>
        </div>
    """

    SLMEM = ["#869AD9", "#6D53BD", "#6F2096", "#4F133F"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/SLMEM.png">
        <p>SLMEM color palette</p>
        </div>
        </div>
    """

    DATN = ["#A9B0B3", "#586164", "#20293F", "#030C22"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/DATN.png">
        <p>DATN color palette</p>
        </div>
        </div>
    """

    TSK = ["#F5DB37", "#37CAE5", "#0F86B6", "#123F77"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/TSK.png">
        <p>TSK color palette</p>
        </div>
        </div>
    """

    PPR = ["#ADFFFC", "#8570B2", "#FF0084", "#68006A"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/PPR.png">
        <p>PPR color palette</p>
        </div>
        </div>
    """

    CMYK = ["#FFFF00", "#0BE8FD", "#FB00FA", "#373737"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CMYK.png">
        <p>CMYK color palette</p>
        </div>
        </div>
    """

    VB85 = ["#FF0000", "#DB0000", "#520000", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/VB85.png">
        <p>VB85 color palette</p>
        </div>
        </div>
    """

    AZC = ["#47FF99", "#32B66D", "#124127", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/AZC.png">
        <p>AZC color palette</p>
        </div>
        </div>
    """

    GELC = ["#FF9C00", "#C27600", "#4F3000", "#000000"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GELC.png">
        <p>GELC color palette</p>
        </div>
        </div>
    """

    ROGA = ["#EBC4AB", "#649A57", "#574431", "#323727"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/ROGA.png">
        <p>ROGA color palette</p>
        </div>
        </div>
    """

    KDITW = ["#FFFE6E", "#D5690F", "#3C3CA9", "#2C2410"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/KDITW.png">
        <p>KDITW color palette</p>
        </div>
        </div>
    """

    DIMWM = ["#FFDBCB", "#F27D7A", "#558429", "#222903"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/DIMWM.png">
        <p>DIMWM color palette</p>
        </div>
        </div>
    """

    SPEZI = ["#FEDA1B", "#DF7925", "#B60077", "#382977"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/SPEZI.png">
        <p>SPEZI color palette</p>
        </div>
        </div>
    """

    FFS = ["#E9D9CC", "#C5C5CE", "#75868F", "#171F62"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/FFS.png">
        <p>FFS color palette</p>
        </div>
        </div>
    """

    BANANA = ["#FDFE0A", "#FED638", "#977B25", "#221A09"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/BANANA.png">
        <p>BANANA color palette</p>
        </div>
        </div>
    """

    HIPSTER = ["#FDFEF5", "#DEA963", "#9E754F", "#241606"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/HIPSTER.png">
        <p>HIPSTER color palette</p>
        </div>
        </div>
    """

    NC = ["#FCFE54", "#54FEFC", "#04AAAC", "#0402AC"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/NC.png">
        <p>NC color palette</p>
        </div>
        </div>
    """

    GLMO = ["#FFBF98", "#A1A8B8", "#514F6C", "#2F1C35"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GLMO.png">
        <p>GLMO color palette</p>
        </div>
        </div>
    """

    TPA = ["#F3C677", "#E64A4E", "#912978", "#0C0A3E"]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/TPA.png">
        <p>TPA color palette</p>
        </div>
        </div>
    """

    def describe(self) -> Tuple[str, list]:
        """
        Describe itself. Return as a tuple the color palette name and colors.

        :returns: a 2-values tuple containing the color name and its values
        :rtype: str, list

        >>> from gamebeye.gbcamcolors.gbcamcolors import GBColorPalettes
        >>> GBColorPalettes.BW.describe()
        ('BW', ['#FFFFFF', '#A8A8A8', '#545454', '#000000'])
        """
        return self.name, self.value

    def __str__(self) -> str:
        """
        Convert the enum member to a formatted string.

        :returns: the enum member as a string
        :rtype: str

        >>> from gamebeye.gbcamcolors.gbcamcolors import GBColorPalettes
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

        >>> from gamebeye.gbcamcolors.gbcamcolors import GBColorPalettes
        >>> GBColorPalettes.BW.rgb_colors
        [[255, 255, 255], [168, 168, 168], [84, 84, 84], [0, 0, 0]]
        """
        return [list(hex_to_rgb(hex_value)) for hex_value in self.value]
