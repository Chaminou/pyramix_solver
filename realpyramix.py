#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import numpy as np
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from solvealgofunction import *

# Longeur des axes du repère orthonormé
longueur_axes = 2

#-----------------#
# Transformations #
#-----------------#

# Rotation
# Entrées:
#  -sommet: le point à faire tourner. C'est une liste de trois floats, exemple: sommet = [1,2.5,3]
#  -angle: l'angle en radians (sens trionométrique) de la rotation
#  -vecteur: donne l'axe de la rotation. C'est une liste de trois points.
# Retour:
#  -une liste de trois points contenant les coordonnées de l'image de sommet par la rotation
#
# Voir https://fr.wikipedia.org/wiki/Matrice_de_rotation#En_dimension_trois si besoin
def Rotation(sommet, angle, vecteur):
    c = np.cos(angle)
    s = np.sin(angle)
    norme = np.sqrt(vecteur[0]**2 + vecteur[1]**2 + vecteur[2]**2)

    # [x, y, z] doit être normé
    x = vecteur[0] / norme
    y = vecteur[1] / norme
    z = vecteur[2] / norme
    
    R = [[x**2*(1-c) +   c, x *y*(1-c) - z*s, x *z*(1-c) + y*s],
         [x *y*(1-c) + z*s, y**2*(1-c) + c  , y *z*(1-c) - x*s],
         [x *z*(1-c) - y*s, y *z*(1-c) + x*s, z**2*(1-c) + c]]

    return np.dot(R, np.transpose(sommet))

#-------------#
# Translation #
#-------------#
# Comme la rotation mais en plus simple
def Translation(sommet, vecteur):
    return [sommet[0] + vecteur[0], sommet[1] + vecteur[1], sommet[2] + vecteur[2]]

# Quelques couleurs en RGB
couleurs = [
    [1,1,1], # Blanc
    [1,0,0], # Rouge
    [0,1,0], # Vert
    [0,0,1], # Bleu
    [1,1,0], # Jaune
    [0,1,1], # Cyan
    [1,0,1], # Magenta
    [0.5,0.5,0], # Jaune pas beau
    [0.5,0,0.5],
    [0,0.5,0.5],
    [0,0,0] # Noir
]

#-------------------------------------#
# Listes de points des figures utiles #
#-------------------------------------#

# Le repère orthonormé
sommets_repere = [ [0,0,0], [longueur_axes,0,0], [0,longueur_axes,0], [0,0,longueur_axes] ]
aretes_repere = [[0,1], [0,2], [0,3]]

# ---------------------------#
# Tétraèdre de référence: contexte pour y voir clair #
# -------------------------- #
# On note ABCD le tétraèdre régulier dont:
#  -le coté a pour longueur 1
#  -le centre de gravité G est condondu avec l'origine du repère (O,i,j,k)
#  -(BD) // Ox et vecteur GA et j colinéaire de même sens
# La hauteur de BDC issue de D coupe (BC) en D'. On note D'' l'intersection entre (AH) et (BDC).
#
# On peut alors prouver que (exercice plus difficile qu'il n'y paraît) que:
#  -DD' = racine(3) / 2
#  -AA'' = racine(2/3)
#  -GA'' = (1/4) * racine(2/3) et GA = (3/4) * racine (2/3)
#  -A''D'' = (1*3) * racine(3)/ et A''D = (2*3) * racine(3) / 2
#
# S'en déduisent les coordonnées de A, B, C et D dans le repère (O,i,j,k) = (G,i,j,k):
# A(0, (3*4) * racine(2/3), 0)
# B(-1/2, -(1/4) * racine (2/3), (1/3) * racine(3) / 2 )
# C(1/2, -(1/4) * racine (2/3), (1/3) * racine(3) / 2 )
# D(0, -(1/4) * racine (2/3), -(2/3) * racine(3) / 2 )

# Les sommets sont des triplets de coordonnées
sommets_tetraedre = [
    [0, 0.75 * np.sqrt(2.0/3), 0], # A ("sommet")
    [-0.5, -0.25 * np.sqrt(2.0/3), np.sqrt(3) / 6], # B (avant gauche)
    [0.5, -0.25 * np.sqrt(2.0/3), np.sqrt(3) / 6], # C (avant droit)
    [0, -0.25 * np.sqrt(2.0/3), -np.sqrt(3) / 3], # D (fond)
    [0, 0, 0] # Centre de gravité
    ]
