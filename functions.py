from tabulate import *


# Lit les informations sur l'automate dans le fichier txt
# Paramètre : fichier qui respecte le format d'écriture des automates
# Return la matrice automate, contenant les informations sur l'automate
def readfile(file):
    infos = []
    with open(file, 'r') as f:
        line = f.readline()
        while line != "":
            line = line.replace('\n', '')
            infos.append(line)
            line = f.readline()
    return infos


def lire_saisie_utilisateur():
    entree = input()
    entree.replace('\n', '')
    return entree


# Identifie les entrées à partir de la matrice automate
# Paramètre : matrice d'un automate lu
# Return une liste d'entrées
def identifier_entrees(automate):
    matrice = automate[2].split(' ')
    for i in range(len(matrice)):
        matrice[i] = int(matrice[i])
    # On supprime le nombre d'entrées, puisqu'on peut y accéder avec len(matrice)
    del matrice[0]
    return matrice


# Identifie les sorties à partir de la matrice automate
# Paramètre : matrice d'un automate lu
# Return une liste de sorties
def identifier_sorties(automate):
    matrice = automate[3].split(' ')
    for i in range(len(matrice)):
        matrice[i] = int(matrice[i])
    # On supprime le nombre de sorties, puisqu'on peut y accéder avec len(matrice)
    del matrice[0]
    return matrice


# Crée une matrice contenant l'alphabet reconnu par l'automate, en fonction de la taille de celui-ci
# Paramètre : matrice d'un automate lu
# Return une liste de lettres
def creer_alphabet(automate):
    alphabet = []
    for i in range(int(automate[0])):
        alphabet.append(chr(97 + i))
    return alphabet


# Récupère toutes les transitions d'une matrice automate et les ordonne dans un tableau 2D, pour faciliter la recherche
# Paramètre : matrice d'un automate lu
# Return une liste 2D de transitions
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


# Trie les états en fonction de leur arrivée, pour un affichage en ordre croissant lors de l'afficher_automate
# Paramètre : liste 2D de transitions, récupérée avec recuper_transition
# Return une liste de transition triée par ordre croissant d'arrivées
def trier_etats_arrivee(transition):
    transition.sort(key=lambda x: x[2])
    return transition


# Affiche l'automate selon le modèle du sujet
# Paramètre : matrice d'un automate lu
# Return : rien → fonction d'affichage
def afficher_automate(automate):
    matrice_affichage = []
    matrice_ligne = ["Fonction", "Etat"]
    alphabet = creer_alphabet(automate)
    for i in range(int(automate[0])):
        matrice_ligne.append(alphabet[i])
    matrice_affichage.append(matrice_ligne)
    for i in range(int(automate[1])):
        matrice_ligne = []
        entrees = identifier_entrees(automate)
        sorties = identifier_sorties(automate)
        if i in entrees and i not in sorties:
            matrice_ligne.append('E')
        elif i not in entrees and i in sorties:
            matrice_ligne.append('S')
        elif i in entrees and i in sorties:
            matrice_ligne.append("E/S")
        else:
            matrice_ligne.append(' ')
        matrice_ligne.append(str(i))
        for j in range(len(alphabet)):
            transitions_lettre = []
            for k in range(int(automate[4])):
                transition = recuperer_transition(automate)
                transition = trier_etats_arrivee(transition)
                if alphabet[j] == transition[k][1] and str(i) == transition[k][0]:
                    transitions_lettre.append(transition[k][2])
            if len(transitions_lettre) == 0:
                transitions_lettre.append("-")
            matrice_ligne.append(transitions_lettre)
        matrice_affichage.append(matrice_ligne)
    # Suppression des sous tableaux → conversion les listes en chaines de caractères séparées par des virgules 
    for ligne in matrice_affichage:
        for j in range(len(ligne)):
            if isinstance(ligne[j], list):
                ligne[j] = ', '.join(ligne[j])
    print(tabulate(matrice_affichage, headers="firstrow", tablefmt="fancy_grid", stralign="center", numalign="center"))


def verification_standard(automate):
    entrees = identifier_entrees(automate)
    transitions = recuperer_transition(automate)
    if len(entrees) != 1:
        return 0
    else:
        for i in range(len(transitions)):
            if transitions[i][2] == entrees[0]:
                return 0
    return 1


