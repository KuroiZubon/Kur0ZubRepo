# Gestion Employés
from abc import ABC, abstractmethod
class Personnes:
    def __init__(self, nom, prenom, age, matricule):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.__matricule = matricule

    # Getter
    def Obtenir_matricule(self):
        return self.__matricule

    # Encapsulation
    def se_presenter(self):
        return(f"Bonjour, je m'appel {self.prenom} {self.nom} et j'ai {self.age} ans!")

class employé(Personnes):
    def __init__(self, nom, prenom, age, matricule, role, salaire_initial):
        super().__init__(nom, prenom, age, matricule)
        self.__salaire = salaire_initial
        self.role = role

    #Getter
    def Obtenir_salaire(self):
        return self.__salaire
    
    #Setter
    def Modifier_salaire (self, nouveau_salaire):
        if nouveau_salaire > 0:
            self.__salaire = nouveau_salaire
            print(f"Le salaire de {self.prenom} a été mis à jour. Le nouveau salaire est de {self.__salaire} $")
        else:
            print(f"Erreur! Le salaire doit être un montant positif!")

    #Encapsulation            
    def se_presenter(self):
        Presentation_base = super().se_presenter()
        return(f"{Presentation_base} Je suis un {self.role} à l'usine Kruger.")

# Création d'une abstraction pour Cadre
class cadre(Personnes, ABC):
    @abstractmethod
    def experience(self):
        pass

class contremaitre(cadre):
    def __init__(self, nom, prenom, age, matricule, roles, experiences):
        super().__init__(nom, prenom, age, matricule)
        self.experiences = experiences
        self.roles = roles

    def se_presenter(self):
            Presentation_base = super().se_presenter()
            return(f"{Presentation_base} Je suis un {self.roles} à l'usine Kruger.")
    #L'abstraction
    def experience(self):
        super().experience()
        print(f"{self.prenom} à {self.experiences} années d'expérience comme {self.roles} à l'usine Kruger!")

class CEO(cadre):
    def __init__(self, nom, prenom, age, matricule, roles, experiences):
        super().__init__(nom, prenom, age, matricule)
        self.experiences = experiences
        self.roles = roles

    def se_presenter(self):
         Presentation_base = super().se_presenter()
         print(f"{Presentation_base} Je suis le {self.roles} de l'usine Kruger.")

    #Abstraction
    def experience(self):
        super().experience()
        print(f"{self.prenom} à {self.experiences} années d'expérience comme {self.roles} à l'usine Kruger!")

#Listes du personnels
Raj = employé("Pattel", "Raj", 30, "RAJPAT123", "Opérateur", 3000.0,)
Liz = employé("Macbeth", "Lizzy", 25, "LIZMACBETH975", "Emballeur",2999.9)
Mimi = contremaitre("Kotori", "Mimi", 40, "MIKOTORI246", "Contremaitre", 4)
Kazu = CEO("Momotaro", "Kazuki", 60, "KAZMOMOTARO680", "CEO", 25)

#Liste commune
membre_usine = [Raj,Liz,Mimi,Kazu]

for membre in membre_usine:
    print(membre.se_presenter())
print()

id_Raj = Raj.Obtenir_matricule()
print(f"Le matricule de Raj est {id_Raj}")

salaire_Raj = Raj.Obtenir_salaire()
print(f"Le salaire de Raj est {salaire_Raj} $")

nouv_salaire = Raj.Modifier_salaire (nouveau_salaire = 4000)
print()

id_Mimi = Mimi.Obtenir_matricule()
print(f"Le matricule de Mimi est {id_Mimi}")
exp_Mimi = Mimi.experience()
print()
print()

id_Kazu = Kazu.Obtenir_matricule()
print (f"Le matricule de Kazuki est {id_Kazu}.")
exp_Kazu = Kazu.experience()
print()

id_Liz = Liz.Obtenir_matricule()
print(f"Le matricule de Lizzy est {id_Liz}.")

salaire_Liz = Liz.Obtenir_salaire()
print(f"Le salaire de Lizzy est de {salaire_Liz} $.")