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

def recuperer_transition(automate):
    transition = []
    lettre = ""
    for i in range(int(automate[4])):
        i += 5
        transition.append(automate[i])
    for i in range(len(transition)):
        for j in range(len(transition[i])):

            if ord(transition[i][j]) >= 97:
                lettre = transition[i][j]
        transition[i] = transition[i].split(lettre)
        transition[i].append(transition[i][1])
        transition[i][1] = lettre
    return transition


def afficher_automate(automate):
    print("        ", end="")
    alphabet = creer_alphabet(automate)
    for i in range(int(automate[0])):
        print("         " + alphabet[i], end="")
    print('\n')
    for i in range(int(automate[1])):
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
        print("  ", end = "")
        if 0 <= i <= 9:
            print(i, end="    |  ")
        if 10 <= i <= 99:
            print(i, end="   |  ")
        if 100 <= i <= 999:
            print(i, end="  |  ")

        for j in range(len(alphabet)):
            transitions_lettre = []
            for k in range(int(automate[4])):
                transition = recuperer_transition(automate)
                if alphabet[j] == transition[k][1] and str(i) == transition[k][0]:
                    transitions_lettre.append(transition[k][2])

            if len(transitions_lettre) == 0:
                transitions_lettre.append("-")
            for l in range(len(transitions_lettre)):
                if len(transitions_lettre) > 1 and l != len(transitions_lettre)-1:
                    print(transitions_lettre[l], end=",")
                else:
                    if len(transitions_lettre) > 1:
                        print(transitions_lettre[l], end="   |    ")
                    else:
                        print(" " + transitions_lettre[l], end = "   |    ")
        print('\n')




def standardiser_automate(automate):
    # créer un nouvel état
    automate[1] = int(automate[1])
    automate[1] += 1
    nouvel_etat = automate[1] - 1
    entrees = identifier_entrees(automate)
    transitions = recuperer_transition(automate)
    for i in range(len(transitions)):
        for j in range(len(entrees)):
            if int(entrees[j]) == int(transitions[i][0]):
                transi = []
                transi.append(str(nouvel_etat))
                transi.append(transitions[i][1])
                transi.append(transitions[i][2])
                present = 0
                for k in range(len(transitions)):
                    if transi[0] == transitions[k][0] and transi[1] == transitions[k][1] and transitions[k][2] == transi[2]:
                        present += 1

                if present == 0:
                    transitions.append(transi)
                    automate.append(str(nouvel_etat)+str(transitions[i][1])+ str(transitions[i][2]))
                    automate[2] = "1 " + str(nouvel_etat)
                    automate[4] = int(automate[4])
                    automate[4] += 1
    return automate







