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
    """
    Vérifie lavalidité d'une clé pour le chiffrage ou déchiffrage du message
    :param key: Un liste d'entiers positifs compris entre 1 et n
    :param n: Un entier strictement positif
    :return:
    """
    for x in key:
        if x < 1 or x > n:
            print("clé invalide")
            return False
    return True

def createKey(n):
    """
    Génère une clé sous forme d'une liste d'entiers positifs généré aléatoirement
    et compris entre 1 et n
    :param n: Limite de la range attribuée
    :return: retourne la clé sous forme de liste
    """
    liste = []
    for x in range(0,27):
        liste += [int(random.randrange(1,n))]
    return liste

def find(letter,alphabet):
    """
    Renvoi la position d'une lettre dans l'alphabet rentré
    :param letter: lettre rentrée en paramètre
    :param alphabet: Alphabet rentré en paramètre
    :return: Retourne la position dans l'alphabet
    """
    upLetter = letter.upper()
    position = 0
    for x in alphabet:
        if x == upLetter:
            return position
        else:
            position += 1
    print("Lettre non présente")

def shift(i):
    """
    i est un entier compris entre 0 et 25
    la fonction retournera i + 6 modulo de 26
    :param i: L'entier rentré en paramètre
    :return: retourne le résultat de l'opération
    """
    shiffting = (i+6) % 26
    return shiffting

def cipherLetter(letter,alphabet):
    pass

def cipherText(cylinder,key,text):
    pass

#print(convertLetters("Bite c à dudule^$$ù*** â^î-5613.!"))   Pourquoi Sam xD
#print(mix())
#print(loadCylinder('test'))