# Fonction permettant de standardiser un automate
# Paramètre : matrice d'un automate lu
# Return la matrice de l'automate standardisé
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
                transi = [str(nouvel_etat), transitions[i][1], transitions[i][2]]
                present = 0
                for k in range(len(transitions)):
                    if transi[0] == transitions[k][0] and transi[1] == transitions[k][1] and transitions[k][2] == \
                            transi[2]:
                        present += 1

                if present == 0:
                    transitions.append(transi)
                    automate.append(str(nouvel_etat) + str(transitions[i][1]) + str(transitions[i][2]))
                    automate[2] = "1 " + str(nouvel_etat)
                    automate[4] = int(automate[4])
                    automate[4] += 1
    return automate


def verification_deterministe(automate):
    entrees = identifier_entrees(automate)
    transitions = recuperer_transition(automate)
    if len(entrees) != 1:
        return 0
    for i in range(int(automate[1])):
        transi = []
        for j in range(len(transitions)):
            if i == int(transitions[j][0]):
                transi.append(transitions[j])
        for k in range(len(transi)):
            for l in range(len(transi)):
                if transi[k][0] == transi[l][0] and transi[k][1] == transi[l][1] and transi[l][2] != transi[k][2]:
                    return 2
    return 1


def determiniser_automate(automate):
    matrice = [[[1, 2, 3], [5, 6], [4, 0]], [[5, 6], [4, 0]], [[4, 0], [1, 2, 3]], [[123, 'a', 40], [56, 'b', 123]]]
    entrees = identifier_entrees(automate)
    transitions = recuperer_transition(automate)
    nouvelle_matrice = [[]]
    nouvelle_matrice[0].append(entrees)
    transitions_nouvel_etat = recuperer_transitions_etat(nouvelle_matrice[0][0], transitions)
    nouvel_etat = ''
    for i in range(len(nouvelle_matrice[0][0])):
        nouvel_etat += str(nouvelle_matrice[0][0][i])
    for i in range(len(transitions_nouvel_etat)):
        nouvelle_matrice.append(nouvel_etat)
    print(nouvel_etat)
    print(transitions_nouvel_etat)


def recuperer_transitions_etat(nouvel_etat, transitions):
    transitions_nouvel_etat = []
    for i in range(len(nouvel_etat)):
        for j in range(len(transitions)):
            if nouvel_etat[i] == int(transitions[j][0]):
                matricetemp = [str(nouvel_etat[i]), transitions[j][1], transitions[j][2]]
                transitions_nouvel_etat.append(matricetemp)
    return transitions_nouvel_etat


def verification_complet(automate):
    cases_problematiques = ['']
    transitions = recuperer_transition(automate)
    alphabet = creer_alphabet(automate)
    for i in range(int(automate[1])):
        for j in range(len(alphabet)):
            present = False
            case_problematique = []
            for k in range(len(transitions)):
                if alphabet[j] == transitions[k][1] and i == int(transitions[k][0]):
                    present = True
            if present is False:
                case_problematique.append(str(i))
                case_problematique.append(alphabet[j])
                cases_problematiques.append(case_problematique)
    if len(cases_problematiques) >= 2:
        cases_problematiques[0] = 0
        return cases_problematiques
    else:
        cases_problematiques[0] = 1
        return cases_problematiques


def completer_automate(automate):
    etats_problematiques = verification_complet(automate)
    alphabet = creer_alphabet(automate)
    automate[1] = int(automate[1])
    automate[1] += 1
    nouvel_etat = str(automate[1] - 1)
    automate[4] = int(automate[4])
    for i in range(1, len(etats_problematiques), 1):
        automate[4] += 1
        automate.append(etats_problematiques[i][0] + etats_problematiques[i][1] + nouvel_etat)
    for i in range(len(alphabet)):
        automate[4] += 1
        automate.append(nouvel_etat + alphabet[i] + nouvel_etat)
    return automate


def lire_mot():
    mot = ''
    mots = []
    while mot != 'fin':
        mot = input()
        mot.replace('\n', '')
        if mot != 'fin':
            mots.append(mot)
    return mots
