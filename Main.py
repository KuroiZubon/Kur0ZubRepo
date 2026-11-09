from POO_00Q6_V2 import*

#------------------ Définition du menu -------------------------------
#
def menu():
    print("[1] Option 1: Obtenir le nom complet de l'employé.")
    print("[2] Option 2: Obtenir matricule de l'employé.")
    print("[3] Option 3: Obtenir le salaire d'employé.")
    print("[4] Option 4: Modifier le salaire d'un employé non cadre.")
    print("[5] Option 5: Présentation de l'employé.")
    print("[6] Option 6: Obtenir l'expérience d'un cadre.")
    print("[0] Option 0: Terminer le programme!")

#------------- Listes du personnels (objets) -------------------------
#
Raj = Employes("Pattel", "Raj", 30, "RAJPAT123", "Opérateur", 3000.0)
Lizzy = Employes("Macbeth", "Lizzy", 25, "LIZMACBETH975", "Emballeur",2999.9)
Mimi = Contremaitre("Kotori", "Mimi", 40, "MIKOTORI246", "Contremaitre", 4)
Kazuki = CEO("Momotaro", "Kazuki", 60, "KAZMOMOTARO680", "CEO", 25)

#----------------- Liste commune -------------------------------------
#
membre_usine = [Raj,Lizzy,Mimi,Kazuki]

#--------------- Définition de fonction ------------------------------

def trouver_employe(prenom):
 #---- Retourne prénom ou None si le prenom n'existe pas. ------------
    for employe in membre_usine:
        if employe.prenom.lower() == prenom.lower():   # "raj" ou "Raj" fonctionnent
            return employe
    return None
#------------------ Lecture de l'input utilisateur -------------------
#
def lire_option():
    while True:
        try:
            option = int(input("Entrer votre option! "))
        except ValueError:
            print("Erreur : veuillez entrer un nombre.")
            continue

        if 0 <= option <= 6:
            return option
        print("Erreur : option invalide. Choisissez un nombre entre 0 et 6.")

#---------- Début du programme: Gestionnaire d'employé --------------
menu()
option = lire_option()

while option != 0:
    input_prenom = input("Veuillez indiquer le prénom de l'employé! ")
    employe = trouver_employe(input_prenom)

    if employe is None:
        print(f"Aucun employé nommé {input_prenom}.")
        print()
    elif option == 1:
        print(f" Le nom complet de l'employé est {employe.prenom} {employe.nom}.")
        print()
    elif option == 2:
        id_perso = employe.obtenir_matricule()
        print(f"Le matricule de {employe.prenom} est {id_perso}")
        print()
    elif option == 3:
        if employe is None:
            print("Erreur! Cet employé n'existe pas!")
            print()
        elif isinstance(employe, Cadre):
            print(f"Erreur! {employe.prenom} est un cadre. Son salaire ne peut pas être obtenu ici!")
            print()
        else:
            salaire_emp = employe.obtenir_salaire()
            print(f"Le salaire de {employe.prenom} est {salaire_emp}")
            print()
    elif option == 4:
        if employe is None:
            print("Erreur! Cet employé n'existe pas!")
            print()
        elif isinstance(employe, Cadre):
            print(f"Erreur! {employe.prenom} est un cadre. Son salaire ne peut pas être modifié ici!")
            print()
        else:                    
            while True:
                try:
                    nouveau_salaire = float(input("Entrez le nouveau salaire : "))
                except ValueError:
                    print("Erreur! Veuillez entrer un montant valide!")
                    continue
                if nouveau_salaire > 0:
                    employe.modifier_salaire(nouveau_salaire)
                    break
                print("Erreur! Le salaire doit être un montant positif!")
                print()
    elif option == 5: # polymorphisme
           presentation = employe.se_presenter()
           print(f"{presentation}")
           print()
    elif option == 6:
        if employe is None:
            print("Erreur! Cet employé n'existe pas!")
            print()
        elif not isinstance(employe, Cadre):
            print(f"Erreur! {employe.prenom} n'est pas un cadre!")
            print()
        else:
            exp = employe.experience()
            print()
    elif option == 0:
        exit
    menu()
    option = lire_option()
#----------- Fermeture du programme! ---------------------------------
#
print("Fin du programme. Merci d'avoir utilisé le gestionnaire d'employés!")