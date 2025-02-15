"""Define the GBColorValues enum."""

from enum import Enum, unique
from typing import List, Tuple

from skimage.color import deltaE_ciede2000

from gamebeye.gbcamcolors.color_helpers import hex_to_rgb, rgb_to_lab


# Class decorator @unique ensure each enum value is unique
@unique
class GBColorValues(Enum):
    """
    Pre-defined colorsbased upon Game Boy Camera known palettes.

    The GBColorValues class inherits from Enum class where the keys are
    the color names and the value a string whose value represent a color
    coded in hexadecimal basis.
    """

    WHITE = "#FFFFFF"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/WHITE.png">
        <p>White color</p>
        </div>
        </div>
    """

    UNIFORM_GREY = "#A8A8A8"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/UNIFORM_GREY.png">
        <p>Uniform grey color</p>
        </div>
        </div>
    """

    BRILLIANT_LIQUORICE = "#545454"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BRILLIANT_LIQUORICE.png">
        <p>Brilliant liquorice color</p>
        </div>
        </div>
    """

    BLACK = "#000000"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BLACK.png">
        <p>Black color</p>
        </div>
        </div>
    """

    GAMEBOY_CONTRAST = "#0F380F"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GAMEBOY_CONTRAST.png">
        <p>GameBoy constrast color</p>
        </div>
        </div>
    """

    GAMEBOY_LIGHT = "#9BBC0F"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GAMEBOY_LIGHT.png">
        <p>GameBoy light color</p>
        </div>
        </div>
    """

    LUMINESCENT_GREEN = "#77A112"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/LUMINESCENT_GREEN.png">
        <p>Luminescent green color</p>
        </div>
        </div>
    """

    GAMEBOY_SHADE = "#306230"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GAMEBOY_SHADE.png">
        <p>GameBoy shade color</p>
        </div>
        </div>
    """

    UMBRA = "#1F1F1F"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/UMBRA.png">
        <p>Umbra color</p>
        </div>
        </div>
    """

    DAPPLED_DAYDREAM = "#C4CFA1"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/DAPPLED_DAYDREAM.png">
        <p>Dappled daydream color</p>
        </div>
        </div>
    """

    CIDER_PEAR_GREEN = "#8B956D"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CIDER_PEAR_GREEN.png">
        <p>Cider pear green color</p>
        </div>
        </div>
    """

    KELP = "#4D533C"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/KELP.png">
        <p>Kelp color</p>
        </div>
        </div>
    """

    BLACK_STALLION = "#081820"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BLACK_STALLION.png">
        <p>Black stallion color</p>
        </div>
        </div>
    """

    LIGHT_GREEN_GLINT = "#E0F8D0"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/LIGHT_GREEN_GLINT.png">
        <p>Light green glint color</p>
        </div>
        </div>
    """

    LAUDABLE_LIME = "#88C070"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/LAUDABLE_LIME.png">
        <p>Laudable lime color</p>
        </div>
        </div>
    """

    PLANTAIN_GREEN = "#346856"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/PLANTAIN_GREEN.png">
        <p>Plantain green color</p>
        </div>
        </div>
    """

    BLUE_GREEN = "#0B7A6D"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BLUE_GREEN.png">
        <p>Blue green color</p>
        </div>
        </div>
    """

    CERAMIC_BLUE_TURQUOISE = "#16A596"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CERAMIC_BLUE_TURQUOISE.png">
        <p>Ceramic blue turquoise color</p>
        </div>
        </div>
    """

    EXQUISITE_TURQUOISE = "#19C7B3"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/EXQUISITE_TURQUOISE.png">
        <p>Exquisite turquoise color</p>
        </div>
        </div>
    """

    ICE_CLIMBER = "#1DDECE"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ICE_CLIMBER.png">
        <p>Ice climber color</p>
        </div>
        </div>
    """

    GREEN_WATERLOO = "#2B2B26"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GREEN_WATERLOO.png">
        <p>Green Waterloo color</p>
        </div>
        </div>
    """

    GIBRALTAR_GREY = "#706B66"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GIBRALTAR_GREY.png">
        <p>Gibraltar grey color</p>
        </div>
        </div>
    """

    LONDON_STONES = "#A89F94"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/LONDON_STONES.png">
        <p>London stone color</p>
        </div>
        </div>
    """

    NOBLE_CREAM = "#E0DBCD"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/NOBLE_CREAM.png">
        <p>Noble cream color</p>
        </div>
        </div>
    """

    VERT_PIERRE = "#4C625A"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/VERT_PIERRE.png">
        <p>Vert pierre color</p>
        </div>
        </div>
    """

    CHICON = "#DBF4B4"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CHICON.png">
        <p>Chicon color</p>
        </div>
        </div>
    """

    LODEN_FROST = "#7B9278"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/LODEN_FROST.png">
        <p>Loden frost color</p>
        </div>
        </div>
    """

    SEAWASHED_GLASS = "#ABC396"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SEAWASHED_GLASS.png">
        <p>Seawashed glass color</p>
        </div>
        </div>
    """

    BRACKEN_FERN = "#2E463D"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BRACKEN_FERN.png">
        <p>Bracken fern color</p>
        </div>
        </div>
    """

    ELWYNN_FOREST_OLIVE = "#7E8416"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ELWYNN_FOREST_OLIVE.png">
        <p>Elwynn forest olive color</p>
        </div>
        </div>
    """

    FRESH_HERBS = "#385D49"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FRESH_HERBS.png">
        <p>Fresh herbs color</p>
        </div>
        </div>
    """

    MOSSY_GREEN = "#577B46"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/MOSSY_GREEN.png">
        <p>Mossy green color</p>
        </div>
        </div>
    """

    COFFEE_ADDICTION = "#833100"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/COFFEE_ADDICTION.png">
        <p>Coffer addiction color</p>
        </div>
        </div>
    """

    DREAMY_SUNSET = "#FFAD63"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/DREAMY_SUNSET.png">
        <p>Dreamy sunset color</p>
        </div>
        </div>
    """

    DESERT_FLOWER = "#FF8F84"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/DESERT_FLOWER.png">
        <p>Desert flower color</p>
        </div>
        </div>
    """

    NEW_SLED = "#943A3A"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/NEW_SLED.png">
        <p>New sled color</p>
        </div>
        </div>
    """

    AGED_ANTICS = "#846B29"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/AGED_ANTICS.png">
        <p>Aged antics color</p>
        </div>
        </div>
    """

    CHESS_IVORY = "#FFE7C5"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CHESS_IVORY.png">
        <p>Chess ivory color</p>
        </div>
        </div>
    """

    DUSTY_CORAL = "#CE9C85"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/DUSTY_CORAL.png">
        <p>Dusty coral color</p>
        </div>
        </div>
    """

    COUNT_CHOCULA = "#5B3109"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/COUNT_CHOCULA.png">
        <p>Count chocula color</p>
        </div>
        </div>
    """

    AQUA_RAPIDS = "#65A49B"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/AQUA_RAPIDS.png">
        <p>Aqua rapids color</p>
        </div>
        </div>
    """

    BLUE = "#0000FE"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BLUE.png">
        <p>Blue color</p>
        </div>
        </div>
    """

    TWILIGHT = "#53528C"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/TWILIGHT.png">
        <p>Twilight color</p>
        </div>
        </div>
    """

    PERRYWINKLE = "#8B8CDE"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/PERRYWINKLE.png">
        <p>Perrywinkle color</p>
        </div>
        </div>
    """

    RAINY_GREY = "#A5A5A5"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/RAINY_GREY.png">
        <p>Rainy grey color</p>
        </div>
        </div>
    """

    CALAMANSI = "#FFFFA5"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CALAMANSI.png">
        <p>Calamansi color</p>
        </div>
        </div>
    """

    CAVERNOUS = "#525252"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CAVERNOUS.png">
        <p>Cavernous color</p>
        </div>
        </div>
    """

    CHERISHED_ONE = "#FE9494"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CHERISHED_ONE.png">
        <p>Cherished one color</p>
        </div>
        </div>
    """

    PERRYWINKLE_BLUE = "#9395FE"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/PERRYWINKLE_BLUE.png">
        <p>Periwinkle blue color</p>
        </div>
        </div>
    """

    YELLOW = "#FFFF00"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/YELLOW.png">
        <p>Yellow color</p>
        </div>
        </div>
    """

    RED = "#FF0000"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/RED.png">
        <p>Red color</p>
        </div>
        </div>
    """

    DRIED_MUSTARD = "#7D4900"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/DRIED_MUSTARD.png">
        <p>Dried mustard color</p>
        </div>
        </div>
    """

    HYPER_GREEN = "#51FF00"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/HYPER_GREEN.png">
        <p>Hyper green color</p>
        </div>
        </div>
    """

    ULTIMATE_ORANGE = "#FF4200"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ULTIMATE_ORANGE.png">
        <p>Ultimate orange color</p>
        </div>
        </div>
    """

    SPRING_FROST = "#7BFF30"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SPRING_FROST.png">
        <p>Spring frost color</p>
        </div>
        </div>
    """

    ROYAL_NAVY_BLUE = "#0163C6"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ROYAL_NAVY_BLUE.png">
        <p>Royal navy blue color</p>
        </div>
        </div>
    """

    FANFARE = "#008486"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FANFARE.png">
        <p>Fanfare color</p>
        </div>
        </div>
    """

    GOLDEN_YELLOW = "#FFDE00"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GOLDEN_YELLOW.png">
        <p>Golden yellow color</p>
        </div>
        </div>
    """

    FANTASY_CONSOLE_SKY = "#21AFF5"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FANTASY_CONSOLE_SKY.png">
        <p>Fantasy console sky color</p>
        </div>
        </div>
    """

    FREEZY_WIND = "#9EFBE3"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FREEZY_WIND.png">
        <p>Freezy wind color</p>
        </div>
        </div>
    """

    NUIT_BLANCHE = "#1E4793"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/NUIT_BLANCHE.png">
        <p>Nuit blanche color</p>
        </div>
        </div>
    """

    DARK_ECLIPSE = "#0E1E3D"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/DARK_ECLIPSE.png">
        <p>Dark eclipse color</p>
        </div>
        </div>
    """

    CREME_FRAICHE = "#EBEEE7"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CREME_FRAICHE.png">
        <p>Crème fraîche color</p>
        </div>
        </div>
    """

    KOSHER_KHAHI = "#868779"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/KOSHER_KHAHI.png">
        <p>Kosher khaki color</p>
        </div>
        </div>
    """

    RED_STOP = "#FA2B25"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/RED_STOP.png">
        <p>Red stop color</p>
        </div>
        </div>
    """

    VELCET_BLACK = "#2A201E"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/VELCET_BLACK.png">
        <p>Velvet black color</p>
        </div>
        </div>
    """

    ACAPULCO_DIVE = "#6F9EDF"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ACAPULCO_DIVE.png">
        <p>Acapulco of smoke color</p>
        </div>
        </div>
    """

    SEA_OF_GALILEE = "#42678E"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SEA_OF_GALILEE.png">
        <p>Sea of Galilee color</p>
        </div>
        </div>
    """

    WHISPER_OF_SMOKE = "#CECECE"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/WHISPER_OF_SMOKE.png">
        <p>Whisper of smoke color</p>
        </div>
        </div>
    """

    BLACK_BOX = "#102533"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BLACK_BOX.png">
        <p>Black box color</p>
        </div>
        </div>
    """

    LAZY_LIZARD = "#A0A840"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/LAZY_LIZARD.png">
        <p>Lazy lizard color</p>
        </div>
        </div>
    """

    PESTO_DI_RUCOLA = "#708028"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/PESTO_DI_RUCOLA.png">
        <p>Pesto di rucola color</p>
        </div>
        </div>
    """

    SALSA_VERDE = "#D0D058"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SALSA_VERDE.png">
        <p>Salsa verde color</p>
        </div>
        </div>
    """

    GODZILLA = "#405010"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GODZILLA.png">
        <p>Godzilla color</p>
        </div>
        </div>
    """

    WAX_FLOWER = "#EDB4A1"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/WAX_FLOWER.png">
        <p>Wax flower color</p>
        </div>
        </div>
    """

    MELON_TWIST = "#A96868"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/MELON_TWIST.png">
        <p>Melon twitst color</p>
        </div>
        </div>
    """

    SCINTILLATING_VIOLET = "#764462"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SCINTILLATING_VIOLET.png">
        <p>Scintillating violet color</p>
        </div>
        </div>
    """

    MOON_WHITE = "#EAF5FA"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/MOON_WHITE.png">
        <p>Moon white color</p>
        </div>
        </div>
    """

    BLUE_JEANS = "#5FB1F5"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BLUE_JEANS.png">
        <p>Blue jeans color</p>
        </div>
        </div>
    """

    SMOOCH_ROUGE = "#D23C4E"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SMOOCH_ROUGE.png">
        <p>Smooch rouge color</p>
        </div>
        </div>
    """

    DARK_MAHOGANY = "#4C1C2D"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/DARK_MAHOGANY.png">
        <p>Dark mahogany color</p>
        </div>
        </div>
    """

    MOONGLOW = "#F8E3C4"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/MOONGLOW.png">
        <p>Moonglow color</p>
        </div>
        </div>
    """

    ROYAL_FUCHSIA = "#CC3495"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ROYAL_FUCHSIA.png">
        <p>Royal fuchsia color</p>
        </div>
        </div>
    """

    FUCHSIA_NEBULA = "#6B1FB1"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FUCHSIA_NEBULA.png">
        <p>Fuchsia nebula color</p>
        </div>
        </div>
    """

    COSMIC_VOID = "#0B0630"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/COSMIC_VOID.png">
        <p>Cosmic void color</p>
        </div>
        </div>
    """

    CHESTNUT_SHELL = "#B5FF32"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CHESTNUT_SHELL.png">
        <p>Chestnut shell color</p>
        </div>
        </div>
    """

    PEEVISH_RED = "#FF2261"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/PEEVISH_RED.png">
        <p>Peevish red color</p>
        </div>
        </div>
    """

    NIGHT_BROWN = "#462917"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/NIGHT_BROWN.png">
        <p>Night brown color</p>
        </div>
        </div>
    """

    BATS_CLOAK = "#1D1414"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BATS_CLOAK.png">
        <p>Bats cloak color</p>
        </div>
        </div>
    """

    POLO_PONY = "#CF9255"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/POLO_PONY.png">
        <p>Polo pony color</p>
        </div>
        </div>
    """

    OK_CORRAL = "#CF7163"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/OK_CORRAL.png">
        <p>OK corral color</p>
        </div>
        </div>
    """

    CERISE = "#B01553"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CERISE.png">
        <p>Cerise color</p>
        </div>
        </div>
    """

    DARK_SIENNA = "#3F1711"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/DARK_SIENNA.png">
        <p>Dark sienna color</p>
        </div>
        </div>
    """

    PILA_YELLOW = "#FFFF55"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/PILA_YELLOW.png">
        <p>Pîlâ yellow color</p>
        </div>
        </div>
    """

    FLUORESCENT_RED = "#FF5555"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FLUORESCENT_RED.png">
        <p>Fluorescent red color</p>
        </div>
        </div>
    """

    RED_LEEVER = "#881400"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/RED_LEEVER.png">
        <p>Red leever color</p>
        </div>
        </div>
    """

    VIVID_LIME_GREEN = "#A1D909"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/VIVID_LIME_GREEN.png">
        <p>Vivid lime green color</p>
        </div>
        </div>
    """

    FOREST_EMPRESS = "#467818"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FOREST_EMPRESS.png">
        <p>Forest empress color</p>
        </div>
        </div>
    """

    MYRTLE = "#27421F"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/MYRTLE.png">
        <p>Myrtle color</p>
        </div>
        </div>
    """

    TINTED_ICE = "#CEF7F7"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/TINTED_ICE.png">
        <p>Tinted ice color</p>
        </div>
        </div>
    """

    BLAZE = "#F78E50"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BLAZE.png">
        <p>Blaze color</p>
        </div>
        </div>
    """

    CACODEMON_RED = "#9E0000"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CACODEMON_RED.png">
        <p>Cacodemon red color</p>
        </div>
        </div>
    """

    DWARF_FORTRESS = "#1E0000"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/DWARF_FORTRESS.png">
        <p>Dwarf fortress color</p>
        </div>
        </div>
    """

    PINK_MACAROON = "#E6AEC4"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/PINK_MACAROON.png">
        <p>Pink macaroon color</p>
        </div>
        </div>
    """

    CARMINE_ROSE = "#E65790"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CARMINE_ROSE.png">
        <p>Carmine rose color</p>
        </div>
        </div>
    """

    MADRILENO_MAROON = "#8F0039"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/MADRILENO_MAROON.png">
        <p>Madrileno maroon color</p>
        </div>
        </div>
    """

    ILVAITE_BLACK = "#380016"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ILVAITE_BLACK.png">
        <p>Ilvaite black color</p>
        </div>
        </div>
    """

    HINT_OF_YELLOW = "#FCF1CD"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/HINT_OF_YELLOW.png">
        <p>Hint of yellow color</p>
        </div>
        </div>
    """

    WICKERWORK = "#C09E7D"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/WICKERWORK.png">
        <p>Wickerork color</p>
        </div>
        </div>
    """

    MOOSE_FUR = "#725441"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/MOOSE_FUR.png">
        <p>Moose fur color</p>
        </div>
        </div>
    """

    FLAXSEED = "#F7E7C6"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FLAXSEED.png">
        <p>Flaxseed color</p>
        </div>
        </div>
    """

    GOLDEN_NUGGET = "#D68E49"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GOLDEN_NUGGET.png">
        <p>Golden nugget color</p>
        </div>
        </div>
    """

    JAIPUR = "#A63725"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/JAIPUR.png">
        <p>Jaipur color</p>
        </div>
        </div>
    """

    POWERFUL_VIOLET = "#331E50"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/POWERFUL_VIOLET.png">
        <p>Powerful violet color</p>
        </div>
        </div>
    """

    CREME = "#FFFFB5"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CREME.png">
        <p>Crème color</p>
        </div>
        </div>
    """

    GARDEN_STROLL = "#7BC67B"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GARDEN_STROLL.png">
        <p>Garden stroll color</p>
        </div>
        </div>
    """

    MAKRUT_LIME = "#6B8C42"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/MAKRUT_LIME.png">
        <p>Makrut lime color</p>
        </div>
        </div>
    """

    KURO_BROWN = "#5A3921"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/KURO_BROWN.png">
        <p>Kuro brown color</p>
        </div>
        </div>
    """

    ELECTRIC_SHEEP = "#55FFFF"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ELECTRIC_SHEEP.png">
        <p>Electric sheep color</p>
        </div>
        </div>
    """

    ULTIMATE_PINK = "#FF55FF"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ULTIMATE_PINK.png">
        <p>Ultimate pink color</p>
        </div>
        </div>
    """

    YELLOWISH_GREEN = "#AEDF1E"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/YELLOWISH_GREEN.png">
        <p>Yellowish green color</p>
        </div>
        </div>
    """

    SPANISH_VIRIDIAN = "#047E60"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SPANISH_VIRIDIAN.png">
        <p>Spanish viridian color</p>
        </div>
        </div>
    """

    GRANITA = "#B62558"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GRANITA.png">
        <p>Granita color</p>
        </div>
        </div>
    """

    ZINNWALDITE_BROWN = "#2C1700"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ZINNWALDITE_BROWN.png">
        <p>Zinnwaldite brown color</p>
        </div>
        </div>
    """

    PORTAGE = "#869AD9"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/PORTAGE.png">
        <p>Portage color</p>
        </div>
        </div>
    """

    CIRCUMORBITAL_RING = "#6D53BD"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CIRCUMORBITAL_RING.png">
        <p>Circumorbital ring color</p>
        </div>
        </div>
    """

    VIOLET_CARMINE = "#4F133F"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/VIOLET_CARMINE.png">
        <p>Violet carmine color</p>
        </div>
        </div>
    """

    ORB_OF_DISCORD = "#6F2096"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ORB_OF_DISCORD.png">
        <p>Orb of discord color</p>
        </div>
        </div>
    """

    RED_PEGASUS = "#DB0000"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/RED_PEGASUS.png">
        <p>Red pegasus color</p>
        </div>
        </div>
    """

    UMBRAL_UMBER = "#520000"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/UMBRAL_UMBER.png">
        <p>Umbral umber color</p>
        </div>
        </div>
    """

    BRILLIANT_SILVER = "#A9B0B3"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BRILLIANT_SILVER.png">
        <p>Brilliant silver color</p>
        </div>
        </div>
    """

    ANCHOR_GREY = "#586164"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ANCHOR_GREY.png">
        <p>Anchor grey color</p>
        </div>
        </div>
    """

    YANKEES_BLUE = "#20293F"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/YANKEES_BLUE.png">
        <p>Yankees blue color</p>
        </div>
        </div>
    """

    VOID = "#030C22"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/VOID.png">
        <p>Void color</p>
        </div>
        </div>
    """

    ANGELS_TRUMPET = "#F5DB37"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ANGELS_TRUMPET.png">
        <p>Angel's trumpet color</p>
        </div>
        </div>
    """

    LAKE_THUN = "#37CAE5"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/LAKE_THUN.png">
        <p>Lake thun color</p>
        </div>
        </div>
    """

    LUCARIO_BLUE = "#0F86B6"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/LUCARIO_BLUE.png">
        <p>Lucario blue color</p>
        </div>
        </div>
    """

    INOFFENSIVE_BLUE = "#123F77"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/INOFFENSIVE_BLUE.png">
        <p>Inoffesive blue color</p>
        </div>
        </div>
    """

    FROSTBITE = "#ADFFFC"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FROSTBITE.png">
        <p>Frostbite color</p>
        </div>
        </div>
    """

    DAHLIA_PURPLE = "#8570B2"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/DAHLIA_PURPLE.png">
        <p>Dahlia purple color</p>
        </div>
        </div>
    """

    FANCY_FUCHSIA = "#FF0084"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FANCY_FUCHSIA.png">
        <p>Fancy fuchsia color</p>
        </div>
        </div>
    """

    PURPLE_DREAMER = "#68006A"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/PURPLE_DREAMER.png">
        <p>Purple dreamer color</p>
        </div>
        </div>
    """

    PAINT_THE_SKY = "#0BE8FD"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/PAINT_THE_SKY.png">
        <p>Paint the sky color</p>
        </div>
        </div>
    """

    SIXTEEN_MILLION_PINK = "#FB00FA"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SIXTEEN_MILLION_PINK.png">
        <p>Sixteen million pink color</p>
        </div>
        </div>
    """

    DARK_GREY = "#373737"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/DARK_GREY.png">
        <p>Dark grey color</p>
        </div>
        </div>
    """

    SEA_GREEN = "#47FF99"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SEA_GREEN.png">
        <p>Sea green color</p>
        </div>
        </div>
    """

    TURTLE_WARRIOR = "#32B66D"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/TURTLE_WARRIOR.png">
        <p>Turtle warrior color</p>
        </div>
        </div>
    """

    MIZUKAZE_GREEN = "#124127"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/MIZUKAZE_GREEN.png">
        <p>Mizukaze green color</p>
        </div>
        </div>
    """

    MANDARIN_PEEL = "#FF9C00"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/MANDARIN_PEEL.png">
        <p>Mandarin peel color</p>
        </div>
        </div>
    """

    CASSANDRAS_CURSE = "#C27600"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CASSANDRAS_CURSE.png">
        <p>Cassandra's curse color</p>
        </div>
        </div>
    """

    KYOTO_HOUSE = "#4F3000"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/KYOTO_HOUSE.png">
        <p>Kyoto house color</p>
        </div>
        </div>
    """

    WEEKEND_RETREAT = "#EBC4AB"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/WEEKEND_RETREAT.png">
        <p>Weekend retreat color</p>
        </div>
        </div>
    """

    ASTROTURF = "#649A57"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ASTROTURF.png">
        <p>Astroturf color</p>
        </div>
        </div>
    """

    OLD_TREASURE_CHEST = "#574431"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/OLD_TREASURE_CHEST.png">
        <p>Old treasure chest color</p>
        </div>
        </div>
    """

    BLACK_POWDER = "#323727"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BLACK_POWDER.png">
        <p>Black powder color</p>
        </div>
        </div>
    """

    EARLY_SPRING_NIGHT = "#3C3CA9"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/EARLY_SPRING_NIGHT.png">
        <p>Early spring night color</p>
        </div>
        </div>
    """

    SUPER_BANANA = "#FFFE6E"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SUPER_BANANA.png">
        <p>Super banana color</p>
        </div>
        </div>
    """

    CINAMON = "#D5690F"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CINAMON.png">
        <p>Cinamon color</p>
        </div>
        </div>
    """

    BLACK_SLUG = "#2C2410"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BLACK_SLUG.png">
        <p>Black slug color</p>
        </div>
        </div>
    """

    GLAZED_SUGAR = "#FFDBCB"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GLAZED_SUGAR.png">
        <p>Glazed sugar color</p>
        </div>
        </div>
    """

    JINZA_SAFFLOWER = "#F27D7A"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/JINZA_SAFFLOWER.png">
        <p>Jinza safflower color</p>
        </div>
        </div>
    """

    EMERALD_CLEAR_GREEN = "#558429"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/EMERALD_CLEAR_GREEN.png">
        <p>Emerald clear green color</p>
        </div>
        </div>
    """

    LIQUORICE_ROOT = "#222903"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/LIQUORICE_ROOT.png">
        <p>Liquorice root color</p>
        </div>
        </div>
    """

    CANDLELIGHT = "#FEDA1B"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CANDLELIGHT.png">
        <p>Candlelight color</p>
        </div>
        </div>
    """

    CHEROKEE_DIGNITY = "#DF7925"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CHEROKEE_DIGNITY.png">
        <p>Cherokee dignity color</p>
        </div>
        </div>
    """

    EYE_POPPING_CHERRY = "#B60077"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/EYE_POPPING_CHERRY.png">
        <p>Eye popping cherry color</p>
        </div>
        </div>
    """

    DEEP_SPACE_RODEO = "#382977"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/DEEP_SPACE_RODEO.png">
        <p>Deep space rodeo color</p>
        </div>
        </div>
    """

    SHORELAND = "#E9D9CC"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SHORELAND.png">
        <p>Shoreland color</p>
        </div>
        </div>
    """

    FLAT_ALUMINIUM = "#C5C5CE"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FLAT_ALUMINIUM.png">
        <p>Flat aluminium color</p>
        </div>
        </div>
    """

    ADIRONDACK_BLUE = "#75868F"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ADIRONDACK_BLUE.png">
        <p>Adirondack blue color</p>
        </div>
        </div>
    """

    PURE_MIDNIGHT = "#171F62"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/PURE_MIDNIGHT.png">
        <p>Pure pidnight color</p>
        </div>
        </div>
    """

    HEXOS_PALESUN = "#FDFE0A"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/HEXOS_PALESUN.png">
        <p>Hexos palesun color</p>
        </div>
        </div>
    """

    FLIRTATIOUS = "#FED638"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FLIRTATIOUS.png">
        <p>Flirtatious color</p>
        </div>
        </div>
    """

    SPRUCED_UP = "#977B25"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SPRUCED_UP.png">
        <p>Spruced up color</p>
        </div>
        </div>
    """

    NOIR_MYSTIQUE = "#221A09"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/NOIR_MYSTIQUE.png">
        <p>Noir mystique color</p>
        </div>
        </div>
    """

    MILK = "#FDFEF5"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/MILK.png">
        <p>Milk color</p>
        </div>
        </div>
    """

    SUGAR_HONEY_CASHEW = "#DEA963"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/SUGAR_HONEY_CASHEW.png">
        <p>Sugar honey cashew color</p>
        </div>
        </div>
    """

    GOLDEN_GLOVE = "#9E754F"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GOLDEN_GLOVE.png">
        <p>Golden glove color</p>
        </div>
        </div>
    """

    CANNON_BLACK = "#241606"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/CANNON_BLACK.png">
        <p>Cannon black color</p>
        </div>
        </div>
    """

    BUTTER_CAKE = "#FCFE54"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BUTTER_CAKE.png">
        <p>Butter cake color</p>
        </div>
        </div>
    """

    FIJI = "#04AAAC"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/FIJI.png">
        <p>Fiji color</p>
        </div>
        </div>
    """

    TRADITIONAL_ROYAL_BLUE = "#0402AC"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/TRADITIONAL_ROYAL_BLUE.png">
        <p>Traditional royal blue color</p>
        </div>
        </div>
    """

    BLUSHING_CINNAMON = "#FFBF98"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BLUSHING_CINNAMON.png">
        <p>Blushing cinnamon color</p>
        </div>
        </div>
    """

    RIDGE_VIEW = "#A1A8B8"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/RIDGE_VIEW.png">
        <p>Ridge view color</p>
        </div>
        </div>
    """

    PANGO_BLACK = "#514F6C"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/PANGO_BLACK.png">
        <p>Pango black color</p>
        </div>
        </div>
    """

    BLEACHED_CEDAR = "#2F1C35"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/BLEACHED_CEDAR.png">
        <p>Bleached cedar color</p>
        </div>
        </div>
    """

    ORANGE_CHOCOLATE = "#F3C677"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/ORANGE_CHOCOLATE.png">
        <p>orange chocolate color</p>
        </div>
        </div>
    """

    THIMBLEBERRY = "#E64A4E"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/THIMBLEBERRY.png">
        <p>Thimbleberry color</p>
        </div>
        </div>
    """

    VIOLET_VIXEN = "#912978"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/VIOLET_VIXEN.png">
        <p>Violet vixen color</p>
        </div>
        </div>
    """

    GRIM_REAPER = "#0C0A3E"
    """
    .. raw:: html

        <div class="centered-grid">
        <div class="grid-item">
        <img src="../_static/colorValues/GRIM_REAPER.png">
        <p>Grim reaper color</p>
        </div>
        </div>
    """

    def describe(self) -> Tuple[str, list]:
        """
        Describe itself. Return as a tuple the color palette name and colors.

        :returns: a 2-values tuple containing the color name and its values
        :rtype: str, list

        >>> from gamebeye.gbcamcolors.gbcolorvalues import GBColorValues
        >>> GBcolorValues.ROYAL_NAVY_BLUE.describe()
        ('ROYAL_NAVY_BLUE', '#0163C6')
        """
        return self.name, self.value

    def __str__(self) -> str:
        """
        Convert the enum member to a formatted string.

        :returns: the enum member as a string
        :rtype: str

        >>> from gamebeye.gbcamcolors.gbcolorvalues import GBColorValues
        >>> str(GBcolorValues.ROYAL_NAVY_BLUE)
        "ROYAL_NAVY_BLUE : '#0163C6'"
        """
        return "{} : {}".format(self.name, str(self.value))

    @property
    def rgb_colors(self) -> List[int]:
        """
        Return the the color value of the enum in RGB space.

        :return: the color values in the RGB space
        :rtype: list[int]

        >>> from gamebeye.gbcamcolors.gbcolorvalues import GBColorValues
        >>> GBColorValues.ROYAL_NAVY_BLUE
        [1, 99, 198]
        """
        return hex_to_rgb(self.value)

    def distance_from(self, rgb_value: list[int]):
        """
        Compute the deltaE_ciede2000 between the current color from a (R, G, B) array.

        :param list rgb_value: (R, G, B) list of reference

        :return: the color distance
        :rtype: float
        """
        ref_lab_color = rgb_to_lab(rgb_value)
        lab_color = rgb_to_lab(self.rgb_colors)
        return deltaE_ciede2000(ref_lab_color, lab_color)

    @classmethod
    def nearest_color(cls, rgb_value):
        """
        Find nearest color value among the GBColorValues.

        :param list rgb_val: (R, G, B) list to convert

        :return: the nearest color from the GBColorValues
        :rtype: GBColorValue

        >>> from gamebeye.gbcamcolors.gbcolorvalues import GBColorValues
        >>> GBColorValues.nearest_color([2, 100, 198])
        <GBColorValues.ROYAL_NAVY_BLUE: '#0163C6'>
        """
        distance = [(color, color.distance_from(rgb_value)) for color in cls]
        return min(distance, key=lambda d: d[1])[0]
