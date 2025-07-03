# Simulateur Financier Polyvalent - Calculateur d’Impôt sur le Revenu

## Description
1. Ce logiciel permet de calculer le montant de l’impôt sur le revenu en France en fonction de la composition familiale, des revenus imposables et des pensions versées aux enfants étudiants.  
2. Il prend en compte le quotient familial, applique le barème progressif officiel et affiche le montant final de l’impôt ainsi que le revenu net annuel et mensuel.

## Fonctionnalités
1. Calcul du nombre de parts fiscales selon le nombre d’adultes, d’enfants et d’étudiants dans le foyer.  
2. Vérification du plafond légal des pensions versées aux étudiants (max 6 674 € par étudiant).  
3. Application du barème progressif officiel de l’impôt sur le revenu.  
4. Affichage clair du montant d’impôt, du revenu net annuel et du revenu net mensuel.  
5. Interface graphique intuitive développée avec Tkinter pour saisir les paramètres et lancer la simulation.

## Utilisation
- Renseignez le nombre d’adultes dans le foyer.  
- Indiquez le nombre d’étudiants et d’enfants à charge.  
- Entrez le revenu imposable annuel brut.  
- Saisissez le montant annuel de la pension versée par étudiant (doit être inférieur à 6 674 € par étudiant).  
- Cliquez sur "Lancer la simulation" pour afficher le résultat.

## Structure
- `nom_du_script.py` : Fichier principal contenant la fonction de calcul d’impôt et l’interface graphique Tkinter.  
    1. `impots(...)` : Calcule l’impôt, le revenu net annuel et mensuel selon les paramètres saisis.  
    2. `Page3` : Classe Tkinter qui gère l’interface utilisateur (formulaire de saisie et affichage des résultats).  
    3. `Application` : Classe principale qui initialise la fenêtre Tkinter et affiche la page de calcul.  
- `README.md` : Documentation du projet (ce fichier).  
- `requirements.txt` : Liste des dépendances nécessaires (matplotlib, numpy).

## Contributions
Les contributions sont les bienvenues ! N’hésitez pas à proposer des améliorations ou corriger des bugs via pull requests.

## Licence
Ce projet est sous licence MIT.

## Auteur
Ton Nom
