from vehicule import Voiture, Camion
from client import Client
from date import Date
from location import Location
from parc_auto import ParcAuto

def main():
    # Création de véhicules
    voiture1 = Voiture("Mercedes", "GLe", 2024, 4)
    voiture2 = Voiture("BMW", "X6", 2019, 4)
    camion1 = Camion("Volvo", "FH16", 2018, 20.5)

    # Création de clients
    client1 = Client("Ahmady", 1)
    client2 = Client("Yuyu", 2)

    # Création des dates de location
    date_debut1 = Date(1, 5, 2025)
    date_fin1 = Date(10, 5, 2025)

    # Création des locations
    location1 = Location(client1, voiture1, date_debut1, date_fin1)
    location2 = Location(client2, camion1, Date(5, 5, 2025), Date(15, 5, 2025))

    # Création parc auto
    parc = ParcAuto()
    parc.ajouter_vehicule(voiture1)
    parc.ajouter_vehicule(voiture2)
    parc.ajouter_vehicule(camion1)

    # Affichage véhicules disponibles
    print("\nVéhicules disponibles :")
    for vehicule in parc.lister_disponibles():
        vehicule.afficher_info()

    # Recherche par modèle
    modele_recherche = "GLe"
    print(f"\nRecherche du modèle '{modele_recherche}' :")
    trouve = parc.rechercher(modele_recherche)
    for vehicule in trouve:
        vehicule.afficher_info()

    # Affichage des détails des locations et calcul prix
    print("\nDétails des locations :")
    location1.afficher()
    prix1 = Location.calcul_prix(location1.duree())
    print(f"Prix total : {prix1} CFA\n")

    location2.afficher()
    prix2 = Location.calcul_prix(location2.duree())
    print(f"Prix total : {prix2} CFA\n")

    # Tester louer et rendre un véhicule
    print("\nTester la location d'un véhicule :")
    voiture1.louer()   # loue v1
    voiture1.louer()   # essaye de louer v1 à nouveau (doit bloquer)
    voiture1.rendre()  # rend v1
    voiture1.louer()   # reloue v1

if __name__ == "__main__":
    main()
