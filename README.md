# Renforcement-de-Reseau
Un mini-projet de renforcement de réseau fait en Python.

## Lancer le code
Il faut éxécuter le fichier `ameliorations.py`, qui va dépendre du script `graphe.py` pour fonctionner. En effet, `graphe.py` va définir une classe qui va représenter le réseau.
`ameliorations.py` va utiliser cette classe pour charger les données à partir des fichiers donnés pour qu'elle puisse convertir cette charge de données en une classe réseau. Elle peut également lister la liste des ponts et des points d'articulations et améliorer le réseau pour faire en sorte qu'il n'ait plus de ponts ou de points d'articulation. (Se référer à l'énoncé pour plus de détails à ce sujet).

## Options
Pour mener à bien l'éxécution du fichier `ameliorations.py`, il faut aussi ajouter des options en plus dans la ligne de commande:

`--metro [lignes]` : précise les lignes de métro que l’on veut charger dans le réseau. Le paramètre `lignes` est facultatif : s’il existe, il s’agit des numéros de lignes qui nous intéressent (par exemple : --metro 3b 7 14) ; sinon, on charge toutes les lignes de métro disponibles dans le répertoire courant.

`--rer [lignes]` : cf. `--metro`, mais pour les lignes de RER.

`--liste-stations` : affiche la liste des stations du réseau avec leur identifiant triées par ordre alphabétique.

`--articulations` : affiche les points d’articulation du réseau qui a été chargé.

`--ponts` : affiche les ponts du réseau qui a été chargé.

`--ameliorer-articulations` : affiche les points d’articulation du réseau qui a été chargé, ainsi que les arêtes à rajouter pour que ces stations ne soient plus des points d’articulation.

`--ameliorer-ponts` : affiche les ponts du réseau qui a été chargé, ainsi que les arêtes à rajouter pour que ces arêtes ne soient plus des ponts.

## Pour plus d'informations...
Se référer au fichier PDF `Énoncé.pdf` pour lire la consigne du projet.

