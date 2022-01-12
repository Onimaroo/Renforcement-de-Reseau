#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from graphe import *
import math
import argparse
import os
import re
 
"""
Implémentation des fonctions demandées dans le sujet.
"""

def charger_donnees(reseau, nom_fichier):
    """
    Doctests pour la fonction charger_donnees.
    
    Vous devez avoir implémenté la classe Graphe et la fonction charger_donnees.
    Rajoutez éventuellement ci-dessous les imports nécessaires:
    
    >>> from graphe import *
    >>> from ameliorations import *
    
    Récupérer les données de la ligne de métro 14:
    
    >>> reseau = Graphe()
    >>> charger_donnees(reseau, "METRO_14.txt")
    
    Afficher les identifiants des sommets:
    
    >>> sorted(reseau.sommets())
    [1722, 1757, 1869, 1955, 1964, 2068, 1166824, 1166826, 1166828]
    
    Afficher les noms des sommets:
    
    >>> sorted(map(reseau.nom_sommet, reseau.sommets()))
    ['Bercy', 'Bibliothèque-François Mitterrand', 'Châtelet', 'Cour Saint-Emilion', 'Gare de Lyon', 'Madeleine', 'Olympiades', 'Pyramides', 'Saint-Lazare']
    
    Afficher les arêtes:
    
    >>> sorted(reseau.aretes())  # doctest: +NORMALIZE_WHITESPACE
    [(1722, 1869, 'METRO_14'), (1757, 1869, 'METRO_14'),
    (1757, 1964, 'METRO_14'), (1955, 1964, 'METRO_14'),
    (1955, 2068, 'METRO_14'), (2068, 1166828, 'METRO_14'),
    (1166824, 1166826, 'METRO_14'), (1166826, 1166828, 'METRO_14')]
    
    Rajouter au réseau les données de la ligne de métro 3b:
    
    >>> charger_donnees(reseau, "METRO_3b.txt")
    
    Afficher les identifiants des sommets:
    
    >>> sorted(reseau.sommets())
    [1659, 1718, 1722, 1752, 1757, 1783, 1869, 1955, 1964, 2068, 1166824, 1166826, 1166828]
    
    Afficher les arêtes:
    
    >>> sorted(reseau.aretes())  # doctest: +NORMALIZE_WHITESPACE
    [(1659, 1783, 'METRO_3b'), (1718, 1752, 'METRO_3b'),
    (1718, 1783, 'METRO_3b'), (1722, 1869, 'METRO_14'),
    (1757, 1869, 'METRO_14'), (1757, 1964, 'METRO_14'),
    (1955, 1964, 'METRO_14'), (1955, 2068, 'METRO_14'),
    (2068, 1166828, 'METRO_14'), (1166824, 1166826, 'METRO_14'),
    (1166826, 1166828, 'METRO_14')]
    
    """
    pattern1 = re.compile('\d+/\d+/\d+') # pattern pour les stations
    pattern2 = re.compile('\d+:\D') # pattern pour les aretes
    fichier = open(nom_fichier, "r", encoding = "utf-8")

    for ligne in fichier:
        if pattern1.match(ligne.strip()):
            arete = ligne.split('/')
            reseau.ajouter_arete(int(arete[0]), int(arete[1]), nom_fichier[:len(nom_fichier) - 4])
        if pattern2.match(ligne.strip()):
            reseau.ajouter_sommet(int(ligne.split(':')[0]), ligne.split(':')[1].strip())

    fichier.close()
        
