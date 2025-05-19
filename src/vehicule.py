# vehicule.py
from abc import ABC, abstractmethod

class Vehicule(ABC):
    def __init__(self, marque: str, modele: str, annee: int):
        self._marque = marque            # attribut protégé marque
        self._modele = modele            # attribut protégé modèle
        self._annee = annee              # attribut protégé année
        self._disponible = True          # par défaut, véhicule disponible

    @abstractmethod
    def afficher_info(self):
        pass

    def louer(self):
        if self._disponible:
            self._disponible = False
            print(f"Le véhicule {self._modele} a été loué.")
        else:
            print(f"Le véhicule {self._modele} n'est pas disponible pour la location.")

    def rendre(self):
        self._disponible = True
        print(f"Le véhicule {self._modele} a été rendu et est disponible.")

    def est_disponible(self) -> bool:
       return self._disponible


class Voiture(Vehicule):
    def __init__(self, marque: str, modele: str, annee: int, nb_portes: int):
        super().__init__(marque, modele, annee)
        self.nb_portes = nb_portes  

    def afficher_info(self):
        dispo = "Disponible" if self._disponible else "Loué"
        print(f"Voiture : {self._marque} {self._modele} ({self._annee}), "
              f"{self.nb_portes} portes, État : {dispo}")


class Camion(Vehicule):
    def __init__(self, marque: str, modele: str, annee: int, capacite: float):
        super().__init__(marque, modele, annee)
        self.capacite = capacite 

    def afficher_info(self):
        dispo = "Disponible" if self._disponible else "Loué"
        print(f"Camion : {self._marque} {self._modele} ({self._annee}), "
              f"Capacité : {self.capacite} tonnes, État : {dispo}")
