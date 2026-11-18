# TP3 — Études de cas Small Data et Big Data

**Étudiant :** Karim Abdelwadoud
**Identifiant :** ID22
**Date :** 18/11/2026

## 1. Présentation du projet

Ce travail pratique présente deux études de cas portant sur l'analyse et le traitement des données.

- **Small Data :** prédiction du résultat d'un match de football à partir de l'European Soccer Database.
- **Big Data :** prédiction de la valeur des transactions à partir du dataset Santander Value Prediction Challenge.

L'objectif est de mettre en œuvre les différentes étapes d'un processus de traitement des données : Data, EDA, Prétraitement, Transformation, Machine Learning, Évaluation et Déploiement.

## 2. Organisation du dépôt

```text
TP3_IDxx/
├── README.md
├── Small/
│   ├── 01_Soccer_Prediction_Small_Data.ipynb
└── Big/
    ├── 02_Santander_Value_Prediction_Big_Data.ipynb

```

## 3. Projet 1 — Small Data : Soccer Prediction

### Description
Ce projet consiste à prédire le résultat d'un match de football.

La variable cible possède trois classes :
- H : victoire de l'équipe à domicile.
- D : match nul.
- A : victoire de l'équipe à l'extérieur.

### Dataset
European Soccer Database.

### Technologies
- Python
- Pandas et NumPy
- PySpark
- Scikit-learn
- Matplotlib et Seaborn
- FastAPI
- Docker

### Méthodologie
1. Chargement des données.
2. Analyse exploratoire (EDA).
3. Prétraitement et nettoyage.
4. Création des variables explicatives.
5. Entraînement des modèles de classification.
6. Évaluation des performances.
7. Déploiement avec FastAPI et Docker.

### Résultats
L'accuracy obtenue sur le jeu de test est d'environ 51,7 % pour le modèle évalué.

## 4. Projet 2 — Big Data : Santander Value Prediction

### Description
Ce projet consiste à prédire la valeur d'une transaction à partir de nombreuses variables explicatives.

### Dataset
Santander Value Prediction Challenge.

### Dimensions
- Entraînement : 4 459 lignes et 4 993 colonnes.
- Test : 49 342 lignes et 4 992 colonnes.

### Technologies
- Python
- Apache Spark / PySpark
- Spark SQL
- RDD et MapReduce
- Spark MLlib
- Pandas et NumPy
- Matplotlib

### Méthodologie
1. Chargement des données.
2. Analyse exploratoire distribuée.
3. Prétraitement.
4. Transformation des variables.
5. Sélection des variables.
6. Entraînement des modèles avec Spark MLlib.
7. Évaluation avec RMSLE.
8. Génération du fichier de soumission Kaggle.

### Résultats
Le modèle Random Forest obtient un RMSLE de validation de 1.3684 dans les résultats initiaux.

Le traitement est effectué en mode local avec Spark. HDFS est proposé comme configuration optionnelle.

## 5. Installation et exécution

### Prérequis
- Python 3.12
- Java compatible avec la version de Spark utilisée
- Jupyter Notebook
- PySpark
- Docker Desktop (pour le déploiement du projet Soccer, si utilisé)

### Exécution du projet Small Data
1. Ouvrir le dossier Small.
2. Installer les dépendances depuis requirements.txt.
3. Ouvrir le notebook.
4. Exécuter toutes les cellules dans l'ordre.

### Exécution du projet Big Data
1. Ouvrir le dossier Big.
2. Installer les dépendances depuis requirements.txt.
3. Vérifier l'installation de Java.
4. Ouvrir le notebook.
5. Exécuter les cellules dans l'ordre.

## 6. Contribution et état des notebooks

Les notebooks présentent les traitements effectués, les explications, les résultats et les conclusions.

L'état d'exécution complet et les éventuels problèmes rencontrés sont précisés dans la première cellule Markdown de chaque notebook.

## 7. Conclusion générale

Ces deux projets permettent de mettre en pratique les techniques d'analyse et de traitement des données.

Le projet Small Data aborde la classification et le déploiement d'un modèle prédictif.

Le projet Big Data met en évidence les possibilités d'Apache Spark pour traiter des données de grande dimension, réaliser des transformations distribuées et entraîner des modèles de Machine Learning.