def numerotations(reseau):
    """
    >>> from graphe import *
    >>> from ameliorations import *
    >>> G = Graphe()
    >>> charger_donnees(G, "METRO_3b.txt")
    >>> charger_donnees(G, "METRO_7.txt")
    >>> numerotations(G)
    ({1925: 1, 2055: 33, 1800: 24, 1674: 28, 1805: 15, 1806: 17, 1911: 35, 1808: 3, 1681: 14, 1685: 8, 1944: 34, 1695: 38, 2080: 30, 1696: 37, 1953: 25, 2085: 26, 1703: 29, 1964: 16, 1971: 21, 1718: 39, 1846: 20, 1849: 22, 1854: 10, 1985: 31, 1860: 27, 1734: 5, 1740: 4, 1871: 7, 1744: 32, 1876: 2, 1752: 40, 1757: 19, 2015: 23, 2020: 11, 1639: 36, 1773: 18, 1648: 9, 1649: 12, 1907: 13, 1783: 41, 1659: 42, 1790: 6}, {1925: None, 2055: 1744, 1800: 2015, 1674: 1860, 1805: 1681, 1806: 1964, 1911: 1944, 1808: 1876, 1681: 1907, 1685: 1876, 1944: 2055, 1695: 1696, 2080: 1703, 1696: 1639, 1953: 1800, 2085: 1953, 1703: 1674, 1964: 1805, 1971: 1846, 1718: None, 1846: 1757, 1849: 1971, 1854: 1648, 1985: 2080, 1860: 2085, 1734: 1740, 1740: 1808, 1871: 1790, 1744: 1985, 1876: 1925, 1752: 1718, 1757: 1773, 2015: 1849, 2020: 1854, 1639: 1925, 1773: 1806, 1648: 1685, 1649: 2020, 1907: 1649, 1783: 1718, 1659: 1783, 1790: 1734}, {1925: 1, 2055: 33, 1800: 24, 1674: 28, 1805: 15, 1806: 17, 1911: 35, 1808: 3, 1681: 14, 1685: 8, 1944: 34, 1695: 38, 2080: 30, 1696: 37, 1953: 25, 2085: 26, 1703: 29, 1964: 16, 1971: 21, 1718: 39, 1846: 20, 1849: 22, 1854: 10, 1985: 31, 1860: 27, 1734: 5, 1740: 4, 1871: 7, 1744: 32, 1876: 2, 1752: 40, 1757: 19, 2015: 23, 2020: 11, 1639: 36, 1773: 18, 1648: 9, 1649: 12, 1907: 13, 1783: 41, 1659: 42, 1790: 6})
    """
    debut = dict()
    parent = dict()
    ancetre = dict()
    instant = 0
    for i in reseau.sommets():
        debut[i] = 0
        parent[i] = None
        ancetre[i] = math.inf
    def numérotation_recursive(s):
        nonlocal instant
        instant += 1
        ancetre[s] = instant
        debut[s] = ancetre[s]
        for t in reseau.voisins(s):
            if debut[t] != 0:
                if parent[s] != t:
                    ancetre[s] = min(ancetre[s], debut[t])
            else:
                parent[t] = s
                numérotation_recursive(t)
                ancetre[s] = min(ancetre[s], ancetre[t])
    for v in reseau.sommets():
        if debut[v] == 0:
            numérotation_recursive(v)
    return debut, parent, ancetre
    
def points_articulation(reseau):
    """
    Doctests pour la fonction points_articulation.
    
    Vous devez avoir implémenté la classe Graphe et la fonction points_articulation.
    Rajoutez éventuellement ci-dessous les imports nécessaires:
    
    >>> from graphe import *
    >>> from ameliorations import *
    
    Exemple de l'énoncé:
    
    >>> G = Graphe()
    >>> G.ajouter_sommets(zip('abcdefghijkl', [None] * 12))
    >>> G.ajouter_aretes(
    ...     [('a', 'b', None), ('b', 'c', None), ('c', 'a', None), ('c', 'd', None), ('d', 'e', None),
    ...      ('e', 'f', None), ('f', 'd', None), ('a', 'g', None), ('g', 'h', None), ('h', 'a', None),
    ...      ('h', 'i', None), ('i', 'j', None), ('j', 'h', None), ('j', 'k', None), ('k', 'i', None),
    ...      ('i', 'l', None), ('k', 'h', None)])
    >>> sorted(points_articulation(G))
    ['a', 'c', 'd', 'h', 'i']
    
    Exemple du livre d'Even:
    
    >>> G = Graphe()
    >>> G.ajouter_sommets(zip('abcdefg', [None] * 7))
    >>> G.ajouter_aretes(
    ...     [('a', 'b', None), ('b', 'c', None), ('b', 'd', None), ('c', 'd', None), ('d', 'e', None),
    ...      ('d', 'f', None), ('d', 'g', None), ('e', 'f', None), ('f', 'g', None)])
    >>> sorted(points_articulation(G))
    ['b', 'd']
    
    Exemple de Wikipedia:
    
    >>> G = Graphe()
    >>> G.ajouter_sommets(zip('abcdefghijklmn', [None] * 14))
    >>> G.ajouter_aretes(
    ...     [('a', 'b', None), ('b', 'c', None), ('c', 'd', None), ('d', 'a', None), ('c', 'e', None),
    ...      ('e', 'f', None), ('f', 'g', None), ('g', 'h', None), ('g', 'i', None), ('g', 'm', None),
    ...      ('i', 'j', None), ('i', 'k', None), ('k', 'l', None), ('l', 'm', None), ('m', 'n', None),
    ...      ('n', 'l', None)]
    ... )
    >>> sorted(points_articulation(G))
    ['c', 'e', 'f', 'g', 'i']
    """
    numero = numerotations(reseau)
    def points_articulation_aux(reseau, debut, parent, ancetre):
        articulations = set()
        racines = []
        for v in reseau.sommets():
            if parent[v] == None:
                racines.append(v)
        for depart in racines:
            summum = sum([1 for i in parent.values() if i == depart])
            if summum >= 2:
                articulations.add(depart)
        racines.append(None)
        for v in reseau.sommets():
            if parent[v] not in racines and ancetre[v] >= debut[parent[v]]:
                articulations.add(parent[v])
        return articulations
    return points_articulation_aux(reseau, numero[0], numero[1], numero[2])
           