# Les arêtes sont des couples de sommets
aretes_tetraedre = [
    [0,1], [0,2], [0,3], # Arêtes joignant les sommets du triangle ed base au "sommet": [AB], [AC] et [AD]
    [1,2], [2,3], [3,1] # Triangle de base: BCD
]
# Les faces sont des triplets de sommets
faces_tetraedre = [
    [0,1,2], [0,2,3], [0,3,1], # ABC, ACD, ADB
    [1,2,3] # Base: BCD
]
couleurs_aretes_tetraedre = [10,10,10,10,10,10,10]
couleurs_faces_tetraedre = [1,2,3,4]
#-------------------------#
# L'octaèdre de référence #
#-------------------------#
sommets_octaedre = [
    [0, np.sqrt(2)/2, 0], # Le "sommet du haut"
    [0.5, 0, 0.5], # Avant droit
    [0.5, 0, -0.5], # Arrière droit
    [-0.5, 0, -0.5], # Arrière gauche
    [-0.5, 0, 0.5], # Avant gauche
    [0, -np.sqrt(2)/2, 0], # Le "sommet du bas"
    [0, 0, 0] # Centre de gravité
]
# Les arêtes sont des couples de sommets
aretes_octaedre = [
    [0,1], [0,2], [0,3], [0,4],
    [1,2], [2,3], [3,4], [4,1],
    [5,1], [5,2], [5,3], [5,4]
]
# Les faces sont des triplets de sommets (triangles)
faces_octaedre = [
    [0,1,2], [0,2,3], [0,3,4], [0,4,1],
    [5,1,2], [5,2,3], [5,3,4], [5,4,1]    
]
couleurs_aretes_octaedre = [10,10,10,10,10,10,10,10,10,10,10,10]
couleurs_faces_octaedre = [2,0,3,0,0,4,0,1]

class Polyedre:
    def __init__(self, # Constructeur de la classe Polyedre
                 sommets, 
                 aretes,
                 faces,
                 couleurs_aretes = couleurs, # Liste des couleurs des arêtes
                 couleurs_faces = couleurs, # Liste des couleurs des faces
                 vecteur_position = [0, 0, 0],
                 angle = 0,
                 vecteur_rotation = [0, 0, 1]):
        self.sommets = list(sommets) # Attention à cloner la liste (qui est passée par référence)
        self.aretes = aretes
        self.faces = faces
        
        self.couleurs_aretes = couleurs_aretes
        self.couleurs_faces = couleurs_faces

        # Attention ici: la rotation initiale est effectuée avant la translation initiale
        self.rotation(angle, vecteur_rotation)
        self.translation(vecteur_position)
        
        self.sommets_initiaux = list(self.sommets) # Pour afficher les axes du polyèdres

    # On appelle axes les droites (GA), (GB), (GC) et (GD)
    def afficher_axes(self):
        glBegin(GL_LINES)
        couleur = 0
        glColor3fv(couleurs[couleur])
        for sommet in self.sommets_initiaux:
            glVertex3fv([0,0,0])
            glVertex3fv([10 * coordonnee for coordonnee in sommet])
        glEnd()
    def afficher_aretes(self):
        glBegin(GL_LINES)
        couleur = 0
        for arete in self.aretes:
            glColor3fv(couleurs[self.couleurs_aretes[couleur]])
            for sommet in arete:
                glVertex3fv(self.sommets[sommet])
            couleur += 1
        glEnd()
    def afficher_faces(self):
        glBegin(GL_TRIANGLES)
        couleur = 0
        for face in self.faces:
            glColor3fv(couleurs[self.couleurs_faces[couleur]])
            for sommet in face:
                glVertex3fv(self.sommets[sommet])
            couleur += 1
        glEnd()
    def afficher(self):
        self.afficher_faces()
        self.afficher_aretes()
    def rotation(self, angle, vecteur):
        self.sommets[:] = [Rotation(sommet, angle, vecteur) for sommet in self.sommets]
    def translation(self, vecteur):
        self.sommets[:] = [Translation(sommet, vecteur) for sommet in self.sommets]

    # Les rotations s'effectuent par rapport aux axes du tétraèdre de référence
    def haut(self, u = 1):   self.rotation(-u * 2 * np.pi / 3, sommets_tetraedre[0])
    def fond(self, u = 1):   self.rotation(-u * 2 * np.pi / 3, sommets_tetraedre[3])
    def gauche(self, u = 1): self.rotation(-u * 2 * np.pi / 3, sommets_tetraedre[1])
    def droite(self, u = 1): self.rotation(-u * 2 * np.pi / 3, sommets_tetraedre[2])

    def hauti(self, u = 1):   self.rotation(u * 2 * np.pi / 3, sommets_tetraedre[0])
    def fondi(self, u = 1):   self.rotation(u * 2 * np.pi / 3, sommets_tetraedre[3])
    def gauchei(self, u = 1): self.rotation(u * 2 * np.pi / 3, sommets_tetraedre[1])
    def droitei(self, u = 1): self.rotation(u * 2 * np.pi / 3, sommets_tetraedre[2])

