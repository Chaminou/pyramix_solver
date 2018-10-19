import numpy as np
import random
import tqdm
from tkinter import *

move = []
melange = []

list_index_check = [(1, 1), (1, 2), (1, 3), (1, 6), (1, 7), (1, 8), (1, 11), (1, 12), (1, 13),
					(2, 1), (2, 2), (2, 3), (2, 6), (2, 7), (2, 8), (2, 11), (2, 12), (2, 13),
					(3, 6), (3, 7), (3, 8),
					(4, 6), (4, 7), (4, 8),]

list_useful_move = ["R", "R'", "U", "U'", "L", "L'", "B", "B'"]

solvedlist = np.array([['0','0','2','0','0','0','0','4','0','0','0','0','3','0','0'], ['0','2','2','2','0','0','4','4','4','0','0','3','3','3','0'], ['2','2','2','2','2','4','4','4','4','4','3','3','3','3','3'], ['0','0','0','0','0','1','1','1','1','1','0','0','0','0','0'], ['0','0','0','0','0','0','1','1','1','0','0','0','0','0','0'], ['0','0','0','0','0','0','0','1','0','0','0','0','0','0','0']])


def switchcolor (tab, linex, rowy) :


	if tab[linex, rowy] == 0 :
		return "black"
	if tab[linex, rowy] == 1 :
		return "yellow"
	if tab[linex, rowy] == 2 :
		return "red"
	if tab[linex, rowy] == 3 :
		return "blue"
	if tab[linex, rowy] == 4 :
		return "green"
	if tab[linex, rowy] == '0' :
		return "black"
	if tab[linex, rowy] == '1' :
		return "yellow"
	if tab[linex, rowy] == '2' :
		return "red"
	if tab[linex, rowy] == '3':
		return "blue"
	if tab[linex, rowy] == '4' :
		return "green"
	if tab[linex, rowy] == 'd' :
		return "#fca1a1"
	if tab[linex, rowy] == 'e' :
		return "#ff5151"
	if tab[linex, rowy] == 'f' :
		return "#842525"
	if tab[linex, rowy] == 'm' :
		return "#ffbcf9"
	if tab[linex, rowy] == 'n' :
		return "#ff70f3"
	if tab[linex, rowy] == 'o' :
		return "#84397e"
	if tab[linex, rowy] == 'p' :
		return "#841d7b"
	if tab[linex, rowy] == 'q' :
		return "#ff00e9"
	if tab[linex, rowy] == 'g' :
		return "#d3ffc4"
	if tab[linex, rowy] == 'h' :
		return "#a1ff82"
	if tab[linex, rowy] == 'i' :
		return "#35bf07"
	if tab[linex, rowy] == 'r' :
		return "#7c9376"
	if tab[linex, rowy] == 's' :
		return "#55824a"
	if tab[linex, rowy] == 't' :
		return "#2c935e"
	if tab[linex, rowy] == 'u' :
		return "#00ff7b"
	if tab[linex, rowy] == 'v' :
		return "#005b2c"
	if tab[linex, rowy] == 'j' :
		return "#bffff7"
	if tab[linex, rowy] == 'k' :
		return "#72ffee"
	if tab[linex, rowy] == 'l' :
		return "#00ffe1"
	if tab[linex, rowy] == 'w' :
		return "#607699"
	if tab[linex, rowy] == 'x' :
		return "#3d5d91"
	if tab[linex, rowy] == 'y' :
		return "#0061ff"
	if tab[linex, rowy] == 'z' :
		return "#00235b"
	if tab[linex, rowy] == '5' :
		return "#005b5a"
	if tab[linex, rowy] == '6' :
		return "#f9e5b8"
	if tab[linex, rowy] == '7' :
		return "#f9cf75"
	if tab[linex, rowy] == '8' :
		return "#ffae00"
	if tab[linex, rowy] == '9' :
		return "#8e7d57"
	if tab[linex, rowy] == 'a' :
		return "#9b7012"
	if tab[linex, rowy] == 'b' :
		return "#e3e884"
	if tab[linex, rowy] == 'c' :
		return "#8ba34b"
	if tab[linex, rowy] == '_' :
		return "#c5ff28"



