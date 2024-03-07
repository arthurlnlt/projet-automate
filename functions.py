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

def afficher_automate(automate):
    alphabet = []
    for i in range(int(automate[0])):
        alphabet.append(chr(97 + i))
        print("        " + alphabet[i], end="")
    print('\n')
    for i in range(int(automate[1])):
        if (" " + str(i)) in automate[2]:
            print('E', end="")
        if (" " + str(i)) in automate[3]:
            print('S ', end="")
        else:
            print("  ", end="")
        print(i, end=" | ")

        for j in range(len(alphabet)):
            transitions_lettre = []
            for k in range(int(automate[4])):
                k = k + 5
                # prévoir pour nombre d'états à 2 chiffre
                if alphabet[j] in automate[k] and str(i) == automate[k][0]:
                    transitions_lettre.append(automate[k][2])

            if len(transitions_lettre) == 0:
                transitions_lettre.append("--")
            l = 0
            for l in range(len(transitions_lettre)):
                if len(transitions_lettre) > 1 and l != len(transitions_lettre)-1:
                    print(transitions_lettre[l], end=",")
                else:
                    print(transitions_lettre[l], end = "       ")

        print('\n')
