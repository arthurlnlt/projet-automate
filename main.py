from functions import *

entree = ''
while input != "fin":
    print("Projet Automates Groupe E3")
    print("Choisissez le numéro de l'automate :")
    entree = lire_saisie_utilisateur()
    if entree == "fin":
        break
    file = "Automates/E3-" + entree + ".txt"
    numautomate = entree
    automate = (readfile(file))
    trace_execution(automate, numautomate, "Automate originel")
    afficher_automate(automate)
    if verification_standard(automate) != 1:
        print("Votre automate n'est pas standardisé. Voulez-vous le standardiser ? (oui/non)")
        entree = lire_saisie_utilisateur()
        if entree == "fin":
            break
        if entree == "oui":
            automate = standardiser_automate(automate)
            trace_execution(automate, numautomate, "standardisation")
            print("Voici l'automate standardisé")
            afficher_automate(automate)
    else:
        print("Votre automate est déja standardisé !")
    complet = verification_complet(automate)
    if complet[0] == 0:
        print("Votre automate n'est pas complété dans les cases :", end=" ")
        for i in range(1, len(complet), 1):
            print(complet[i][0] + complet[i][1], end=" ")
        print("Voulez-vous le compléter ? (oui/non)")
        entree = lire_saisie_utilisateur()
        if entree == "fin":
            break
        if entree == "oui":
            automate = completer_automate(automate)
            trace_execution(automate, numautomate, "complétion")
            print("Voici l'automate complété: ")
            afficher_automate(automate)
    else:
        print("Votre automate est déjà complet !")
    print("Voulez-vous créer le complémentaire de l'automate ? (oui/non)")
    entree = lire_saisie_utilisateur()
    if entree == "fin":
        break
    if entree == "oui":
        print("Voici l'automate complémentaire: ")
        automate_complementaire = complementaire(automate)
        trace_execution(automate_complementaire, numautomate, "complémentaire")

        afficher_automate(automate_complementaire)
    deterministe = verification_deterministe(automate)
    if deterministe == 0 or deterministe == 2:
        if deterministe == 1:
            print("Votre automate n'est pas déterministe (trop d'entrées). Voulez-vous le déterminiser ? (oui/non)")
        else:
            print("Votre automate n'est pas déterministe (ambiguité). Voulez-vous le déterminiser ? (oui/non)")
        entree = lire_saisie_utilisateur()
        if entree == "fin":
            break
        if entree == "oui":
            print("Voici l'automate determinisé")

    else:
        print("Votre automate est déja déterministe !")
    print("Lecture de mots : (saisissez 'fin' pour arrêter la saisie)")