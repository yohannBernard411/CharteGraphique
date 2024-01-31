from color_convert import *
import webbrowser
import os

def generate_charte():
    hexa = input_hexa()
    # convertion hexa en rgb
    rgb = hex_to_rgb(hexa)
    # convertion rgb en hsl
    hsl = rgb_to_hsl(rgb[0], rgb[1], rgb[2])
    # rotation chromatique
    light_main = (hsl[0]+1, hsl[1]-21, hsl[2]+20)
    light_main = verif_hsl(light_main)
    dark_main = (hsl[0]+1, hsl[1]+36, hsl[2]-15)
    dark_main = verif_hsl(dark_main)
    secondary = (hsl[0]-10, hsl[1]+19, hsl[2]+45)
    secondary = verif_hsl(secondary)
    light_secondary = (secondary[0]+0, secondary[1]+17, secondary[2]+12)
    light_secondary = verif_hsl(light_secondary)
    dark_secondary = (secondary[0]+0, secondary[1]-40, secondary[2]-20)
    dark_secondary = verif_hsl(dark_secondary)
    contrast = (hsl[0]-156, hsl[1]+19, hsl[2]+15)
    contrast = verif_hsl(contrast)
    # convertion des codes hsl en rgb
    main_rgb = hsl_to_rgb(hsl[0], hsl[1], hsl[2])
    dark_rgb = hsl_to_rgb(dark_main[0], dark_main[1], dark_main[2])
    light_rgb = hsl_to_rgb(light_main[0], light_main[1], light_main[2])
    secondary_rgb = hsl_to_rgb(secondary[0], secondary[1], secondary[2])
    secondary_light_rgb = hsl_to_rgb(light_secondary[0], light_secondary[1], light_secondary[2])
    secondary_dark_rgb = hsl_to_rgb(dark_secondary[0], dark_secondary[1], dark_secondary[2])
    contrast_rgb = hsl_to_rgb(contrast[0], contrast[1], contrast[2])
    # convertion des codes rgb en hexa
    main_hexa = rgb_to_hex(main_rgb[0], main_rgb[1], main_rgb[2])
    dark_hexa = rgb_to_hex(dark_rgb[0], dark_rgb[1], dark_rgb[2])
    light_hexa = rgb_to_hex(light_rgb[0], light_rgb[1], light_rgb[2])
    secondary_hexa = rgb_to_hex(secondary_rgb[0], secondary_rgb[1], secondary_rgb[2])
    secondary_light_hexa = rgb_to_hex(secondary_light_rgb[0], secondary_light_rgb[1], secondary_light_rgb[2])
    secondary_dark_hexa = rgb_to_hex(secondary_dark_rgb[0], secondary_dark_rgb[1], secondary_dark_rgb[2])
    contrast_hexa = rgb_to_hex(contrast_rgb[0], contrast_rgb[1], contrast_rgb[2])
    # generation de la charte graphique dans le fichier de test
    with open('charte.html', 'w') as a_writer:
        a_writer.write("<!DOCTYPE html>\n")
        a_writer.write("<html>\n")
        a_writer.write("    <head>\n")
        a_writer.write("        <title>Charte graphique</title>\n")
        a_writer.write('        <meta charset="utf-8" />\n')
        a_writer.write('        <link rel="stylesheet" href="style.css">\n')
        a_writer.write("    </head>\n")
        a_writer.write("    <body>\n")
        a_writer.write("   <div class='container'>\n")
        a_writer.write('    <div style="background-color:'+main_hexa+'";>MAIN COLOR</div>\n')
        a_writer.write('    <div style="background-color:'+dark_hexa+'";>DARK MAIN COLOR</div>\n')
        a_writer.write('    <div style="background-color:'+light_hexa+'";>LIGHT COLOR</div>\n')
        a_writer.write("    <br>\n")
        a_writer.write('    <div style="background-color:'+secondary_hexa+'";>SECONDARY COLOR</div>\n')
        a_writer.write('    <div style="background-color:'+secondary_light_hexa+'";>SECONDARY LIGHT COLOR</div>\n')
        a_writer.write('    <div style="background-color:'+secondary_dark_hexa+'";>SECONDARY DARK COLOR</div>\n')
        a_writer.write("    <br>\n")
        a_writer.write('    <div style="background-color:'+main_hexa+'";>MAIN COLOR</div>\n')
        a_writer.write('    <div style="background-color:'+contrast_hexa+'";>CONTRAST COLOR</div>\n')
        a_writer.write('    <div style="background-color:'+secondary_hexa+'";>SECONDARY COLOR</div>\n')
        a_writer.write("  </div>\n")
        a_writer.write("    </body>\n")
        a_writer.write("</html>\n")
        a_writer.close()
    url = os.path.abspath(os.path.split(__file__)[0])+'/charte.html'
    webbrowser.open_new_tab(url)

generate_charte()