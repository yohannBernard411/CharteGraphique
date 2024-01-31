"""Module de convertion des couleur rgb, hexa et hsl"""

def rgb_to_hsl(r, g, b):
    """Convertit une couleur RGB en HSL"""
    # Normalisation des composantes RGB
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # Calcul de la luminosité (L)
    max_color = max(r, g, b)
    min_color = min(r, g, b)
    l = (max_color + min_color) / 2.0

    # Calcul de la saturation (S)
    if max_color == min_color:
        s = 0
    else:
        if l <= 0.5:
            s = (max_color - min_color) / (max_color + min_color)
        else:
            s = (max_color - min_color) / (2.0 - max_color - min_color)

    # Calcul de la teinte (H)
    if max_color == min_color:
        h = 0  # la couleur est un gris
    else:
        if max_color == r:
            h = (60 * (g - b) / (max_color - min_color)) % 360
        elif max_color == g:
            h = (60 * (b - r) / (max_color - min_color) + 120) % 360
        elif max_color == b:
            h = (60 * (r - g) / (max_color - min_color) + 240) % 360

    return round(h), round(s * 100), round(l * 100)


def hsl_to_rgb(h, s, l):
    """Convertit une couleur HSL en RGB"""
    h /= 360.0  # Normalisation de la teinte
    s /= 100.0  # Normalisation de la saturation et de la luminosité
    l /= 100.0

    if s == 0:
        r = g = b = l
    else:
        def hue_to_rgb(p, q, t):
            if t < 0:
                t += 1
            if t > 1:
                t -= 1
            if t < 1/6:
                return p + (q - p) * 6 * t
            if t < 1/2:
                return q
            if t < 2/3:
                return p + (q - p) * (2/3 - t) * 6
            return p

        if l < 0.5:
            q = l * (1 + s)
        else:
            q = l + s - l * s

        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)

    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)

    return r, g, b


def hex_to_rgb(hex_color):
    """Convertit une couleur HEXA en RGB"""
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return r, g, b

def rgb_to_hex(r, g, b):
    """Convertit une couleur RGB en HEXA"""
    hex_r = format(round(r), '02x')
    hex_g = format(round(g), '02x')
    hex_b = format(round(b), '02x')
    hex_color = '#' + hex_r + hex_g + hex_b
    return hex_color

def input_hexa():
    """Permet de saisir la valeur en HEXA"""
    hexa = input("saisissez votre couleur en hexa (#334CFF) : ")
    if hexa[0] == "#":
        print("hexa vaut: ", hexa)
    else:
        print("erreur hexa doit debuter avec #: ")
        input_hexa()
    return hexa

def verif_hsl(hsl):
    """Suite à la rotation chromatique, on doit vérifier de ne pas dépasser les valeurs H(0-360), S(0-100), L(0-100)"""
    hsl_list = list(hsl)
    if hsl_list[0] > 360: hsl_list[0] -= 360
    if hsl_list[0] < 0: hsl_list[0] += 360
    for i in range(1, 3):
        if hsl_list[i] > 100: hsl_list[i] = 100
        if hsl_list[i] < 0: hsl_list[i] = 0
    return hsl_list