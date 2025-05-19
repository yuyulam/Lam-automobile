# location.py

class Location:
    def __init__(self, client, vehicule, date_debut, date_fin):
        self.client = client          # instance Client
        self.vehicule = vehicule      # instance Vehicule (ou sous-classe)
        self.date_debut = date_debut  # instance Date
        self.date_fin = date_fin      # instance Date

    def duree(self) -> int:
        return self.date_debut.difference(self.date_fin)

    def afficher(self):
        print(f"Location du {self.date_debut.to_string()} au {self.date_fin.to_string()}")
        print(f"Client : {self.client.infos()}")
        self.vehicule.afficher_info()
        print(f"Durée : {self.duree()} jours")

    @staticmethod
    def calcul_prix(duree_jours: int) -> float:
        prix_journalier = 25000
        return duree_jours * prix_journalier
