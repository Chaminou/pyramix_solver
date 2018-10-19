from solvealgofunction import *


solvedlist = np.array([['0','0','2','0','0','0','0','4','0','0','0','0','3','0','0'], ['0','2','2','2','0','0','4','4','4','0','0','3','3','3','0'], ['2','2','2','2','2','4','4','4','4','4','3','3','3','3','3'], ['0','0','0','0','0','1','1','1','1','1','0','0','0','0','0'], ['0','0','0','0','0','0','1','1','1','0','0','0','0','0','0'], ['0','0','0','0','0','0','0','1','0','0','0','0','0','0','0']])
debuglist = np.array([['0','0','2','0','0','0','0','4','0','0','0','0','3','0','0'], ['0','d','e','f','0','0','g','h','i','0','0','j','k','l','0'], ['m','n','o','p','q','r','s','t','u','v','w','x','y','z','5'], ['0','0','0','0','0','6','7','8','9','a','0','0','0','0','0'], ['0','0','0','0','0','0','b','c','_','0','0','0','0','0','0'], ['0','0','0','0','0','0','0','1','0','0','0','0','0','0','0']])

listedemouvement = ["R", "r", "R'", "r'", "U", "u", "U'", "u'", "L", "l", "L'", "l'", "B", "b", "B'", "b'"]

#grapher(solvedlist, 0)

solvedlist = randomcube(solvedlist, listedemouvement, 30)
#grapher(solvedlist, 0)
solvedlist = gooddowncenter(solvedlist)
#grapher(solvedlist, 0)
solvedlist = goodv(solvedlist)
#grapher(solvedlist, 0)
solvedlist = almostfinish(solvedlist)
#grapher(solvedlist, 0)

solvedlist = corners(solvedlist)
#grapher(solvedlist, 0)
'''

print(len(move))
print(move)
'''
duck = clearallmove(move)
'''
print('résolu en', len(duck), 'étapes !')
print(duck)
''' 
from essai_opengl import *

main(duck)















