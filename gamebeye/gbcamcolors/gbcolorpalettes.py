"""Define the GBColorPalettes enum."""

from enum import Enum, unique
from math import inf
from typing import List, Tuple

from gamebeye.gbcamcolors.color_helpers import hex_to_rgb
from gamebeye.gbcamcolors.gbcolorvalues import GBColorValues


# Class decorator @unique ensure each enum value is unique
@unique
class GBColorPalettes(Enum):
    """
    56 Pre-defined color palettes based upon Game Boy Camera known palettes.

    The GBColorPalettes class inherits from Enum class where the keys are
    the color palette names and the valuea 4 elements array whose values
    represent a color coded in hexadecimal basis.
    """

    BW = [
        GBColorValues.WHITE,
        GBColorValues.UNIFORM_GREY,
        GBColorValues.BRILLIANT_LIQUORICE,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/BW.png">
        <p>BW color palette</p>
        </div>
        </div>
    """

    DMG = [
        GBColorValues.GAMEBOY_LIGHT,
        GBColorValues.LUMINESCENT_GREEN,
        GBColorValues.GAMEBOY_SHADE,
        GBColorValues.GAMEBOY_CONTRAST,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/DMG.png">
        <p>DMG color palette</p>
        </div>
        </div>
    """

    GBPOCKET = [
        GBColorValues.DAPPLED_DAYDREAM,
        GBColorValues.CIDER_PEAR_GREEN,
        GBColorValues.KELP,
        GBColorValues.UMBRA,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBPOCKET.png">
        <p>GBPOCKET color palette</p>
        </div>
        </div>
    """

    BGB = [
        GBColorValues.LIGHT_GREEN_GLINT,
        GBColorValues.LAUDABLE_LIME,
        GBColorValues.PLANTAIN_GREEN,
        GBColorValues.BLACK_STALLION,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/BGB.png">
        <p>BGB color palette</p>
        </div>
        </div>
    """

    GBLIT = [
        GBColorValues.ICE_CLIMBER,
        GBColorValues.EXQUISITE_TURQUOISE,
        GBColorValues.CERAMIC_BLUE_TURQUOISE,
        GBColorValues.BLUE_GREEN,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBLIT.png">
        <p>GBLIT color palette</p>
        </div>
        </div>
    """

    GRAFIXKIDGRAY = [
        GBColorValues.NOBLE_CREAM,
        GBColorValues.LONDON_STONES,
        GBColorValues.GIBRALTAR_GREY,
        GBColorValues.GREEN_WATERLOO,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GRAFIXKIDGRAY.png">
        <p>GRAFIXKIDGRAY color palette</p>
        </div>
        </div>
    """

    GRAFIXKIDGREEN = [
        GBColorValues.CHICON,
        GBColorValues.SEAWASHED_GLASS,
        GBColorValues.LODEN_FROST,
        GBColorValues.VERT_PIERRE,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GRAFIXKIDGREEN.png">
        <p>GRAFIXKIDGREEN color palette</p>
        </div>
        </div>
    """

    BLACKZERO = [
        GBColorValues.ELWYNN_FOREST_OLIVE,
        GBColorValues.MOSSY_GREEN,
        GBColorValues.FRESH_HERBS,
        GBColorValues.BRACKEN_FERN,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/BLACKZERO.png">
        <p>BLACKZERO color palette</p>
        </div>
        </div>
    """

    GBCJP = [
        GBColorValues.WHITE,
        GBColorValues.DREAMY_SUNSET,
        GBColorValues.COFFEE_ADDICTION,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCJP.png">
        <p>GBCJP color palette</p>
        </div>
        </div>
    """

    GBCUA = [
        GBColorValues.WHITE,
        GBColorValues.DESERT_FLOWER,
        GBColorValues.NEW_SLED,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCUA.png">
        <p>GBCUA color palette</p>
        </div>
        </div>
    """

    GBCUC = [
        GBColorValues.CHESS_IVORY,
        GBColorValues.DUSTY_CORAL,
        GBColorValues.AGED_ANTICS,
        GBColorValues.COUNT_CHOCULA,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCUC.png">
        <p>GBCUC color palette</p>
        </div>
        </div>
    """

    GBCL = [
        GBColorValues.WHITE,
        GBColorValues.AQUA_RAPIDS,
        GBColorValues.BLUE,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCL.png">
        <p>GBCL color palette</p>
        </div>
        </div>
    """

    GBCLA = [
        GBColorValues.WHITE,
        GBColorValues.PERRYWINKLE,
        GBColorValues.TWILIGHT,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCLA.png">
        <p>GBCLA color palette</p>
        </div>
        </div>
    """

    GBCLB = [
        GBColorValues.WHITE,
        GBColorValues.RAINY_GREY,
        GBColorValues.CAVERNOUS,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCLB.png">
        <p>GBCLB color palette</p>
        </div>
        </div>
    """

    GBCD = [
        GBColorValues.CALAMANSI,
        GBColorValues.CHERISHED_ONE,
        GBColorValues.PERRYWINKLE_BLUE,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCD.png">
        <p>GBCD color palette</p>
        </div>
        </div>
    """

    GBCDA = [
        GBColorValues.WHITE,
        GBColorValues.YELLOW,
        GBColorValues.RED,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCDA.png">
        <p>GBCDA color palette</p>
        </div>
        </div>
    """

    GBCDB = [
        GBColorValues.WHITE,
        GBColorValues.YELLOW,
        GBColorValues.DRIED_MUSTARD,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCDB.png">
        <p>GBCDB color palette</p>
        </div>
        </div>
    """

    GBCR = [
        GBColorValues.WHITE,
        GBColorValues.HYPER_GREEN,
        GBColorValues.ULTIMATE_ORANGE,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCR.png">
        <p>GBCR color palette</p>
        </div>
        </div>
    """

    GBCEUUS = [
        GBColorValues.WHITE,
        GBColorValues.SPRING_FROST,
        GBColorValues.ROYAL_NAVY_BLUE,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCEUUS.png">
        <p>GBCEUUS color palette</p>
        </div>
        </div>
    """

    GBCRB = [
        GBColorValues.BLACK,
        GBColorValues.FANFARE,
        GBColorValues.GOLDEN_YELLOW,
        GBColorValues.WHITE,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GBCRB.png">
        <p>GBCRB color palette</p>
        </div>
        </div>
    """

    CYBL = [
        GBColorValues.FREEZY_WIND,
        GBColorValues.FANTASY_CONSOLE_SKY,
        GBColorValues.NUIT_BLANCHE,
        GBColorValues.DARK_ECLIPSE,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CYBL.png">
        <p>CYBL color palette</p>
        </div>
        </div>
    """

    AQPP = [
        GBColorValues.CREME_FRAICHE,
        GBColorValues.KOSHER_KHAHI,
        GBColorValues.RED_STOP,
        GBColorValues.VELCET_BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/AQPP.png">
        <p>AQPP color palette</p>
        </div>
        </div>
    """

    WTFP = [
        GBColorValues.WHISPER_OF_SMOKE,
        GBColorValues.ACAPULCO_DIVE,
        GBColorValues.SEA_OF_GALILEE,
        GBColorValues.BLACK_BOX,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/WTFP.png">
        <p>WTFP color palette</p>
        </div>
        </div>
    """

    CHIG = [
        GBColorValues.SALSA_VERDE,
        GBColorValues.LAZY_LIZARD,
        GBColorValues.PESTO_DI_RUCOLA,
        GBColorValues.GODZILLA,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CHIG.png">
        <p>CHIG color palette</p>
        </div>
        </div>
    """

    RCS = [
        GBColorValues.WAX_FLOWER,
        GBColorValues.MELON_TWIST,
        GBColorValues.SCINTILLATING_VIOLET,
        GBColorValues.BLEACHED_CEDAR,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/RCS.png">
        <p>RCS color palette</p>
        </div>
        </div>
    """

    FSIL = [
        GBColorValues.MOON_WHITE,
        GBColorValues.BLUE_JEANS,
        GBColorValues.SMOOCH_ROUGE,
        GBColorValues.DARK_MAHOGANY,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/FSIL.png">
        <p>FSIL color palette</p>
        </div>
        </div>
    """

    SHZOL = [
        GBColorValues.MOONGLOW,
        GBColorValues.ROYAL_FUCHSIA,
        GBColorValues.FUCHSIA_NEBULA,
        GBColorValues.COSMIC_VOID,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/SHZOL.png">
        <p>SHZOL color palette</p>
        </div>
        </div>
    """

    TDOYC = [
        GBColorValues.CHESTNUT_SHELL,
        GBColorValues.PEEVISH_RED,
        GBColorValues.NIGHT_BROWN,
        GBColorValues.BATS_CLOAK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/TDOYC.png">
        <p>TDOYC color palette</p>
        </div>
        </div>
    """

    CFP = [
        GBColorValues.POLO_PONY,
        GBColorValues.OK_CORRAL,
        GBColorValues.CERISE,
        GBColorValues.DARK_SIENNA,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CFP.png">
        <p>CFP color palette</p>
        </div>
        </div>
    """

    SFH = [
        GBColorValues.PILA_YELLOW,
        GBColorValues.FLUORESCENT_RED,
        GBColorValues.RED_LEEVER,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/SFH.png">
        <p>SFH color palette</p>
        </div>
        </div>
    """

    DHG = [
        GBColorValues.VIVID_LIME_GREEN,
        GBColorValues.FOREST_EMPRESS,
        GBColorValues.MYRTLE,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/DHG.png">
        <p>DHG color palette</p>
        </div>
        </div>
    """

    YIRL = [
        GBColorValues.TINTED_ICE,
        GBColorValues.BLAZE,
        GBColorValues.CACODEMON_RED,
        GBColorValues.DWARF_FORTRESS,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/YIRL.png">
        <p>YIRL color palette</p>
        </div>
        </div>
    """

    CCTR = [
        GBColorValues.PINK_MACAROON,
        GBColorValues.CARMINE_ROSE,
        GBColorValues.MADRILENO_MAROON,
        GBColorValues.ILVAITE_BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CCTR.png">
        <p>CCTR color palette</p>
        </div>
        </div>
    """

    D2KR = [
        GBColorValues.HINT_OF_YELLOW,
        GBColorValues.WICKERWORK,
        GBColorValues.MOOSE_FUR,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/D2KR.png">
        <p>D2KR color palette</p>
        </div>
        </div>
    """

    SHMGY = [
        GBColorValues.FLAXSEED,
        GBColorValues.GOLDEN_NUGGET,
        GBColorValues.JAIPUR,
        GBColorValues.POWERFUL_VIOLET,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/SHMGY.png">
        <p>SHMGY color palette</p>
        </div>
        </div>
    """

    LLAWK = [
        GBColorValues.CREME,
        GBColorValues.GARDEN_STROLL,
        GBColorValues.MAKRUT_LIME,
        GBColorValues.KURO_BROWN,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/LLAWK.png">
        <p>LLAWK color palette</p>
        </div>
        </div>
    """

    CGA1 = [
        GBColorValues.WHITE,
        GBColorValues.ELECTRIC_SHEEP,
        GBColorValues.ULTIMATE_PINK,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CGA1.png">
        <p>CGA1 color palette</p>
        </div>
        </div>
    """

    CGA2 = [
        GBColorValues.WHITE,
        GBColorValues.ELECTRIC_SHEEP,
        GBColorValues.FLUORESCENT_RED,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CGA2.png">
        <p>CGA2 color palette</p>
        </div>
        </div>
    """

    MARMX = [
        GBColorValues.YELLOWISH_GREEN,
        GBColorValues.SPANISH_VIRIDIAN,
        GBColorValues.GRANITA,
        GBColorValues.ZINNWALDITE_BROWN,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/MARMX.png">
        <p>MARMX color palette</p>
        </div>
        </div>
    """

    SLMEM = [
        GBColorValues.PORTAGE,
        GBColorValues.CIRCUMORBITAL_RING,
        GBColorValues.ORB_OF_DISCORD,
        GBColorValues.VIOLET_CARMINE,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/SLMEM.png">
        <p>SLMEM color palette</p>
        </div>
        </div>
    """

    DATN = [
        GBColorValues.BRILLIANT_SILVER,
        GBColorValues.ANCHOR_GREY,
        GBColorValues.YANKEES_BLUE,
        GBColorValues.VOID,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/DATN.png">
        <p>DATN color palette</p>
        </div>
        </div>
    """

    TSK = [
        GBColorValues.ANGELS_TRUMPET,
        GBColorValues.LAKE_THUN,
        GBColorValues.LUCARIO_BLUE,
        GBColorValues.INOFFENSIVE_BLUE,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/TSK.png">
        <p>TSK color palette</p>
        </div>
        </div>
    """

    PPR = [
        GBColorValues.FROSTBITE,
        GBColorValues.DAHLIA_PURPLE,
        GBColorValues.FANCY_FUCHSIA,
        GBColorValues.PURPLE_DREAMER,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/PPR.png">
        <p>PPR color palette</p>
        </div>
        </div>
    """

    CMYK = [
        GBColorValues.YELLOW,
        GBColorValues.PAINT_THE_SKY,
        GBColorValues.SIXTEEN_MILLION_PINK,
        GBColorValues.DARK_GREY,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/CMYK.png">
        <p>CMYK color palette</p>
        </div>
        </div>
    """

    VB85 = [
        GBColorValues.RED,
        GBColorValues.RED_PEGASUS,
        GBColorValues.UMBRAL_UMBER,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/VB85.png">
        <p>VB85 color palette</p>
        </div>
        </div>
    """

    AZC = [
        GBColorValues.SEA_GREEN,
        GBColorValues.TURTLE_WARRIOR,
        GBColorValues.MIZUKAZE_GREEN,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/AZC.png">
        <p>AZC color palette</p>
        </div>
        </div>
    """

    GELC = [
        GBColorValues.MANDARIN_PEEL,
        GBColorValues.CASSANDRAS_CURSE,
        GBColorValues.KYOTO_HOUSE,
        GBColorValues.BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GELC.png">
        <p>GELC color palette</p>
        </div>
        </div>
    """

    ROGA = [
        GBColorValues.WEEKEND_RETREAT,
        GBColorValues.ASTROTURF,
        GBColorValues.OLD_TREASURE_CHEST,
        GBColorValues.BLACK_POWDER,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/ROGA.png">
        <p>ROGA color palette</p>
        </div>
        </div>
    """

    KDITW = [
        GBColorValues.SUPER_BANANA,
        GBColorValues.CINAMON,
        GBColorValues.EARLY_SPRING_NIGHT,
        GBColorValues.BLACK_SLUG,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/KDITW.png">
        <p>KDITW color palette</p>
        </div>
        </div>
    """

    DIMWM = [
        GBColorValues.GLAZED_SUGAR,
        GBColorValues.JINZA_SAFFLOWER,
        GBColorValues.EMERALD_CLEAR_GREEN,
        GBColorValues.LIQUORICE_ROOT,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/DIMWM.png">
        <p>DIMWM color palette</p>
        </div>
        </div>
    """

    SPEZI = [
        GBColorValues.CANDLELIGHT,
        GBColorValues.CHEROKEE_DIGNITY,
        GBColorValues.EYE_POPPING_CHERRY,
        GBColorValues.DEEP_SPACE_RODEO,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/SPEZI.png">
        <p>SPEZI color palette</p>
        </div>
        </div>
    """

    FFS = [
        GBColorValues.SHORELAND,
        GBColorValues.FLAT_ALUMINIUM,
        GBColorValues.ADIRONDACK_BLUE,
        GBColorValues.PURE_MIDNIGHT,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/FFS.png">
        <p>FFS color palette</p>
        </div>
        </div>
    """

    BANANA = [
        GBColorValues.HEXOS_PALESUN,
        GBColorValues.FLIRTATIOUS,
        GBColorValues.SPRUCED_UP,
        GBColorValues.NOIR_MYSTIQUE,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/BANANA.png">
        <p>BANANA color palette</p>
        </div>
        </div>
    """

    HIPSTER = [
        GBColorValues.MILK,
        GBColorValues.SUGAR_HONEY_CASHEW,
        GBColorValues.GOLDEN_GLOVE,
        GBColorValues.CANNON_BLACK,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/HIPSTER.png">
        <p>HIPSTER color palette</p>
        </div>
        </div>
    """

    NC = [
        GBColorValues.BUTTER_CAKE,
        GBColorValues.ELECTRIC_SHEEP,
        GBColorValues.FIJI,
        GBColorValues.TRADITIONAL_ROYAL_BLUE,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/NC.png">
        <p>NC color palette</p>
        </div>
        </div>
    """

    GLMO = [
        GBColorValues.BLUSHING_CINNAMON,
        GBColorValues.RIDGE_VIEW,
        GBColorValues.PANGO_BLACK,
        GBColorValues.BLEACHED_CEDAR,
    ]
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorPalettes/GLMO.png">
        <p>GLMO color palette</p>
        </div>
        </div>
    """

    TPA = [
        GBColorValues.ORANGE_CHOCOLATE,
        GBColorValues.THIMBLEBERRY,
        GBColorValues.VIOLET_VIXEN,
        GBColorValues.GRIM_REAPER,
    ]
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

        >>> from gamebeye.gbcamcolors.gbcolorpalettes import GBColorPalettes
        >>> GBColorPalettes.BW.describe()
        ('BW', ['#FFFFFF', '#A8A8A8', '#545454', '#000000'])
        """
        return self.name, self.value

    def __str__(self) -> str:
        """
        Convert the enum member to a formatted string.

        :returns: the enum member as a string
        :rtype: str

        >>> from gamebeye.gbcamcolors.gbcolorpalettes import GBColorPalettes
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

        >>> from gamebeye.gbcamcolors.gbcolorpalettes import GBColorPalettes
        >>> GBColorPalettes.BW.rgb_colors
        [[255, 255, 255], [168, 168, 168], [84, 84, 84], [0, 0, 0]]
        """
        return [hex_to_rgb(color.value) for color in self.value]

    @property
    def hex_colors(self) -> List[str]:
        """
        Return the 4 color values of the enum in hexadecimal.

        :return: the 4 colors values in hexadecimal.
        :rtype: list[str]

        >>> from gamebeye.gbcamcolors.gbcolorpalettes import GBColorPalettes
        >>> GBColorPalettes.BW.hex_colors
        ['#FFFFFF', '#A8A8A8', '#545454', '#000000']
        """
        return [color.value for color in self.value]

    def distance_from(self, rgb_values: list[list[int]]):
        """
        Compute the deltaE_ciede2000 between the palette from a colors list.

        :param list rgb_values: (R, G, B) colors

        :return: the color distance
        :rtype: float
        """
        min_distance = []
        for rgb_value in rgb_values:
            distance = [(color, color.distance_from(rgb_value)) for color in self.value]
            min_distance.append(min(distance, key=lambda d: d[1]))
        return min_distance

    @classmethod
    def nearest_palette(cls, img_rgb_palette: list[list[int]]):
        """
        Find nearest color palette among the GBColorPalettes.

        :param list[list[int]] rgb_color_palette: a color palette

        :return: the nearest color palette from GBColorPalettes
        :rtype: GBColorPalettes
        """
        min_distances = inf
        for palette in cls:
            infos = palette.distance_from(img_rgb_palette)
            colors, _ = zip(*infos, strict=False)

            if len(set(colors)) != 4:
                pass

            for unique_color in set(colors):
                distance = min(
                    [distance for color, distance in infos if color == unique_color]
                )
                if min_distances > distance:
                    nearest_palette = palette
                    min_distances = distance
        return nearest_palette
