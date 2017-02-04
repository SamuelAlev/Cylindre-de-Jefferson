"""
    Project name: Cylindre de Jefferson
    Copyright,
    ALEV Samuel (226430@supinfo.com)
    STOCKMAN Jim (227078@supinfo.com)
    (C) 2016 - 2017
    This script was tested with Python 3.6.0 and PyGame 1.9.2b1
"""
import re, random


def convertLetters(text):
    """
    Retire de la chaine de caractère "text" la ponctuation, accents et espaces.
    Le flag "^" permet de retenir uniquement les caractères compris entre A-Z et a-z.
    :param text: Chaine de caractère à convertir.
    :return: Chaine de caractère convertie.
    """
    return re.sub("[^A-Za-z]", '', text)

def mix():
    """
    Génère une liste de lettre majuscule de A à Z et la mélange.
    Remplis un tableau des caractères A jusqu'à Z (depuis l'ASCII),
    mélange le tableau et en fait une chaine de caractère.
    :return: Chaine de caractère entre A-Z.
    """
    L_Letter = [chr(i) for i in range(65, 91)]
    random.shuffle(L_Letter)
    S_Letter = ''.join(L_Letter)
    return S_Letter

def createCylinder(file,n):
    """
    Créé un fichier texte nommé en fonction de la variable "file" avec "n" nombre(s) de ligne(s)
    avec la chaine de caractère générée en retour de la fonction mix().
    :param file: Chaine de caractère qui fait office de nom de fichier.
    :param n: Entier qui définit le nombre de ligne à générer.
    """
    with open(file + ".txt", "w") as f:
        for i in range(n):
            f.write(mix() + "\n")

def loadCylinder(file):
    """
    Charge un fichier texte nommé en fonction de la variable "file" et le stock sous forme de dictionnaire
    avec la clé étant le numéro de ligne et la ligne correspondante étant contenu.
    :param file: Chaine de caractère qui fait office de nom de fichier.
    :return: Dictionnaire avec la clé étant le numéro de ligne et la ligne correspondante étant contenu.
    """
    output = {}
    with open(file + ".txt") as f:
        liste = f.read().splitlines()
        for i in range(len(liste)):
            output[i+1] = liste[i]
    return output

def keyOK(key,n):
    pass

def createKey(n):
    pass

def find(letter,alphabet):
    pass

def shift(i):
    pass

def cipherLetter(letter,alphabet):
    pass

def cipherText(cylinder,key,text):
    pass

#print(convertLetters("Bite c à dudule^$$ù*** â^î-5613.!"))
#print(mix())
#print(loadCylinder('test'))
