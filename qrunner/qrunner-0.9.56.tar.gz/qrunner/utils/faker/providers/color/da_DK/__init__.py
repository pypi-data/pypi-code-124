from collections import OrderedDict

from .. import Provider as ColorProvider

localized = True


class Provider(ColorProvider):
    """
    Implement color provider for ``da_DK`` locale. Source: https://tools.hopetrip.com.hk/web/colorcode/index-da-1.html
    """

    all_colors = OrderedDict(
        (
            ("Baker-Miller lyserød", "#FF91AF"),
            ("Lysegul (Crayola)", "#FFAA1D"),
            ("Rav", "#FFBF00"),
            ("Rav (SAE / ECE)", "#FF7E00"),
            ("Atomisk mandarin", "#FF9966"),
            ("Bisque", "#FFE4C4"),
            ("Candy apple rød", "#FF0800"),
            ("Babypudder", "#FEFEFA"),
            ("Coquelicot", "#FF3800"),
            ("Blancheret mandel", "#FFEBCD"),
            ("Strålende rose", "#FF55A3"),
            ("Bittersød", "#FE6F5E"),
            ("Cadmium gul", "#FFF600"),
            ("Kanariefarvet gul", "#FFEF00"),
            ("Nellike lyserød", "#FFA6C9"),
            ("Kanariefugl", "#FFFF99"),
            ("Kirsebærblomst lyserød", "#FFB7C5"),
            ("Koral", "#FF7F50"),
            ("Kinesisk gul", "#FFB200"),
            ("Krom gul", "#FFA700"),
            ("Cybergult", "#FFD300"),
            ("Dyb lyserød", "#FF1493"),
            ("Aureolin", "#FDEE00"),
            ("Bananmani", "#FAE7B5"),
            ("Candyfloss", "#FFBCD9"),
            ("Fløde", "#FFFDD0"),
            ("Kosmisk latte", "#FFF8E7"),
            ("Cornsilk", "#FFF8DC"),
            ("Mørk orange", "#FF8C00"),
            ("Dyb safran", "#FF9933"),
            ("Blomsterhvid", "#FFFAF0"),
            ("Brændende rose", "#FF5470"),
            ("Fransk lyserød", "#FD6C9E"),
            ("Fuchsia", "#FF00FF"),
            ("Fransk fuchsia", "#FD3F92"),
            ("Antik hvid", "#FAEBD7"),
            ("Blond", "#FAF0BE"),
            ("Brink pink", "#FB607F"),
            ("Abrikos", "#FBCEB1"),
            ("Majs", "#FBEC5D"),
            ("Koralrosa", "#F88379"),
            ("Kultiveret", "#F5F5F5"),
            ("Cameo pink", "#EFBBCC"),
            ("Champagne", "#F7E7CE"),
            ("Flickr Pink", "#FB0081"),
            ("Dyb champagne", "#FAD6A5"),
            ("Congo pink", "#F88379"),
            ("Champagne lyserød", "#F1DDCF"),
            ("Baby lyserød", "#F4C2C2"),
            ("Beige", "#F5F5DC"),
            ("Fransk rose", "#F64A8A"),
            ("Cyclamen", "#F56FA1"),
            ("Azure (X11 / webfarve)", "#F0FFFF"),
            ("Alice blå", "#F0F8FF"),
            ("Mode fuchsia", "#F400A1"),
            ("Mandel", "#EFDECD"),
            ("Æggeskal", "#F0EAD6"),
            ("Hollandsk hvid", "#EFDFBB"),
            ("Amaranth pink", "#F19CBB"),
            ("Buff", "#F0DC82"),
            ("Ørkensand", "#EDC9AF"),
            ("Cadmium orange", "#ED872D"),
            ("Arylid gul", "#E9D66B"),
            ("Brandopal", "#E95C4B"),
            ("Alabaster", "#EDEAE0"),
            ("Gulerod orange", "#ED9121"),
            ("Hør", "#EEDC82"),
            ("Brændt sienna", "#E97451"),
            ("Cadmium rød", "#E30022"),
            ("Mørk laks", "#E9967A"),
            ("Flamme", "#E25822"),
            ("Knogle", "#E3DAC9"),
            ("Amaranth", "#E52B50"),
            ("Forfrysninger", "#E936A7"),
            ("Fulvous", "#E48400"),
            ("Charm lyserød", "#E68FAC"),
            ("Candy pink", "#E4717A"),
            ("Fawn", "#E5AA70"),
            ("Citrin", "#E4D00A"),
            ("Cinnabar", "#E34234"),
            ("CG rød", "#E03C31"),
            ("Crimson", "#DC143C"),
            ("Jorden gul", "#E1A95F"),
            ("Kina lyserød", "#DE6FA1"),
            ("Rødme", "#DE5D83"),
            ("Chartreuse (traditionel)", "#DFFF00"),
            ("Burlywood", "#DEB887"),
            ("Cerise", "#DE3163"),
            ("Barbie Pink", "#DA1884"),
            ("Fandango pink", "#DE5285"),
            ("Dyb cerise", "#DA3287"),
            ("Chokolade (web)", "#D2691E"),
            ("Lys lilla", "#D891EF"),
            ("Dogwood rose", "#D71868"),
            ("Carmine (M&P)", "#D70040"),
            ("Kobber (Crayola)", "#DA8A67"),
            ("Amaranth rød", "#D3212D"),
            ("Fransk mauve", "#D473D4"),
            ("Kakaobrun", "#D2691E"),
            ("Arktisk kalk", "#D0FF14"),
            ("Brandbil rød", "#CE2029"),
            ("Cedertræskiste", "#C95A49"),
            ("Kamel", "#C19A6B"),
            ("Brændt orange", "#CC5500"),
            ("Fransk hindbær", "#C72C48"),
            ("Aero blå", "#C9FFE5"),
            ("Bitter citron", "#CAE00D"),
            ("Kanel Satin", "#CD607E"),
            ("Lys rødbrun", "#C32148"),
            ("Ørken", "#C19A6B"),
            ("Fuchsia lilla", "#CC397B"),
            ("Engelsk vermillion", "#CC474B"),
            ("Antik messing", "#CD9575"),
            ("Bronze", "#CD7F32"),
            ("Elektrisk kalk", "#CCFF00"),
            ("Fuchsia steg", "#C74375"),
            ("Murstensrød", "#CB4154"),
            ("Legeret orange", "#C46210"),
            ("Kobberrød", "#CB6D51"),
            ("Kardinal", "#C41E3A"),
            ("Bitter kalk", "#BFFF00"),
            ("Engelsk lavendel", "#B48395"),
            ("Celeste", "#B2FFFF"),
            ("Mørk kaki", "#BDB76B"),
            ("Brak", "#C19A6B"),
            ("Fuchsia (Crayola)", "#C154C1"),
            ("Ecru", "#C2B280"),
            ("Bittersød glimmer", "#BF4F51"),
            ("Lyseblå", "#BCD4E6"),
            ("Sorte skygger", "#BFAFB2"),
            ("Elektrisk lilla", "#BF00FF"),
            ("Byzantinsk", "#BD33A4"),
            ("Columbia Blue", "#B9D9EB"),
            ("Mørk guldrør", "#B8860B"),
            ("Kobber", "#B87333"),
            ("Dyb kastanje", "#B94E48"),
            ("Carnelian", "#B31B1B"),
            ("Afrikansk violet", "#B284BE"),
            ("Fandango", "#B53389"),
            ("Askegrå", "#B2BEB5"),
            ("Kobber øre", "#AD6F69"),
            ("Auburn", "#A52A2A"),
            ("Celadon", "#ACE1AF"),
            ("Syregrøn", "#B0BF1A"),
            ("Amaranth lilla", "#AB274F"),
            ("brunt sukker", "#AF6E4D"),
            ("Blå klokke", "#A2A2D0"),
            ("Firebrick", "#B22222"),
            ("Kinesisk rød", "#AA381E"),
            ("Engelsk rød", "#AB4B52"),
            ("Café au lait", "#A67B5B"),
            ("Kadetblå (Crayola)", "#A9B2C3"),
            ("Snestorm blå", "#ACE5EE"),
            ("Kina steg", "#A8516E"),
            ("Fransk beige", "#A67B5B"),
            ("Blast-off bronze", "#A57164"),
            ("Flirt", "#A2006D"),
            ("Android grøn", "#A4C639"),
            ("Cambridge blå", "#A3C1AD"),
            ("Babyblå øjne", "#A1CAF1"),
            ("Amaranth (M&P)", "#9F2B68"),
            ("Cinereous", "#98817B"),
            ("Kedelig", "#967117"),
            ("Citron", "#9FA91F"),
            ("Bæver", "#9F8170"),
            ("Crimson (UA)", "#9E1B32"),
            ("Kadetgrå", "#91A3B0"),
            ("Brunbrun", "#A17A74"),
            ("Stor dukkert o’ruby", "#9C2542"),
            ("Fransk kalk", "#9EFD38"),
            ("Ametyst", "#9966CC"),
            ("Kobber rose", "#996666"),
            ("Eton blå", "#96C8A2"),
            ("Carmine", "#960018"),
            ("Bistre brun", "#967117"),
            ("Mørk orkidé", "#9932CC"),
            ("Mørk violet", "#9400D3"),
            ("Artiskok", "#8F9779"),
            ("kastanje", "#954535"),
            ("Antik fuchsia", "#915C83"),
            ("Mørk havgrøn", "#8FBC8F"),
            ("Baby Blå", "#89CFF0"),
            ("Cool grå", "#8C92AC"),
            ("Mørk magenta", "#8B008B"),
            ("Cordovan", "#893F45"),
            ("Mørk himmelblå", "#8CBED6"),
            ("Æblegrøn", "#8DB600"),
            ("Brun", "#88540B"),
            ("Asparges", "#87A96B"),
            ("Brandy", "#87413F"),
            ("Elektrisk violet", "#8F00FF"),
            ("Blåviolet", "#8A2BE2"),
            ("Brændt umber", "#8A3324"),
            ("Mørkerød", "#8B0000"),
            ("Fransk violet", "#8806CE"),
            ("Fransk lilla", "#86608E"),
            ("Fuzzy Wuzzy", "#87421F"),
            ("Antik rubin", "#841B2D"),
            ("Slagskib grå", "#848482"),
            ("Kinesisk violet", "#856088"),
            ("Aero", "#7CB9E8"),
            ("Coyote brun", "#81613C"),
            ("Byzantium", "#702963"),
            ("Chokolade (traditionel)", "#7B3F00"),
            ("Akvamarin", "#7FFFD4"),
            ("Fransk bistre", "#856D4D"),
            ("Bourgogne", "#800020"),
            ("Dyb taupe", "#7E5E60"),
            ("Falu rød", "#801818"),
            ("Laderød", "#7C0A02"),
            ("Claret", "#7F1734"),
            ("Fransk himmelblå", "#77B5FE"),
            ("Elektrisk blå", "#7DF9FF"),
            ("Bole", "#79443B"),
            ("Kaffe", "#6F4E37"),
            ("Luftoverlegenhed blå", "#72A0C1"),
            ("Blåviolet (Crayola)", "#7366BD"),
            ("Knoppegrøn", "#7BB661"),
            ("Catawba", "#703642"),
            ("Kornblomst blå", "#6495ED"),
            ("Elektrisk indigo", "#6F00FF"),
            ("Eminence", "#6C3082"),
            ("Blågrå", "#6699CC"),
            ("Mark trist", "#6C541E"),
            ("Blodrød", "#660000"),
            ("Cerulean frost", "#6D9BC3"),
            ("Dim grå", "#696969"),
            ("Lyse-grøn", "#66FF00"),
            ("Kadetblå", "#5F9EA0"),
            ("Mørkeblå-grå", "#666699"),
            ("Cyber ​​drue", "#58427C"),
            ("Caput mortuum", "#592720"),
            ("Aubergine", "#614051"),
            ("Mørkt byzantium", "#5D3954"),
            ("Antik bronze", "#665D1E"),
            ("Skovgrøn (Crayola)", "#5FA777"),
            ("Mørkebrun", "#654321"),
            ("Avocado", "#568203"),
            ("Blå bukser", "#5DADEC"),
            ("Mørk elektrisk blå", "#536878"),
            ("Mørk lever (heste)", "#543D37"),
            ("Café noir", "#4B3621"),
            ("Smaragd", "#50C878"),
            ("Carolina blå", "#56A0D3"),
            ("Kadet", "#536872"),
            ("Mørk lever", "#534B4F"),
            ("Engelsk violet", "#563C5C"),
            ("Mørk olivengrøn", "#556B2F"),
            ("Sort koral", "#54626F"),
            ("Blå derfra", "#5072A7"),
            ("Ibenholt", "#555D50"),
            ("Davy er grå", "#555555"),
            ("Militærgrøn", "#4B5320"),
            ("Feldgrau", "#4D5D53"),
            ("Fern grøn", "#4F7942"),
            ("Mørk mosgrøn", "#4A5D23"),
            ("Mørk lava", "#483C32"),
            ("Blåviolet (farvehjul)", "#4D1A7F"),
            ("Deep Space Sparkle", "#4A646C"),
            ("Mørk skiferblå", "#483D8B"),
            ("Sort bønne", "#3D0C02"),
            ("Bistre", "#3D2B1F"),
            ("Sort oliven", "#3B3C36"),
            ("Bluetiful", "#3C69E7"),
            ("B'dazzled blå", "#2E5894"),
            ("Trækul", "#36454F"),
            ("Cerulean blå", "#2A52BE"),
            ("Kosmisk kobolt", "#2E2D88"),
            ("Celadon grøn", "#2F847C"),
            ("Sort kaffe", "#3B2F2F"),
            ("Amazon", "#3B7A57"),
            ("Mørk sienna", "#3C1414"),
            ("Blå (pigment)", "#333399"),
            ("Mørk skifergrå", "#2F4F4F"),
            ("Mørk kornblomst", "#26428B"),
            ("Bleu de France", "#318CE7"),
            ("Mørke lilla", "#301934"),
            ("Keltisk blå", "#246BCE"),
            ("Charleston grøn", "#232B2B"),
            ("Dodger blå", "#1E90FF"),
            ("Blågrøn (farvehjul)", "#064E40"),
            ("Denim", "#1560BD"),
            ("Eerie sort", "#1B1B1B"),
            ("Denimblå", "#2243B6"),
            ("Blå (Crayola)", "#1F75FE"),
            ("Flickr Blue", "#0063dc"),
            ("Skovgrøn (web)", "#228B22"),
            ("Sort chokolade", "#1B1811"),
            ("Engelsk grøn", "#1B4D3E"),
            ("Brunswick grøn", "#1B4D3E"),
            ("Cerulean (Crayola)", "#1DACD6"),
            ("Fluorescerende blå", "#15F4EE"),
            ("Lys marineblå", "#1974D2"),
            ("Mørk jungle grøn", "#1A2421"),
            ("Mørk forår grøn", "#177245"),
            ("Blå (RYB)", "#0247FE"),
            ("Egyptisk blå", "#1034A6"),
            ("Blå safir", "#126180"),
            ("Blågrøn", "#0D98BA"),
            ("Mørk pastelgrøn", "#03C03C"),
        )
    )

    safe_colors = (
        "sort",
        "rødbrun",
        "grøn",
        "mørkeblå",
        "oliven",
        "lilla",
        "blågrøn",
        "lime",
        "blå",
        "sølv",
        "grå",
        "gul",
        "pink",
        "turkis",
        "hvid",
    )