class Pyramide:
    def __init__(self):
        # Construction d'un tétraèdre de référence qui servira à tracer les axes de la pyramide
        self.tetraedre_reference = Polyedre(sommets_tetraedre, aretes_tetraedre, faces_tetraedre)
        self.coeff_translation = 1.1 # Pour écarter un peu les différentes pièces, on les translate un peu plus
        
        # Construction des 10 tétraèdres de la pyramide
        self.tetraedres = [
            # Tétraèdres des centres des arêtes (translations du tétraèdre de référence par chacun des
            # vecteurs demi-somme de couples d'extrémités; envisager une boucle
            # A faire:
            #  -modifier (mettre en blanc) les couleurs des faces invisibles de certains tétraèdre
            #  -faire en sorte que les instructions tiennent sur une seule ligne
            Polyedre(sommets_tetraedre, aretes_tetraedre, faces_tetraedre, couleurs_aretes_tetraedre, [1,0,3,0],
                     [(s1+s2)*self.coeff_translation for s1,s2 in zip(sommets_tetraedre[0], sommets_tetraedre[1])]), 
            Polyedre(sommets_tetraedre, aretes_tetraedre, faces_tetraedre, couleurs_aretes_tetraedre, [1,0,0,4],
                     [(s1+s2)*self.coeff_translation for s1,s2 in zip(sommets_tetraedre[1], sommets_tetraedre[2])]),
            Polyedre(sommets_tetraedre, aretes_tetraedre, faces_tetraedre, couleurs_aretes_tetraedre, [0,2,0,4],
                     [(s1+s2)*self.coeff_translation for s1,s2 in zip(sommets_tetraedre[2], sommets_tetraedre[3])]),
            Polyedre(sommets_tetraedre, aretes_tetraedre, faces_tetraedre, couleurs_aretes_tetraedre, [0,2,3,0],
                     [(s1+s2)*self.coeff_translation for s1,s2 in zip(sommets_tetraedre[3], sommets_tetraedre[0])]),
            Polyedre(sommets_tetraedre, aretes_tetraedre, faces_tetraedre, couleurs_aretes_tetraedre, [1,2,0,0],
                     [(s1+s2)*self.coeff_translation for s1,s2 in zip(sommets_tetraedre[0], sommets_tetraedre[2])]),
            Polyedre(sommets_tetraedre, aretes_tetraedre, faces_tetraedre, couleurs_aretes_tetraedre, [0,0,3,4],
                     [(s1+s2)*self.coeff_translation for s1,s2 in zip(sommets_tetraedre[1], sommets_tetraedre[3])]),

            # Tétraèdres des extrémités (translations du tétrèdre de base par chacun des vecteurs sommets); envisager une boucle
            Polyedre(sommets_tetraedre, aretes_tetraedre, faces_tetraedre, couleurs_aretes_tetraedre, [1,2,3,0],
                     [2*s*self.coeff_translation for s in sommets_tetraedre[0]]),
            Polyedre(sommets_tetraedre, aretes_tetraedre, faces_tetraedre, couleurs_aretes_tetraedre, [1,0,3,4],
                     [2*s*self.coeff_translation for s in sommets_tetraedre[1]]),
            Polyedre(sommets_tetraedre, aretes_tetraedre, faces_tetraedre, couleurs_aretes_tetraedre, [1,2,0,4],
                     [2*s*self.coeff_translation for s in sommets_tetraedre[2]]),
            Polyedre(sommets_tetraedre, aretes_tetraedre, faces_tetraedre, couleurs_aretes_tetraedre, [0,2,3,4],
                     [2*s*self.coeff_translation for s in sommets_tetraedre[3]])

        ]
        # Constructions des 4 octaèdres (translations de l'octaèdre de référence par chacun des vecteurs sommet du tétraèdre de référence)
        # Envisager une boucle
        self.octaedres = [
            Polyedre(sommets_octaedre, aretes_octaedre, faces_octaedre, couleurs_aretes_octaedre, [2,0,3,0,0,0,0,1],
                     sommets_tetraedre[0], -np.arccos(np.sqrt(3)/3), [1,0,0]), 
            Polyedre(sommets_octaedre, aretes_octaedre, faces_octaedre, couleurs_aretes_octaedre, [0,0,3,0,0,4,0,1],
                     sommets_tetraedre[1], -np.arccos(np.sqrt(3)/3), [1,0,0]),
            Polyedre(sommets_octaedre, aretes_octaedre, faces_octaedre, couleurs_aretes_octaedre, [2,0,0,0,0,4,0,1],
                     sommets_tetraedre[2], -np.arccos(np.sqrt(3)/3), [1,0,0]),
            Polyedre(sommets_octaedre, aretes_octaedre, faces_octaedre, couleurs_aretes_octaedre, [2,0,3,0,0,4,0,0],
                     sommets_tetraedre[3], -np.arccos(np.sqrt(3)/3), [1,0,0])
        ]
        for i in range (0,4): self.octaedres[i].translation([(self.coeff_translation-1) * s for s in self.tetraedre_reference.sommets_initiaux[i]])
    # Afficher la pyramide revient à afficher chacun de ses polyèdres
    def afficher(self):
        for octaedre in self.octaedres:
            octaedre.afficher()
        for tetraedre in self.tetraedres:
            tetraedre.afficher()
        self.tetraedre_reference.afficher_axes()
    # Tourner la pyramide revient à tourner chacun de ses polyèdres
    def rotation(self, angle, vecteur):
        for octaedre in self.octaedres:
            octaedre.rotation(angle, vecteur)
        for tetraedre in self.tetraedres:
            tetraedre.rotation(angle, vecteur)

    # Pour les méthodes qui suivent et qui permettent de manipuler la pyramide,
    # on teste à chaque fois chacun des 14 polyèdres pour savoir s'ils sont
    # concernés par le mouvement effectué

    # Revoir les tests sur les produits scalaires (cf tranlations pour séparer les pièces
    # font éhouer les dits tests
    
    # Faire tourner les 2 couches du haut
    def Haut(self, u = 1):
        for tetraedre in self.tetraedres:
            if tetraedre.sommets[4][1] < 0.7: # Test sur l'ordonnée du centre de gravité
                tetraedre.haut(u)
        for octaedre in self.octaedres:
            if octaedre.sommets[6][1] < 0.7: # Idem
                octaedre.haut(u)
    # Faire tourner le petit tétraèdre du haut
    def haut(self, u = 1):
        for tetraedre in self.tetraedres:
            if tetraedre.sommets[4][1] < 0.7 + np.sqrt(2.0/3):
                tetraedre.haut(u)
    # Faire tourner les 2 couches de gauche
    def Gauche(self, u = 1):
        for tetraedre in self.tetraedres:
            if sum(np.multiply(tetraedre.sommets[4], sommets_tetraedre[1])) < 0.7: # Test sur le produit scalaire entre OG' et OG
                tetraedre.gauche(u)
        for octaedre in self.octaedres:
            if sum(np.multiply(octaedre.sommets[6], sommets_tetraedre[1])) < 0.7: # Idem 
                octaedre.gauche(u)
    # Faire tourner le petit tétraèdre de gauche
    def gauche(self, u = 1):
        for tetraedre in self.tetraedres:
            if tetraedre.sommets[4][0] < -0.6:
                tetraedre.gauche(u)
    # Faire tourner les 2 couches de droite
    def Droite(self, u = 1):
        for tetraedre in self.tetraedres:
            if sum(np.multiply(tetraedre.sommets[4], sommets_tetraedre[2])) < 0.7: # Test sur le produit scalaire entre OG' et OG
                tetraedre.droite(u)
        for octaedre in self.octaedres:
            if sum(np.multiply(octaedre.sommets[6], sommets_tetraedre[2])) < 0.7: # Idem 
                octaedre.droite(u)
    # Faire tourner le petit tétraèdre de droite
    def droite(self, u = 1):
        for tetraedre in self.tetraedres:
            if tetraedre.sommets[4][0] > 0.6:
                tetraedre.droite(u)
    # Faire tourner les 2 couches du fond
    def Fond(self, u = 1):
        for tetraedre in self.tetraedres:
            if sum(np.multiply(tetraedre.sommets[4], sommets_tetraedre[3])) < 0.7: # Test sur le produit scalaire entre OG' et OG
                tetraedre.fond(u)
        for octaedre in self.octaedres:
            if sum(np.multiply(octaedre.sommets[6], sommets_tetraedre[3])) < 0.7: # Idem 
                octaedre.fond(u)
    # Faire tourner le petit tétraèdre du fond
    def fond(self, u = 1):
        for tetraedre in self.tetraedres:
            if tetraedre.sommets[4][2] < -0.6:
                tetraedre.fond(u)

    def Hauti(self, u = 1):
        for tetraedre in self.tetraedres:
            if tetraedre.sommets[4][1] < 0.7: # Test sur l'ordonnée du centre de gravité
                tetraedre.hauti(u)
        for octaedre in self.octaedres:
            if octaedre.sommets[6][1] < 0.7: # Idem
                octaedre.hauti(u)
    # Faire tourner le petit tétraèdre du haut
    def hauti(self, u = 1):
        for tetraedre in self.tetraedres:
            if tetraedre.sommets[4][1] < 0.7 + np.sqrt(2.0/3):
                tetraedre.hauti(u)
    # Faire tourner les 2 couches de gauche
    def Gauchei(self, u = 1):
        for tetraedre in self.tetraedres:
            if sum(np.multiply(tetraedre.sommets[4], sommets_tetraedre[1])) < 0.7: # Test sur le produit scalaire entre OG' et OG
                tetraedre.gauchei(u)
        for octaedre in self.octaedres:
            if sum(np.multiply(octaedre.sommets[6], sommets_tetraedre[1])) < 0.7: # Idem 
                octaedre.gauchei(u)
    # Faire tourner le petit tétraèdre de gauche
    def gauchei(self, u = 1):
        for tetraedre in self.tetraedres:
            if tetraedre.sommets[4][0] < -0.6:
                tetraedre.gauchei(u)
    # Faire tourner les 2 couches de droite
    def Droitei(self, u = 1):
        for tetraedre in self.tetraedres:
            if sum(np.multiply(tetraedre.sommets[4], sommets_tetraedre[2])) < 0.7: # Test sur le produit scalaire entre OG' et OG
                tetraedre.droitei(u)
        for octaedre in self.octaedres:
            if sum(np.multiply(octaedre.sommets[6], sommets_tetraedre[2])) < 0.7: # Idem 
                octaedre.droitei(u)
    # Faire tourner le petit tétraèdre de droite
    def droitei(self, u = 1):
        for tetraedre in self.tetraedres:
            if tetraedre.sommets[4][0] > 0.6:
                tetraedre.droitei(u)
    # Faire tourner les 2 couches du fond
    def Fondi(self, u = 1):
        for tetraedre in self.tetraedres:
            if sum(np.multiply(tetraedre.sommets[4], sommets_tetraedre[3])) < 0.7: # Test sur le produit scalaire entre OG' et OG
                tetraedre.fondi(u)
        for octaedre in self.octaedres:
            if sum(np.multiply(octaedre.sommets[6], sommets_tetraedre[3])) < 0.7: # Idem 
                octaedre.fondi(u)
    # Faire tourner le petit tétraèdre du fond
    def fondi(self, u = 1):
        for tetraedre in self.tetraedres:
            if tetraedre.sommets[4][2] < -0.6:
                tetraedre.fondi(u)

