# Lit les infos sur l'automate dans le fichier txt
def readfile(file):
    infos = []
    with open(file, 'r') as f:
        line = f.readline()
        while (line != ""):
            line = line.replace('\n', '')
            infos.append(line)
            line = f.readline()
    return infos


# 0 = nombre symboles alphabet
# 1 = nombre d'états
# 2 = nombre d'états initiaux et leur valeur
# 3 = nombre d'états terminaux et leur valeur
# 4 = nombre de transitions
# 5 et après: transitions


def identifier_entrees(automate):
    matrice = []
    matrice = automate[2].split(' ')
    for i in range(len(matrice)):
        matrice[i] = int(matrice[i])
    del matrice[0]
    return matrice

def identifier_sorties(automate):
    matrice = []
    matrice = automate[3].split(' ')
    for i in range(len(matrice)):
        matrice[i] = int(matrice[i])
    del matrice[0]
    return matrice


def creer_alphabet(automate):
    alphabet = []
    for i in range(int(automate[0])):
        alphabet.append(chr(97 + i))
    return alphabet

def identifier_transition(ligne, lettre):
    transition = []
    transition = ligne.split(lettre)
    return transition

def afficher_automate(automate):
    print("       ", end="")
    alphabet = creer_alphabet(automate)
    for i in range(int(automate[0])):
        print("         " + alphabet[i], end="")
    print('\n')
    for i in range(int(automate[1])+1):
        print(i, end=" | ")
        entrees = identifier_entrees(automate)
        sorties = identifier_sorties(automate)
        if i in entrees and i not in sorties:
            print('  E ', end="  |")
            print(" ", end="")
        elif i not in entrees and i in sorties:
            print('  S ', end="  |")
            print(" ", end="")
        elif i in entrees and i in sorties:
            print(" E/S", end="  | ")

        else:
            print("     ", end=" | ")
        print(i, end=" | ")

        for j in range(len(alphabet)):
            transitions_lettre = []
            for k in range(int(automate[4])):
                k = k + 5
                transition = identifier_transition(automate[k], alphabet[j])
                if alphabet[j] in transition and str(i) == transition[0]:
                    transitions_lettre.append(transition[2])

            if len(transitions_lettre) == 0:
                transitions_lettre.append("-")
            for l in range(len(transitions_lettre)):
                if len(transitions_lettre) > 1 and l != len(transitions_lettre)-1:
                    print(transitions_lettre[l], end=",")
                else:
                    if len(transitions_lettre) > 1:
                        print(transitions_lettre[l], end="      ")
                    else:
                        print(" " + transitions_lettre[l], end = "       ")

        print('\n')




def standardiser_automate(automate):
    # créer un nouvel état
    automate[1] += 1
    entries = []






def lire_numero_transition_depart(ligne):
    if ord(ligne[1]) > 97:
        return ligne[0]
    else:
        nombre = ""
        compteur = 0
        while(ord(ligne[0 + compteur])) < 97:
            nombre += ligne[0+compteur]
            compteur += 1
        return nombre

def lire_numero_transition_arrivee(ligne):
    compteur = 0
    nombre = ""
    while (ord(ligne[0 + compteur]) < 97):
        compteur += 1
        print(compteur)
    for i in range(compteur+1, len(ligne)):
        print(i)
        nombre += ligne[i]
    return nombre