def turners (tab, movement, tabmov) :

	global move

	cachetab = np.zeros((6, 15), dtype='str')

	i = 0
	j = 0

	for i in range(15) :
		for j in range(6) :
			canard = tab[j, i]
			cachetab[j, i] = canard

	if movement == "u" :

		a = tab[0, 2]
		b = tab[0, 7]
		c = tab[0, 12]
		cachetab[0, 2] = b
		cachetab[0, 7] = c
		cachetab[0, 12] = a

		tabmov.append("u")

		return cachetab


	if movement == "U" :

		a = tab[1, 1]
		b = tab[1, 2]
		c = tab[1, 3]

		d = tab[1, 6]
		e = tab[1, 7]
		f = tab[1, 8]

		g = tab[1, 11]
		h = tab[1, 12]
		i = tab[1, 13]

		cachetab[1, 1] = d
		cachetab[1, 2] = e
		cachetab[1, 3] = f

		cachetab[1, 6] = g
		cachetab[1, 7] = h
		cachetab[1, 8] = i

		cachetab[1, 11] = a
		cachetab[1, 12] = b
		cachetab[1, 13] = c

		j = tab[0, 2]
		k = tab[0, 7]
		l = tab[0, 12]
		cachetab[0, 2] = k
		cachetab[0, 7] = l
		cachetab[0, 12] = j

		tabmov.append("U")

		return cachetab


	if movement == "u'" :

		a = tab[0, 2]
		b = tab[0, 7]
		c = tab[0, 12]
		cachetab[0, 2] = c
		cachetab[0, 7] = a
		cachetab[0, 12] = b

		tabmov.append("u'")

		return cachetab


	if movement == "U'" :

		a = tab[1, 1]
		b = tab[1, 2]
		c = tab[1, 3]

		d = tab[1, 6]
		e = tab[1, 7]
		f = tab[1, 8]

		g = tab[1, 11]
		h = tab[1, 12]
		i = tab[1, 13]

		cachetab[1, 1] = g
		cachetab[1, 2] = h
		cachetab[1, 3] = i

		cachetab[1, 6] = a
		cachetab[1, 7] = b
		cachetab[1, 8] = c

		cachetab[1, 11] = d
		cachetab[1, 12] = e
		cachetab[1, 13] = f

		j = tab[0, 2]
		k = tab[0, 7]
		l = tab[0, 12]
		cachetab[0, 2] = l
		cachetab[0, 7] = j
		cachetab[0, 12] = k

		tabmov.append("U'")

		return cachetab


	if movement == "l" :

		a = tab[2, 4]
		b = tab[2, 5]
		c = tab[3, 5]
		cachetab[2, 4] = c
		cachetab[2, 5] = a
		cachetab[3, 5] = b

		tabmov.append("l")

		return cachetab


	if movement == "L" :

		a = tab[1, 3]
		b = tab[2, 2]
		c = tab[2, 3]

		d = tab[1, 6]
		e = tab[2, 6]
		f = tab[2, 7]

		g = tab[3, 6]
		h = tab[3, 7]
		i = tab[4, 6]


		cachetab[1, 3] = i
		cachetab[2, 2] = h
		cachetab[2, 3] = g

		cachetab[1, 6] = b
		cachetab[2, 6] = c
		cachetab[2, 7] = a

		cachetab[3, 6] = e
		cachetab[3, 7] = d
		cachetab[4, 6] = f

		j = tab[2, 4]
		k = tab[2, 5]
		l = tab[3, 5]
		cachetab[2, 4] = l
		cachetab[2, 5] = j
		cachetab[3, 5] = k

		tabmov.append("L")

		return cachetab


	if movement == "l'" :

		a = tab[2, 4]
		b = tab[2, 5]
		c = tab[3, 5]
		cachetab[2, 4] = b
		cachetab[2, 5] = c
		cachetab[3, 5] = a

		tabmov.append("l'")

		return cachetab


	if movement == "L'" :

		a = tab[1, 3]
		b = tab[2, 2]
		c = tab[2, 3]

		d = tab[1, 6]
		e = tab[2, 6]
		f = tab[2, 7]

		g = tab[3, 6]
		h = tab[3, 7]
		i = tab[4, 6]

		cachetab[1, 3] = f
		cachetab[2, 2] = d
		cachetab[2, 3] = e

		cachetab[1, 6] = h
		cachetab[2, 6] = g
		cachetab[2, 7] = i

		cachetab[3, 6] = c
		cachetab[3, 7] = b
		cachetab[4, 6] = a

		j = tab[2, 4]
		k = tab[2, 5]
		l = tab[3, 5]
		cachetab[2, 4] = k
		cachetab[2, 5] = l
		cachetab[3, 5] = j

		tabmov.append("L'")

		return cachetab


	if movement == "r" :

		a = tab[2, 9]
		b = tab[2, 10]
		c = tab[3, 9]
		cachetab[2, 9] = c
		cachetab[2, 10] = a
		cachetab[3, 9] = b

		tabmov.append("r")

		return cachetab


	if movement == "R" :

		a = tab[1, 8]
		b = tab[2, 7]
		c = tab[2, 8]

		d = tab[1, 11]
		e = tab[2, 11]
		f = tab[2, 12]

		g = tab[3, 7]
		h = tab[3, 8]
		i = tab[4, 8]


		cachetab[1, 8] = g
		cachetab[2, 7] = i
		cachetab[2, 8] = h

		cachetab[1, 11] = b
		cachetab[2, 11] = c
		cachetab[2, 12] = a

		cachetab[3, 7] = f
		cachetab[3, 8] = e
		cachetab[4, 8] = d

		j = tab[2, 9]
		k = tab[2, 10]
		l = tab[3, 9]
		cachetab[2, 9] = l
		cachetab[2, 10] = j
		cachetab[3, 9] = k

		tabmov.append("R")

		return cachetab


	if movement == "r'" :

		a = tab[2, 9]
		b = tab[2, 10]
		c = tab[3, 9]
		cachetab[2, 9] = b
		cachetab[2, 10] = c
		cachetab[3, 9] = a

		tabmov.append("r'")

		return cachetab


	if movement == "R'" :

		a = tab[1, 8]
		b = tab[2, 7]
		c = tab[2, 8]

		d = tab[1, 11]
		e = tab[2, 11]
		f = tab[2, 12]

		g = tab[3, 7]
		h = tab[3, 8]
		i = tab[4, 8]

		cachetab[1, 8] = f
		cachetab[2, 7] = d
		cachetab[2, 8] = e

		cachetab[1, 11] = i
		cachetab[2, 11] = h
		cachetab[2, 12] = g

		cachetab[3, 7] = a
		cachetab[3, 8] = c
		cachetab[4, 8] = b

		j = tab[2, 9]
		k = tab[2, 10]
		l = tab[3, 9]
		cachetab[2, 9] = k
		cachetab[2, 10] = l
		cachetab[3, 9] = j

		tabmov.append("R'")

		return cachetab


	if movement == "b" :

		a = tab[2, 0]
		b = tab[2, 14]
		c = tab[5, 7]
		cachetab[2, 0] = b
		cachetab[2, 14] = c
		cachetab[5, 7] = a

		tabmov.append("b")

		return cachetab


	if movement == "B" :

		a = tab[1, 1]
		b = tab[2, 1]
		c = tab[2, 2]

		d = tab[1, 13]
		e = tab[2, 12]
		f = tab[2, 13]

		g = tab[4, 6]
		h = tab[4, 7]
		i = tab[4, 8]


		cachetab[1, 1] = e
		cachetab[2, 1] = f
		cachetab[2, 2] = d

		cachetab[1, 13] = i
		cachetab[2, 12] = g
		cachetab[2, 13] = h

		cachetab[4, 6] = a
		cachetab[4, 7] = b
		cachetab[4, 8] = c

		j = tab[2, 0]
		k = tab[2, 14]
		l = tab[5, 7]
		cachetab[2, 0] = k
		cachetab[2, 14] = l
		cachetab[5, 7] = j

		tabmov.append("B")

		return cachetab


	if movement == "b'" :

		a = tab[2, 0]
		b = tab[2, 14]
		c = tab[5, 7]
		cachetab[2, 0] = c
		cachetab[2, 14] = a
		cachetab[5, 7] = b

		tabmov.append("b'")

		return cachetab


	if movement == "B'" :

		a = tab[1, 1]
		b = tab[2, 1]
		c = tab[2, 2]

		d = tab[1, 13]
		e = tab[2, 12]
		f = tab[2, 13]

		g = tab[4, 6]
		h = tab[4, 7]
		i = tab[4, 8]


		cachetab[1, 1] = g
		cachetab[2, 1] = h
		cachetab[2, 2] = i

		cachetab[1, 13] = c
		cachetab[2, 12] = a
		cachetab[2, 13] = b

		cachetab[4, 6] = e
		cachetab[4, 7] = f
		cachetab[4, 8] = d

		j = tab[2, 0]
		k = tab[2, 14]
		l = tab[5, 7]
		cachetab[2, 0] = l
		cachetab[2, 14] = j
		cachetab[5, 7] = k

		tabmov.append("B'")

		return cachetab

