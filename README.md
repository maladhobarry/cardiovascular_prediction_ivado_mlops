# 🩺 Prédiction des Maladies Cardiovasculaires

Ce projet met en œuvre une chaîne complète de Machine Learning moderne, orientée vers la **prédiction des maladies cardiovasculaires**, avec une architecture pensée pour la **production, la traçabilité** et la **scalabilité**.

---

## 🚀 Fonctionnalités clés

- 📦 Chargement, prétraitement et transformation des données (`DatasetLoader`)
- ✅ Validation des données avec [DeepSeek](https://github.com/deepseek-ai)
- 🤖 Entraînement de multiples modèles :
  - `LogisticRegression`, `LinearSVC`, `RandomForest`, `ExtraTrees`, `MLPClassifier`, `SGDClassifier`, `DecisionTree`, etc.
- 📊 Suivi complet des expériences avec **MLflow**
  - Enregistrement automatique des paramètres, modèles, artefacts, ROC AUC, F1, précision, rappel, etc.
- ⚙️ Orchestration des tâches avec **Prefect**
- 🧩 Intégration d’une base **MongoDB** pour la gestion des données
- 🌐 Déploiement d’une API d’inférence avec **Flask**
- 🔁 Automatisation CI/CD via **GitHub Actions**
- ☁️ Déploiement sur **Google Cloud Platform (GCP)**

---

## 🧠 Objectif

Ce projet vise à créer une base robuste, réplicable et industrialisable pour tout cas de prédiction médicale reposant sur des données tabulaires enrichies.