def ponts(reseau):
    """
    Doctests pour la fonction ponts.
    
    Vous devez avoir implémenté la classe Graphe et la fonction ponts.
    Rajoutez éventuellement ci-dessous les imports nécessaires:
    
    >>> from graphe import *
    >>> from ameliorations import *
    
    >>> # exemple de l'énoncé
    >>> G = Graphe()
    >>> G.ajouter_sommets(zip('abcdefghijkl', [None] * 12))
    >>> G.ajouter_aretes(
    ...     [('a', 'b', None), ('b', 'c', None), ('c', 'a', None), ('c', 'd', None), ('d', 'e', None),
    ...      ('e', 'f', None), ('f', 'd', None), ('a', 'g', None), ('g', 'h', None), ('h', 'a', None),
    ...      ('h', 'i', None), ('i', 'j', None), ('j', 'h', None), ('j', 'k', None), ('k', 'i', None),
    ...      ('i', 'l', None), ('k', 'h', None)])
    >>> sorted(map(sorted, ponts(G)))
    [['c', 'd'], ['i', 'l']]
    
    >>> # exemple du livre d'Even
    >>> G = Graphe()
    >>> G.ajouter_sommets(zip('abcdefg', [None] * 7))
    >>> G.ajouter_aretes(
    ...     [('a', 'b', None), ('b', 'c', None), ('b', 'd', None), ('c', 'd', None), ('d', 'e', None),
    ...      ('d', 'f', None), ('d', 'g', None), ('e', 'f', None), ('f', 'g', None)])
    >>> sorted(map(sorted, ponts(G)))
    [['a', 'b']]
    
    >>> # exemple de wikipedia
    >>> G = Graphe()
    >>> G.ajouter_sommets(zip('abcdefghijklmn', [None] * 14))
    >>> G.ajouter_aretes(
    ...     [('a', 'b', None), ('b', 'c', None), ('c', 'd', None), ('d', 'a', None), ('c', 'e', None),
    ...      ('e', 'f', None), ('f', 'g', None), ('g', 'h', None), ('g', 'i', None), ('g', 'm', None),
    ...      ('i', 'j', None), ('i', 'k', None), ('k', 'l', None), ('l', 'm', None), ('m', 'n', None),
    ...      ('n', 'l', None)]
    ... )
    >>> sorted(map(sorted, ponts(G)))
    [['c', 'e'], ['e', 'f'], ['f', 'g'], ['g', 'h'], ['i', 'j']]
    
    """
    debut, parent, ancetre = numerotations(reseau)
    liste_ponts = set()
    for u in reseau.sommets():
        if parent[u] is not None and ancetre[u] > debut[parent[u]]:
            liste_ponts.add((u, parent[u]))
    return liste_ponts
    
def getFirstKey(dico, val) :
    """Renvoie la première clef dans le dictionnaire ayant pour valeur val"""
    for item in dico.items() :
        if item[1] == val :
            return item[0]
    return None

