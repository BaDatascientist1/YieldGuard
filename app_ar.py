import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Charger le modèle
with open("modele_arachide.pkl", "rb") as file:
    sarimax_arachide = pickle.load(file)

# Interface utilisateur
st.title("Prédiction du rendement de l'arachide")
st.write("Modèle SARIMAX basé sur les facteurs climatiques.")

# Entrées de l'utilisateur
annees_a_predire = st.number_input("Nombre d'années à prédire", min_value=1, value=5)
facteurs_climatiques = st.file_uploader("Téléchargez un fichier CSV contenant les facteurs climatiques pour les années futures", type=["csv"])

if facteurs_climatiques:
    # Charger les données des facteurs climatiques
    future_exog = pd.read_csv(facteurs_climatiques)
    st.write("Données des facteurs climatiques chargées :")
    st.dataframe(future_exog.head())

    # Prédictions
    try:
        predictions = sarimax_arachide.get_forecast(steps=annees_a_predire, exog=future_exog)
        predicted_values = predictions.predicted_mean
        st.write("Prédictions des rendements :")
        st.dataframe(predicted_values)

        # Graphique
        st.line_chart(predicted_values)

    except Exception as e:
        st.error(f"Erreur lors de la prédiction : {e}")
else:
    st.warning("Veuillez charger un fichier CSV pour effectuer des prédictions.")