def gestion_clavier(event, pyramide, tab):
    global fleche_gauche, fleche_droite, fleche_haut, fleche_bas, touche_p, touche_m
    global ratio
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:  fleche_gauche = True
        if event.key == pygame.K_RIGHT: fleche_droite = True
        if event.key == pygame.K_UP:    fleche_haut = True
        if event.key == pygame.K_DOWN:  fleche_bas = True
        if event.key == pygame.K_p:     touche_p = True
        if event.key == pygame.K_m:     touche_m = True
                    
        if event.key == pygame.K_a:
            glLoadIdentity()
            gluPerspective(45, ratio, 0.1, 50.0)
            glTranslatef(0.0,0.0, -8) 
            
                
        if event.key == pygame.K_e: file_operations.append(pyramide.Haut)
        if event.key == pygame.K_r: file_operations.append(pyramide.haut)
        if event.key == pygame.K_q: file_operations.append(pyramide.Gauche)
        if event.key == pygame.K_s: file_operations.append(pyramide.gauche)
        if event.key == pygame.K_d: file_operations.append(pyramide.Fond)
        if event.key == pygame.K_f: file_operations.append(pyramide.fond)
        if event.key == pygame.K_g: file_operations.append(pyramide.Droite)
        if event.key == pygame.K_h: file_operations.append(pyramide.droite)

        if event.key == pygame.K_k:
            spacialturner(melange, pyramide)
            print('30 random scranble moves')
        if event.key == pygame.K_l:
            spacialturner(tab, pyramide)
            print('Solving in ', len(tab), 'moves')
                
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:  fleche_gauche = False
        if event.key == pygame.K_RIGHT: fleche_droite = False
        if event.key == pygame.K_UP:    fleche_haut = False
        if event.key == pygame.K_DOWN:  fleche_bas = False
        if event.key == pygame.K_p:     touche_p = False
        if event.key == pygame.K_m:     touche_m = False