def detectionCSP(G) :
    """Renvoie un dictionnaire spécifiant pour chaque sommet d'un graphe
    la date du représentant de sa CSP."""
    debut, _, ret = numerotations(G)
    def find(x) :
        nonlocal debut
        nonlocal ret
        if ret[x] != ret.get(getFirstKey(debut, ret[x])) :
            ret[x] = find(getFirstKey(debut, ret[x]))
        return ret[x]
    for u in G.sommets() :
        ret[u] = find(u)
    return ret

def feuillesCSP(ponts, CSP):
    """Renvoie les dates des représentants d'une CSP qui est une feuille."""
    feuilles = set()
    noeuds = set()
    for (u, v) in ponts :
        x, y = CSP[u], CSP[v]
        if x in feuilles :
            feuilles.remove(x)
            noeuds.add(x)
        elif x not in noeuds:
            feuilles.add(x)
        if y in feuilles :
            feuilles.remove(y)
            noeuds.add(y)
        elif y not in noeuds :
            feuilles.add(y)
    return feuilles

def candidats(G, ponts, CSP, feuilles) :
    """Renvoie une liste de sommets candidats à être utiliser pour la 
    suppression des ponts."""
    ret = list()
    CSP_choisie = set()
    sommets_ponts = set(sum(ponts, ()))
    for s in G.sommets() :
        if CSP[s] in feuilles and not CSP[s] in CSP_choisie :
            if not s in sommets_ponts or G.degre(s) == 1 :
                ret.append(s)
                CSP_choisie.add(CSP[s])
        if CSP_choisie == feuilles :
            break
    return ret

    
def amelioration_ponts(reseau):
    """
    Doctests pour la fonction amelioration_ponts; on ne vérifie ici que la
    disparition des ponts, et pas la qualité des solutions.
    
    Vous devez avoir déjà implémenté la classe Graphe et la fonction ponts.
    Rajoutez éventuellement ci-dessous les imports nécessaires:
    
    >>> from graphe import *
    >>> from ameliorations import *
    
    Exemple de l'énoncé:
    
    >>> G = Graphe()
    >>> G.ajouter_sommets(zip('abcdefghijkl', [None] * 12))
    >>> G.ajouter_aretes(
    ...     [('a', 'b', None), ('b', 'c', None), ('c', 'a', None), ('c', 'd', None), ('d', 'e', None),
    ...      ('e', 'f', None), ('f', 'd', None), ('a', 'g', None), ('g', 'h', None), ('h', 'a', None),
    ...      ('h', 'i', None), ('i', 'j', None), ('j', 'h', None), ('j', 'k', None), ('k', 'i', None),
    ...      ('i', 'l', None), ('k', 'h', None)])
    >>> for u, v in amelioration_ponts(G):
    ...     G.ajouter_arete(u, v, None)
    >>> len(ponts(G))
    0
    
    Exemple du livre d'Even:
    
    >>> G = Graphe()
    >>> G.ajouter_sommets(zip('abcdefg', [None] * 7))
    >>> G.ajouter_aretes(
    ...     [('a', 'b', None), ('b', 'c', None), ('b', 'd', None), ('c', 'd', None), ('d', 'e', None),
    ...      ('d', 'f', None), ('d', 'g', None), ('e', 'f', None), ('f', 'g', None)])
    >>> for u, v in amelioration_ponts(G):
    ...     G.ajouter_arete(u, v, None)
    >>> len(ponts(G))
    0
    
    Exemple de Wikipedia:
    
    >>> G = Graphe()
    >>> G.ajouter_sommets(zip('abcdefghijklmn', [None] * 14))
    >>> G.ajouter_aretes(
    ...     [('a', 'b', None), ('b', 'c', None), ('c', 'd', None), ('d', 'a', None), ('c', 'e', None),
    ...      ('e', 'f', None), ('f', 'g', None), ('g', 'h', None), ('g', 'i', None), ('g', 'm', None),
    ...      ('i', 'j', None), ('i', 'k', None), ('k', 'l', None), ('l', 'm', None), ('m', 'n', None),
    ...      ('n', 'l', None)]
    ... )
    >>> for u, v in amelioration_ponts(G):
    ...     G.ajouter_arete(u, v, None)
    >>> len(ponts(G))
    0
    
    """
    ret = set()
    CSP = detectionCSP(reseau)
    lst_ponts = ponts(reseau)
    feuilles = feuillesCSP(lst_ponts, CSP)
    lst_candidats = candidats(reseau, lst_ponts, CSP, feuilles)
    for i in range(len(lst_candidats) - 1) :
        ret.add((lst_candidats[i], lst_candidats[i + 1]))
    return ret
    
