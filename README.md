# 🛍️ Recommandation d'Articles - Projet Data Mining

Ce projet consiste à développer un système de recommandation d’articles complémentaires à partir de transactions d’achat réelles, en utilisant les règles d'association (Apriori).

## 📊 Objectif

Créer un moteur de recommandation capable de :
- Analyser des paniers d’achat
- Identifier les associations fréquentes entre les articles
- Proposer des articles complémentaires pertinents

## 📁 Données

Le dataset utilisé est un fichier CSV contenant **7501 transactions anonymes** de clients.  
Chaque ligne correspond à un panier, avec des articles séparés par des virgules.

Exemple :
```csv
milk, eggs, bread
spaghetti, mineral water
```

## ⚙️ Méthodologie

1. **Prétraitement des données** : suppression des valeurs manquantes, structuration des paniers
2. **Extraction de règles** avec l’algorithme **Apriori** (`mlxtend`)
3. **Filtrage** des règles selon le support, la confiance et le lift
4. **Création d’un moteur de recommandation personnalisé**
5. **Développement d’une application web avec Flask**

## 🌐 Application Flask

Une interface web permet à l’utilisateur :
- d’entrer un panier (ex : `"milk, eggs"`)
- de recevoir en réponse une liste de **recommandations d’articles complémentaires**


## 🛠️ Technologies utilisées

- Python 3
- Pandas
- Mlxtend
- Flask
- HTML/CSS

## 📌 Auteur

**Salimata Faye**  