def spacialturner(tab, pyramide) :

    global file_operations


    for i in range(len(tab)) :
        if tab[i] == "R" : file_operations.append(pyramide.Droite)
        if tab[i] == "r" : file_operations.append(pyramide.droite)
        if tab[i] == "R'" : file_operations.append(pyramide.Droitei)
        if tab[i] == "r'" : file_operations.append(pyramide.droitei)

        if tab[i] == "U" : file_operations.append(pyramide.Haut)
        if tab[i] == "u" : file_operations.append(pyramide.haut)
        if tab[i] == "U'" : file_operations.append(pyramide.Hauti)
        if tab[i] == "u'" : file_operations.append(pyramide.hauti)

        if tab[i] == "L" : file_operations.append(pyramide.Gauche)
        if tab[i] == "l" : file_operations.append(pyramide.gauche)
        if tab[i] == "L'" : file_operations.append(pyramide.Gauchei)
        if tab[i] == "l'" : file_operations.append(pyramide.gauchei)

        if tab[i] == "B" : file_operations.append(pyramide.Fond)
        if tab[i] == "b" : file_operations.append(pyramide.fond)
        if tab[i] == "B'" : file_operations.append(pyramide.Fondi)
        if tab[i] == "b'" : file_operations.append(pyramide.fondi)