def amelioration_points_articulation(reseau):
    """
    Doctests pour la fonction amelioration_points_articulation; on ne vérifie ici que la
    disparition des points d'articulation, et pas la qualité des solutions.
    
    Vous devez avoir implémenté la classe Graphe et la fonction points_articulation.
    Rajoutez éventuellement ci-dessous les imports nécessaires:
    
    >>> from graphe import *
    >>> from ameliorations import *
    
    Exemple de l'énoncé:
    
    >>> G = Graphe()
    >>> G.ajouter_sommets(zip('abcdefghijkl', [None] * 12))
    >>> G.ajouter_aretes(
    ...     [('a', 'b', None), ('b', 'c', None), ('c', 'a', None), ('c', 'd', None), ('d', 'e', None),
    ...      ('e', 'f', None), ('f', 'd', None), ('a', 'g', None), ('g', 'h', None), ('h', 'a', None),
    ...      ('h', 'i', None), ('i', 'j', None), ('j', 'h', None), ('j', 'k', None), ('k', 'i', None),
    ...      ('i', 'l', None), ('k', 'h', None)])
    >>> for u, v in amelioration_points_articulation(G):
    ...     G.ajouter_arete(u, v, None)
    >>> len(points_articulation(G))
    0
    
    Exemple du livre d'Even:
    
    >>> G = Graphe()
    >>> G.ajouter_sommets(zip('abcdefg', [None] * 7))
    >>> G.ajouter_aretes(
    ...     [('a', 'b', None), ('b', 'c', None), ('b', 'd', None), ('c', 'd', None), ('d', 'e', None),
    ...      ('d', 'f', None), ('d', 'g', None), ('e', 'f', None), ('f', 'g', None)])
    >>> for u, v in amelioration_points_articulation(G):
    ...     G.ajouter_arete(u, v, None)
    >>> len(points_articulation(G))
    0
    
    Exemple de Wikipedia:
    
    >>> G = Graphe()
    >>> G.ajouter_sommets(zip('abcdefghijklmn', [None] * 14))
    >>> G.ajouter_aretes(
    ...     [('a', 'b', None), ('b', 'c', None), ('c', 'd', None), ('d', 'a', None), ('c', 'e', None),
    ...      ('e', 'f', None), ('f', 'g', None), ('g', 'h', None), ('g', 'i', None), ('g', 'm', None),
    ...      ('i', 'j', None), ('i', 'k', None), ('k', 'l', None), ('l', 'm', None), ('m', 'n', None),
    ...      ('n', 'l', None)]
    ... )
    >>> for u, v in amelioration_points_articulation(G):
    ...     G.ajouter_arete(u, v, None)
    >>> len(points_articulation(G))
    0
    
    """
    numero = numerotations(reseau)
    liste_aretes = set()
    def amelioration_points_articulation_aux(reseau, debut, parent, ancetre):
        nonlocal liste_aretes
        racines = []
        for v in sorted(reseau.sommets()):
            if parent[v] == None:
                racines.append(v)
        racines.append(None)
        for u in sorted(reseau.sommets(), key=lambda item: debut[item], reverse = True):
            for v in sorted(reseau.sommets(), key=lambda item: debut[item], reverse = True):
                if parent[u] in racines and parent[u] == parent[v] and u != v and (v, u) not in liste_aretes:
                    liste_aretes.add((u, v))
                elif ancetre[u] != ancetre[v]:
                    if parent[v] not in racines and ancetre[v] >= debut[parent[v]]:
                        liste_aretes.add((v, racines[0]))
    amelioration_points_articulation_aux(reseau, numero[0], numero[1], numero[2])
    return liste_aretes

