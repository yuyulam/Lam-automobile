# Gestion d’un Parc Automobile

## Projet Python - Encadré par Ibrahima SY (GitHub: https://github.com/syibrahima31)

Ce projet simule la gestion d'un parc de véhicules destinés à la location pour une entreprise fictive nommée AutoPlus. Il met en œuvre les principaux concepts de Programmation Orientée Objet en Python.

---

## Objectifs pédagogiques

Le projet valide les compétences suivantes :
- Encapsulation : utilisation d’attributs privés avec getters/setters.
- Héritage : spécialisation de la classe abstraite `Vehicule`.
- Abstraction : classe abstraite avec méthode non implémentée.
- Polymorphisme : redéfinition de méthodes dans les sous-classes.
- Relations entre classes : association, agrégation, composition.
- Méthodes statiques et de classe : utilisation dans le calcul du prix.

---

## Architecture du projet

- `vehicule.py` : classe abstraite `Vehicule` et ses sous-classes `Voiture` et `Camion`.
- `client.py` : classe `Client`.
- `date.py` : classe `Date` (composition).
- `location.py` : classe `Location`.
- `parc_auto.py` : classe `ParcAuto` (agrégation).
- `main.py` : script principal de démonstration.
- `README.md` : ce fichier.
- `.gitignore` (facultatif) : pour ignorer les fichiers inutiles.

---

## Instructions d’exécution

python main.py