def main(tab):
    # Instanciation du repère et de la pyramide
    mon_repere = Polyedre(sommets_repere, aretes_repere, [], (1,2,3), ())
    ma_pyramide = Pyramide()
    
    # Clavier (touches pour faire tourner la caméra)
    global fleche_gauche, fleche_droite, fleche_haut, fleche_bas, touche_p, touche_m
    
    fleche_gauche = False
    fleche_droite = False
    fleche_haut = False
    fleche_bas = False
    touche_p = False
    touche_m = False

    pas_rotation_camera = 1 # ~vitesse de rotation de la caméra
    
    # Transition des opérations
    # Clarifier le nom des variables
    global file_operations
    
    file_operations = [] # Liste qui sert de file pour les différentes opérations (Haut, droite, ...)
    taux_transition_operation = 0 # Pour tester quand une opération est complète; voir ci-après
    pas_rotation_operation = 0.1 # pas pour les opérations

    # pygame
    display = (600,600)
    global ratio
    ratio = display[0]/display[1]

    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # pyOpenGl
    gluPerspective(45, ratio, 0.1, 50.0)
    glTranslatef(0.0,0.0, -8) 
    glEnable(GL_DEPTH_TEST) # Permet de cacher les objets placés derrière d'autres objets

    while True:
        # Gestion des événements clavier
        for event in pygame.event.get(): gestion_clavier(event, ma_pyramide, tab)
        
        # Mouvements de la caméra
        if fleche_gauche: glRotatef(pas_rotation_camera, 0, 1, 0)
        if fleche_droite: glRotatef(-pas_rotation_camera, 0, 1, 0)
        if fleche_haut:   glRotatef(pas_rotation_camera, 1, 0, 0)
        if fleche_bas:    glRotatef(-pas_rotation_camera, 1, 0, 0)
        if touche_p:      glRotatef(pas_rotation_camera, 0, 0, 1)
        if touche_m:      glRotatef(-pas_rotation_camera, 0, 0, 1)
        
        # Gestion des animations des opérations
        if taux_transition_operation == 0:
            if(len(file_operations) > 0): # Si une opération est dans la file
                operation_courante = file_operations.pop(0)
                taux_transition_operation += pas_rotation_operation
        elif taux_transition_operation > 1.05:
            taux_transition_operation = 0
        else:
            operation_courante(pas_rotation_operation)
            taux_transition_operation += pas_rotation_operation

        # Mise à jour de l'affichage
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        mon_repere.afficher_aretes()
        ma_pyramide.afficher()
        pygame.display.flip()
        
        pygame.time.wait(10) # Enlevable
