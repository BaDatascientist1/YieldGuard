
---

# **Prédiction des Rendements Agricoles avec Streamlit**  

Ce projet contient deux applications Streamlit, `app_ar.py` et `app_riz.py`, développées pour lancer des modèles de prédiction des rendements annuels de l’arachide et du riz. Ces applications utilisent des fichiers de test et des modèles pré-entraînés pour fournir des prédictions basées sur des facteurs climatiques.

## **Contenu du projet**  

- **`app_ar.py`** : Application Streamlit pour le modèle de prédiction du rendement de l'arachide.  
- **`app_riz.py`** : Application Streamlit pour le modèle de prédiction du rendement du riz.  
- **`fichier_test.csv`** : Un fichier CSV d'exemple pour tester les modèles.  
- **`model_arachide.pkl`** : Modèle pré-entraîné pour prédire le rendement de l'arachide.  
- **`model_riz.pkl`** : Modèle pré-entraîné pour prédire le rendement du riz.  

## **Prérequis**  

Assurez-vous d’avoir installé les dépendances nécessaires avant de lancer les applications :  
1. **Python 3.8+**  
2. Les bibliothèques Python requises (spécifiées dans un fichier `requirements.txt` si vous l'avez ajouté). Pour les installer :  
   ```bash
   pip install -r requirements.txt
   ```

## **Comment exécuter les applications ?**  

1. Clonez le dépôt sur votre machine :  
   ```bash
   git clone https://github.com/votre-utilisateur/nom-du-repo.git
   cd nom-du-repo
   ```

2. Lancez l'application pour le modèle de l'arachide :  
   ```bash
   streamlit run app_ar.py
   ```

3. Lancez l'application pour le modèle du riz :  
   ```bash
   streamlit run app_riz.py
   ```

## **Comment utiliser les applications ?**  

1. Une fois l'application lancée, elle s’ouvre dans votre navigateur.  
2. **Téléversez** un fichier CSV (comme `fichier_test.csv`) contenant les données nécessaires au modèle.  
3. Cliquez sur **Prédire** pour afficher les résultats.  

## **Structure des données d'entrée**  

Les modèles attendent des fichiers CSV avec les colonnes suivantes (à adapter si nécessaire) :  
- Exemple : `Temperature`, `Pluviométrie`, `Humidité du sol`.  

Assurez-vous que votre fichier d'entrée respecte cette structure pour des prédictions fiables.

## **Aperçu des fichiers modèles (`.pkl`)**  

Les fichiers `.pkl` contiennent les modèles entraînés pour effectuer les prédictions. Ils ont été générés à partir de données climatiques et agricoles, et ils sont chargés directement par les scripts `app_ar.py` et `app_riz.py`.

## **Contributeurs**  

- **Votre Nom**  
  *Data Scientist et Développeur des applications*  

---
