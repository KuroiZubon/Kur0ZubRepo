# Gestion Employés
from abc import ABC, abstractmethod

class Personnes:
    def __init__(self, nom, prenom, age, matricule):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        # Encapsulation
        self.__matricule = matricule

    # Getter
    def Obtenir_matricule(self):
        return self.__matricule

    def se_presenter(self):
        return(f"Bonjour, je m'appel {self.prenom} {self.nom} et j'ai {self.age} ans!")

class employes(Personnes):
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
         return(f"{Presentation_base} Je suis le {self.roles} de l'usine Kruger.")

    #Abstraction
    def experience(self):
        super().experience()
        print(f"{self.prenom} à {self.experiences} années d'expérience comme {self.roles} à l'usine Kruger!")