def randomcube(tab, liste, iteration) :

	global melange

	#random.seed(0)

	for i in range(iteration) :
		tab = turners(tab, random.choice(liste), melange)

	return tab


def grapher(tab, iteration) :

	largeur = 320
	hauteur = 140

	graphx = 0
	praphy = 0

	x = (int(iteration) % 6) * largeur
	y = (int(iteration) // 6) * hauteur

	fenetre = Tk()
	fenetre.title(str(iteration))
	fenetre.resizable(width=False, height=False)
	fenetre.geometry('%dx%d+%d+%d' % (largeur, hauteur, x - 10, y))

	C = Canvas(fenetre, height=640, width=480)

	for graphx in range(0, 6) :

		for graphy in range(0, 15) :

			C.create_oval((graphy*20)+10, (graphx*20)+10, (graphy*20) + 30, (graphx*20) + 30, fill=switchcolor(tab, graphx, graphy))

	C.pack()

	fenetre.mainloop()


def som(tab, algo) :

	global move

	if algo == "ll" :

		tab = turners(tab, "L", move)
		tab = turners(tab, "U'", move)
		tab = turners(tab, "L'", move)

	if algo == "lr" :

		tab = turners(tab, "B'", move)
		tab = turners(tab, "U", move)
		tab = turners(tab, "B", move)

	if algo == "fl" :

		tab = turners(tab, "R", move)
		tab = turners(tab, "U'", move)
		tab = turners(tab, "R'", move)

	if algo == "fr" :

		tab = turners(tab, "L'", move)
		tab = turners(tab, "U", move)
		tab = turners(tab, "L", move)

	if algo == "rl" :

		tab = turners(tab, "B", move)
		tab = turners(tab, "U'", move)
		tab = turners(tab, "B'", move)

	if algo == "rr" :

		tab = turners(tab, "R'", move)
		tab = turners(tab, "U", move)
		tab = turners(tab, "R", move)

	return tab


def gooddowncenter(tab) :

	global move


	if tab[2, 1] == '1' :
		tab = turners(tab, "B", move)
	if tab[2, 13] == '1' :
		tab = turners(tab, "B'", move)

	if tab[2, 3] == '1' :
		tab = turners(tab, "L'", move)
	if tab[2, 6] == '1' :
		tab = turners(tab, "L", move)

	if tab[2, 8] == '1' :
		tab = turners(tab, "R'", move)
	if tab[2, 11] == '1' :
		tab = turners(tab, "R", move)

	return tab


def goodv(tab) :

	global move

	#while tab[4, 6] != 1 or tab[2, 2] != 2 or tab[4, 8] != 1 or tab[2, 12] != 3 :
	for i in range(0, 4) :

		for j in range(0, 4) :

			if tab[1, 1] == '1' or tab[1, 6] == '1' or tab[1, 11] == '1' or tab[1, 13] == '1' or tab[1, 8] == '1' or tab[1, 3] == '1' :

				if tab[1, 1] == '1' and tab[1, 13] == '3':
					tab = som(tab, 'rr')
				if tab[1, 6] == '1' and tab[1, 3] == '2':
					tab = som(tab, 'lr')
				if tab[1, 11] == '1' and tab[1, 8] == '4':
					tab = som(tab, 'fr')
				if tab[1, 13] == '1' and tab[1, 1] == '2':
					tab = som(tab, 'll')
				if tab[1, 8] == '1' and tab[1, 11] == '3':
					tab = som(tab, 'rl')
				if tab[1, 3] == '1' and tab[1, 6] == '4':
					tab = som(tab, 'fl')

			tab = turners(tab, "U", move)

		if tab[2, 2] == '1' :
			tab = som(tab, 'll')
		elif tab[2, 12] == '1' :
			tab = som(tab, 'rr')
		elif tab[2, 7] == '1' :
			tab = som(tab, 'fl')
		elif tab[4, 6] == '1' and tab[2, 2] != '2' :
			tab = som(tab, 'll')
		elif tab[4, 8] == '1' and tab[2, 12] != '3' :
			tab = som(tab, 'rr')
		elif tab[3, 7] == '1' and tab[2, 7] != '4' :
			tab = som(tab, 'fl')

	return tab


def almostfinish(tab) :

	global move

	for i in range(3) :

		if tab[1, 6] == tab[1, 2] and tab[1, 3] == tab[1, 7] and tab[1, 8] == tab[1, 12] and tab[1, 11] == tab[1, 7] :

			tab = turners(tab, "R'", move)
			tab = turners(tab, "L", move)
			tab = turners(tab, "R", move)
			tab = turners(tab, "L'", move)
			tab = turners(tab, "U", move)
			tab = turners(tab, "L'", move)
			tab = turners(tab, "U'", move)
			tab = turners(tab, "L", move)

		elif tab[1, 1] == tab[1, 12] and tab[1, 3] == tab[1, 12] and tab[1, 6] == tab[1, 2] and tab[1, 8] == tab[1, 2] and tab[1, 11] == tab[1, 7] and tab[1, 13] == tab[1, 7] :

			tab = turners(tab, "R'", move)
			tab = turners(tab, "U'", move)
			tab = turners(tab, "R", move)
			tab = turners(tab, "U'", move)
			tab = turners(tab, "R'", move)
			tab = turners(tab, "U'", move)
			tab = turners(tab, "R", move)

		elif tab[1, 1] == tab[1, 7] and tab[1, 3] == tab[1, 7] and tab[1, 6] == tab[1, 12] and tab[1, 8] == tab[1, 12] and tab[1, 11] == tab[1, 2] and tab[1, 13] == tab[1, 2] :

			tab = turners(tab, "R'", move)
			tab = turners(tab, "U", move)
			tab = turners(tab, "R", move)
			tab = turners(tab, "U", move)
			tab = turners(tab, "R'", move)
			tab = turners(tab, "U", move)
			tab = turners(tab, "R", move)

		elif tab[1, 1] == tab[1, 7] and tab[1, 3] == tab[1, 12] and tab[1, 6] == tab[1, 2] and tab[1, 8] == tab[1, 7] and tab[1, 11] == tab[1, 2] and tab[1, 13] == tab[1, 12] :

			tab = turners(tab, "R'", move)
			tab = turners(tab, "L'", move)
			tab = turners(tab, "U'", move)
			tab = turners(tab, "L", move)
			tab = turners(tab, "U", move)
			tab = turners(tab, "R", move)

		elif tab[1, 1] == tab[1, 7] and tab[1, 3] == tab[1, 12] and tab[1, 6] == tab[1, 7] and tab[1, 8] == tab[1, 2] and tab[1, 11] == tab[1, 12] and tab[1, 13] == tab[1, 2] :

			tab = turners(tab, "R'", move)
			tab = turners(tab, "U'", move)
			tab = turners(tab, "L'", move)
			tab = turners(tab, "U", move)
			tab = turners(tab, "L", move)
			tab = turners(tab, "R", move)

		else :
			tab = turners(tab, "U", move)

	for j in range(2) :
		if tab[1, 7] != '4' :
			tab = turners(tab, "U", move)

	return tab

def corners(tab) :

	global move


	if tab[0, 2] == '4' :
		tab = turners(tab, "u'", move)
	elif tab[0, 2] == '3' :
		tab = turners(tab, "u", move)

	if tab[2, 4] == '4' :
		tab = turners(tab, "l", move)
	elif tab[2, 4] == '1' :
		tab = turners(tab, "l'", move)

	if tab[2, 9] == '3' :
		tab = turners(tab, "r", move)
	elif tab[2, 9] == '1' :
		tab = turners(tab, "r'", move)

	if tab[2, 0] == '1' :
		tab = turners(tab, "b", move)
	elif tab[2, 0] == '3' :
		tab = turners(tab, "b'", move)


	return tab

def duplicatetab(tab, debut) :

	cachetab = []

	for i in range(debut, len(tab)) :
		canard = tab[i]
		cachetab.append(canard)

	return cachetab

def clearingmove(tab) :

	newtab = duplicatetab(tab, 0)
	cachetab = []

	totaliteration = len(newtab)

	for j in range(totaliteration):

		i = 0

		while i < len(newtab) :


			if newtab[i] == "U" and newtab[i+1] == "U" :
				cachetab.append("U'")
				i += 1

			elif newtab[i] == "U'" and newtab[i+1] == "U'" :
				cachetab.append("U")
				i += 1

			elif newtab[i] == "U'" and newtab[i+1] == "U" :
				i += 1

			elif newtab[i] == "U" and newtab[i+1] == "U'" :
				i += 1

			else :
				chatons = newtab[i]
				cachetab.append(chatons)

			i += 1

		newtab = duplicatetab(cachetab, 0)
		cachetab = []

	return newtab


def negatif(move) :
	if len(move) == 2 :
		return move[0]
	else :
		a = move + "'"
		return a


def clearallmove(tab) :

	newtab = duplicatetab(tab, 0)

	for j in range(len(tab)) :
		localtest = len(newtab) - 1
		cachetab = []
		i = 0

		while i < localtest :

			negatifiplus1 = negatif(newtab[i + 1])

			if newtab[i] == newtab[i+1] :
				ajout = negatif(newtab[i])
				cachetab.append(ajout)
				i += 1
			elif newtab[i] == negatifiplus1 :
				i += 1
			else :
				ajout = newtab[i]
				cachetab.append(ajout)

			i += 1

		cachetab.append(newtab[i])

		newtab = duplicatetab(cachetab, 0)

	return cachetab



def solvedtest(test, solved, randseed) :
	for i in range(5) :
		for j in range(15) :
			if test[i, j] != solved[i, j] :
				return(randseed)

	return(-1)


def check_if_done(tab, reftab) :
	global list_index_check

	for i in list_index_check :
		if tab[i] != reftab[i] :
			return False

	return True


def bourrin(tab) :

	global solvedlist

	testtab = np.zeros((6, 15), dtype='str')

	for a in tqdm.tqdm(list_useful_move) :
		for b in list_useful_move :
			for c in list_useful_move :
				for d in list_useful_move :
					for e in list_useful_move :
						for f in list_useful_move :
							for g in list_useful_move :

								testtab = np.copy(tab)

								move_to_check =  [a, b, c, d, e, f, g]
								for k in move_to_check :
									testtab = turners(testtab, k, move)

								if check_if_done(testtab, solvedlist) == True :
									return move_to_check
