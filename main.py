from functions import *


entree = ''
while input != "fin":
    print("Projet Automates Groupe ..")
    print("Choisissez le numéro de l'automate :")
    entree = lire_saisie_utilisateur()
    if entree == "fin":
        break
    file = "E1-" + entree + ".txt"
    automate = (readfile(file))
    afficher_automate(automate)
    if verification_standard(automate) != 1:
        print("Votre automate n'est pas standardisé. Voulez-vous le standardiser ? (oui/non)")
        entree = lire_saisie_utilisateur()
        if entree == "fin":
            break
        if entree == "oui":
            automate = standardiser_automate(automate)
            print("Voici l'automate standardisé")
            afficher_automate(automate)

    else:
        print("Votre automate est déja standardisé !")
    if verification_deterministe(automate) == 0:
        print("Votre automate n'est pas déterministe. Voulez-vous le déterminiser ? (oui/non)")
        entree = lire_saisie_utilisateur()
        if entree == "fin":
            break
        if entree == "oui":
            automate = determiniser_automate(automate)
            print("Voici l'automate determinisé")
            afficher_automate(automate)

