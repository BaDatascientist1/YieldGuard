# Guide de déploiement de l'application Streamlit pour la prédiction des rendements

Ce guide explique étape par étape comment déployer une application Streamlit pour prédire les rendements agricoles en utilisant des modèles pré-entraînés (SARIMAX). Les données climatiques futures sont requises en tant qu'entrées.

---

## 1. **Prérequis**

### Logiciels nécessaires
- **Python 3.8 ou supérieur**
- **Git** (pour cloner et gérer le dépôt GitHub)
- **Streamlit** (pour exécuter l'application)
- **pip** ou **conda** (pour installer les dépendances)

### Bibliothèques Python requises
- streamlit
- numpy
- pandas
- statsmodels
- pmdarima
- matplotlib

Ces bibliothèques sont listées dans le fichier `requirements.txt`.

---

## 2. **Configuration locale du projet**

1. **Cloner le dépôt GitHub**
   
   Si votre projet est sur GitHub, cloner le répertoire avec la commande suivante :
   ```bash
   git clone <URL_du_dépôt>
   ```
   Naviguez ensuite dans le dossier du projet :
   ```bash
   cd <nom_du_répertoire>
   ```

2. **Installer les dépendances**
   
   Si vous utilisez **pip** :
   ```bash
   pip install -r requirements.txt
   ```
   Si vous utilisez **conda** :
   ```bash
   conda create --name my_env --file requirements.txt
   conda activate my_env
   ```

3. **Vérifier l'installation**
   Lancez Streamlit pour tester localement l'application :
   ```bash
   streamlit run app.py
   ```
   Cela ouvrira une interface dans votre navigateur. Assurez-vous que tout fonctionne correctement.

---

## 3. **Organisation des fichiers**

Assurez-vous que votre répertoire contient les fichiers suivants :

- **app.py** : le fichier principal contenant le code de l'application.
- **requirements.txt** : liste des bibliothèques nécessaires.
- **modèles pré-entraînés** : fichiers enregistrés (par ex. `sarimax_riz.pkl`, `sarimax_arachide.pkl`).

Structure suggérée :
```
Projet/
|— app.py
|— requirements.txt
|— sarimax_riz.pkl
|— sarimax_arachide.pkl
|— Donnees/
    |— exemple_donnees.csv
```

---

## 4. **Déploiement sur Streamlit Cloud**

1. **Créer un compte Streamlit Cloud**
   - Rendez-vous sur [streamlit.io](https://streamlit.io/) et créez un compte.
   
2. **Importer votre projet**
   - Depuis votre tableau de bord, cliquez sur **New App**.
   - Sélectionnez le dépôt GitHub contenant votre projet.

3. **Configurer l'application**
   - Branche : choisissez la branche principale (généralement `main` ou `master`).
   - Chemin du fichier : indiquez le chemin vers `app.py` (par exemple, `app.py` si à la racine).

4. **Déployer**
   Cliquez sur **Deploy**. Streamlit Cloud installera automatiquement les dépendances et lancera l'application.

5. **Partager votre application**
   Une URL publique sera générée (par exemple : `https://<votre_nom>.streamlit.app`). Partagez cette URL pour permettre à d'autres d'accéder à votre application.

---

## 5. **Fonctionnalités de l'application**

- **Upload des données futures** :
  L'utilisateur peut importer un fichier CSV contenant les données climatiques futures avec les colonnes suivantes :
  - `LATITUDE`, `LONGITUDE`, `GWETTOP`, `PRECTOTCORR`, `QV2M`, `RH2M`, `T2M`, `T2M_MAX`, `T2M_RANGE`.

- **Affichage des prédictions** :
  - Les prédictions de rendement (en kg/ha) sont affichées dans un tableau avec les coordonnées géographiques (latitude, longitude).
  - Un graphique est généré pour visualiser les résultats.

---

## 6. **Dépannage**

### Problèmes communs
1. **Erreur : ModuleNotFoundError**
   - Assurez-vous que toutes les bibliothèques sont installées.
   - Vérifiez que `requirements.txt` inclut bien toutes les dépendances.

2. **Problèmes d'importation de modèles**
   - Assurez-vous que les fichiers des modèles (`sarimax_riz.pkl`, `sarimax_arachide.pkl`) sont bien dans le répertoire du projet.

3. **Erreur lors de l'upload des données futures**
   - Vérifiez que le fichier CSV contient les colonnes nécessaires.
   - Assurez-vous que les noms des colonnes correspondent exactement.

---

## 7. **Idées d'améliorations futures**

- Intégration de données saisonnières pour des prédictions plus précises.
- Optimisation des modèles avec d'autres approches (exemple : Random Forest, XGBoost).
- Génération d'une interface multilingue pour toucher un public plus large.

---

Avec ce guide, vous devriez être capable de déployer et d'utiliser votre application Streamlit sans problème. Bonne chance pour votre présentation ! 🎉

