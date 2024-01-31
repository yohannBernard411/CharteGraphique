# Charte Graphique

1 Pourquoi ?
===========

Pour gagner du temps lors de la conception de la maquette sous figma.

J'avais déterminer un ensemble de couleur pour mon portefolio et je m'en suis servit de base pour ce générateur.


![Ma charte portefolio](C:\Users\yohan\Desktop\testCharteGraphique\ChartePortefolio.png "Ma charte portefolio").

2 Recherche
===========

Alors la premiére version ne donnait rien car je modifiais directement les valeurs en RGB, ce qui me donnait des résultats plus qu'approximatifs.

Pour obtenir de meilleurs résultats, il a fallu que je passe en HSL, afin d'effectuer une "rotation chromatique", et ainsi obtenir des résultats plus cohérents.

3 Développement
===============

Les fonctions de conversions hexa vers rgb et rgb vers hsl sont trés bien expliqués dans wikipedia et facilement convertibles en code python.

Je les ai regroupées dans le module color_convert.

Le fichier generate_charte n'est que le déroulement de la convertion.

Ensuite les couleurs sont enregistrer dans un fichier html pour étre directement ouvert dans le navigateur afin d'avoir un rendu visuel de la charte graphique créée.

4 Instalation
=============

Il suffit de cloner le repo

```shell
git clone https://github.com/yohannBernard411/CharteGraphique.git
```

Il utilise les librairies webbrowser et os


5 Utilisation
=============

```shell
py generate_charte.py
```

La console vous demande alors la couleur en hexa (Ne pas oublié le # devant)

Puis le navigateur s'ouvre pour vous afficher la charte graphique créée

![Nouvelle charte graphique](C:\Users\yohan\Desktop\testCharteGraphique\CharteBrowser.png "Nouvelle charte graphique").


6 Conclusion
============
Encore une tache automatisée pour gagner du temps lors de mes prochaines créations. 🕰️