def main():
    import doctest
    doctest.testmod()
    G = Graphe()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--metro", type=str, help= "précise les lignes de métro que l’on veut charger dans le réseau. Le paramètre lignes est facultatif : s’il existe, il s’agit des numéros de lignes qui nous intéressent (par exemple : --metro 3b 7 14) ; sinon, on charge toutes les lignes de métro disponibles dans le répertoire courant.", nargs = "*")
    parser.add_argument("--rer", type=str, help= "cf. --metro, mais pour les lignes de RER." , nargs = "*")
    parser.add_argument("--liste-stations", help= " affiche la liste des stations du réseau avec leur identifiant triées par ordre alphabétique", action="store_true")
    parser.add_argument("--articulations", help="affiche les points d’articulation du réseau qui a été chargé", action="store_true")
    parser.add_argument("--ponts", help= "affiche les ponts du réseau qui a été chargé", action="store_true")
    parser.add_argument("--ameliorer-articulations", help= "affiche les points d’articulation du réseau qui a été chargé, ainsi que les arêtes à rajouter pour que ces stations ne soient plus des points d’articulation", action="store_true")
    parser.add_argument("--ameliorer-ponts", help= "affiche les ponts du réseau qui a été chargé, ainsi que les arêtes à rajouter pour que ces arêtes ne soient plus des ponts", action="store_true")
    
    args = parser.parse_args()
    if args.metro is not None:
        if len(args.metro) > 0:
            for nom in args.metro:
                print("Chargement des lignes {} de metro ... terminé.".format(nom))
                charger_donnees(G, "METRO_{}.txt".format(nom))
        else:
            list = os.listdir(r"..\Network_Project")
            for nom in list:
                f_split = nom.split('_')
                if f_split[0] == "METRO":
                    print("Chargement des lignes {} de metro ... terminé.".format(nom))
                    charger_donnees(G, nom)
        print("Le réseau contient {} sommets et {} arêtes.".format(len(G.sommets()), len(G.aretes())))
        
    if args.rer is not None:
        if len(args.rer) > 0:
            for nom in args.rer:
                print("Chargement des lignes {} de RER ... terminé.".format(nom))
                charger_donnees(G, "RER_{}.txt".format(nom))
        else:
            list = os.listdir(r"..\Network_Project")
            for nom in list:
                f_split = nom.split('_')
                if f_split[0] == "RER":
                    print("Chargement des lignes {} de RER ... terminé.".format(nom))
                    charger_donnees(G, nom)
        print("Le réseau contient {} sommets et {} arêtes.".format(len(G.sommets()), len(G.aretes())))
        
    if args.liste_stations:
        print("Le réseau contient les {} stations suivantes:".format(len(G.sommets())))
        for station, nom in sorted(G.liste_sommets.items(), key=lambda item: item[1]):
            print("{} ({})".format(nom, station))
            
    if args.articulations:
        print("Le réseau contient les {} articulations suivants:".format(len(points_articulation(G))))
        numéro = 1
        for articulation in sorted(points_articulation(G), key=lambda item: G.nom_sommet(item)):
            print("{} : {}".format(numéro, G.nom_sommet(articulation)))
            numéro += 1
            
    if args.ponts:
        print("Le réseau contient les {} ponts suivants:".format(len(ponts(G))))
        for pont in sorted(ponts(G), key=lambda item: G.nom_sommet(item[0])):
            print("{} -- {}".format(G.nom_sommet(pont[0]), G.nom_sommet(pont[1])))
            
    if args.ameliorer_articulations:
        print("On peut éliminer tous les points d'articulations du réseau en rajoutant les {} arêtes suivantes".format(len(amelioration_points_articulation(G))))
        for arete in sorted(amelioration_points_articulation(G), key=lambda item: G.nom_sommet(item[0])):
            print("{} -- {}".format(G.nom_sommet(arete[0]), G.nom_sommet(arete[1])))
            
    if args.ameliorer_ponts:
        print("On peut éliminer tous les ponts du réseau en rajoutant les {} arêtes suivantes".format(len(amelioration_ponts(G))))
        for arete in sorted(amelioration_ponts(G), key=lambda item: G.nom_sommet(item[0])):
            print("{} -- {}".format(G.nom_sommet(arete[0]), G.nom_sommet(arete[1])))

        


if __name__ == "__main__":
    main()