
class ParcAuto:
    def __init__(self):
        self.vehicules = []  # liste d'instances Vehicule

    def ajouter_vehicule(self, v):
        self.vehicules.append(v)
        print(f"Véhicule {v._modele} ajouté au parc.")

    def lister_disponibles(self):
        """Retourne la liste des véhicules disponibles"""
        return [v for v in self.vehicules if v.est_disponible()]

    def rechercher(self, modele: str):
        """Recherche un véhicule par modèle (retourne la liste correspondante)"""
        return [v for v in self.vehicules if v._modele.lower() == modele.lower()]
