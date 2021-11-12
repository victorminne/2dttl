#part 1 Initialisation 

import pandas as pd 
import numpy as np
import seaborn as sb 
import matplotlib as mp 
import matplotlib.pyplot as plt
from scipy.stats.mstats import winsorize
import os
import webbrowser



#question 2.x

def display_html_p2(selected_data) : 

    html_board = selected_data[0:50].to_html()
    with open("board.html", "w") as f:
        f.write(html_board)
    full_filename = os.path.abspath("board.html")
    #get the path of the file genrated and launch the file in a browser
    webbrowser.open(f"file://{full_filename}")


def display_matplot_lib (selected_data) :

    #matplot lib graphs
    selected_data.hist(figsize=(12, 10), bins=30, edgecolor="black")
    plt.subplots_adjust(hspace=0.7, wspace=0.4)
    plt.show()


def print_questions_p3(selected_data):
    #Question 3.1 (0.5 point) : Quels sont les attributs numériques (quantitatifs) ?
    print(selected_data.select_dtypes(include=[float]))

    #Question 3.2 (0.5 point) : Quels sont les attributs qui ne sont pas numériques (cathégoriques) ?
    print(selected_data.select_dtypes(include=[object]))

    # Question 3.3 (0.5 point) : Avons-nous d'informations sur les dates ?
    #pas bon, les dates c'est la galère rn mais je bosse dessus
    #print(data.select_dtypes(include=[np.datetime64]))

    # Question 3.4 (0.5 point) : Y a-t-il un attribut vide (NaN)? (utiliser la fonction isnull())
    print(pd.isnull(data).sum())



#question 4.x

def get_data () :
        
    #import data as dataframe
    data = pd.read_csv('weather_madrid.csv')
    # ^ ^ ^ penser à remodif, j'ai dû mettre le path asbolu pour que ça marche et si tu vois ce commentaire, c'est que j'ai oublié de le retirer
    return data

# Question 4.1 (1 point) : Créer un nouveau dataFrame avec ces attributs

def select_data(data) :
    #get information queried as series to add them in dict
    CET = pd.Series(data = data["CET"])
    Mean_TemperatureC = pd.Series(data = data["Mean TemperatureC"])
    Min_TemperatureC = pd.Series(data = data["Min TemperatureC"])
    Max_TemperatureC = pd.Series(data = data["Max TemperatureC"])
    Mean_Humidity = pd.Series(data = data[" Mean Humidity"])
    Min_Humidity = pd.Series(data =  data[" Min Humidity"])
    Max_Humidity = pd.Series(data =  data["Max Humidity"])
    MeanDew_PointC = pd.Series(data =  data["MeanDew PointC"])
    Min_DewpointC = pd.Series(data =  data["Min DewpointC"])
    Dew_PointC = pd.Series(data =  data["Dew PointC"])
    CloudCover = pd.Series(data =  data[" CloudCover"])
    Events = pd.Series(data =  data[" Events"])

    # Question 4.2 (1 point) : Renommer les attributs pour les rendre plus faciles à manipuler : "date", "MeanTemp", "MinTemp", "MaxTemp", "MeanHum", "MaxHum", "MinHum", "MeanDew", "MinDew", "Dew", "CloudCover", "Events"
    data_dict = {"date" : CET, "MeanTemp" : Mean_TemperatureC, "MinTemp" : Min_TemperatureC, "MaxTemp" : Max_TemperatureC, "MeanHum" : Mean_Humidity, "MaxHum" : Max_Humidity, "MinHum" : Min_Humidity, "MeanDew" : MeanDew_PointC,"MinDew" : Min_DewpointC, "Dew" : Dew_PointC, "CloudCover" : CloudCover, "Events" : Events}

    #convert dict in dataframe 
    select_data = pd.DataFrame(data = data_dict)
    return select_data

# Question 4.3 (1 point) : Utilisez la fonction describe() pour voir les détails de vos données filtrées. Observez les informations et trouvez l'aberration.
def display_discribe_data (selected_data) :
    print(selected_data.describe())

# Question 4.4 (0,5 point) : Quel attribut présente une anomalie ?

# Question 4.5 (1 point) : Utilisez Seaborn pour tracer un boxplot de l'attribut anormal. Qu'observez-vous ? Combien y a-t-il de valeurs aberrantes ?



#questions 5.x

def print_question_p5 (selected_data) :

    # Question 5.1 (1 point) : Traiter les valeurs aberrantes : Corriger le(s) point(s) aberrant(s) et expliquer votre choix.
    selected_data = selected_data - selected_data.quantile(.05) - selected_data.quantile(.95)

    # Question 5.2 (1 point) : Avez-vous des valeurs manquantes (NaN) ? Combien de lignes ont des valeurs manquantes ?
    # voir question 3.4

    # Question 5.3 (1 point) : Que se passe-t-il si vous utilisez la fonction dropna() ?
    # C'est une fonction qui retire les colonnes ou lignes ( en fonction des arguments donnés, par défaut lignes ) contenant des valeurs manquantes

    # Question 5.4 (1 point) : Pensez-vous que c'est une bonne idée d'utiliser la fonction dropna() ? Expliquez votre réponse.
    # Cela dépend des arguments entrés; en effet, en précisant des paramètres supplémentaires, on peut ne retirer que les lignes ou colonnes contenant un nombre défini de NaN

    # Question 5.5 (1 point) : Avez-vous des valeurs manquantes pour l'attribut "Events" ? Combien ?
    #"Events" est un attribut spécial. Une valeur NaN pour un événement pourrait signifier que rien ne s'est passé ce jour-là, que c'était peut-être un jour sans pluie ou sans neige ou autre.
    # 5014, voir question 3.4

    # Question 5.6 (1 point) : Remplacez tous les événements NaN par "NoEvent" pour indiquer qu'aucun événement ne s'est produit.
    selected_data["Events"].fillna("NoEvent", inplace=True)
    #Choisissez maintenant une stratégie pour remplir toutes les valeurs numériques restantes (Temperature, Humidity, Dew, CloudCover).
    # Question 5.7 (1 point) : Expliquez votre choix lorsque vous remplissez toutes les valeurs manquantes.
    selected_data["MeanTemp"].interpolate(method = 'linear', limit_direction = 'forward') #à défaut d'avoir une valeur pour la journée, on utilise une approximation calculée grâce à la fonction interpolate()
    selected_data["MeanHum"].interpolate(method = 'linear', limit_direction = 'forward') #même logique que pour MeanTemp
    selected_data["Dew"].interpolate(method = 'linear', limit_direction = 'forward')  #même logique que pour MeanTemp
    selected_data["CloudCover"].fillna(0) #Les valeurs présentes sont numériques et représentent la couverture nuageuse, une couverture nulle (NaN) peut être représentée par un 0

    print(selected_data)



def print_question_p6 (selected_data) :

    # Question 6.1 (0.5 point) : Utilisez la fonction to_datetime() pour convertir la chaîne en une date. Utilisez la fonction dtypes pour vérifier si la conversion a été correctement effectuée.
    selected_data['CET'] = pd.to_datetime(selected_data['CET'], infer_datetime_format=True, utc=True)
    print(selected_data.dtypes)

    # Question 6.2 (1 point) : Ajouter un nouvel attribut "year" contenant l'année de la date sous forme d'entier (Vérifier les pandas).


    # Question 6.3 (1 point) : Ajouter un nouvel attribut "day" contenant le jour de l'année [1-365].


    # Question 6.4 (1 point) : Écrivez les données résultantes dans un fichier nommé weather_madrid_clean.csv.


if __name__ == "__main__":
    data = get_data()
    selected_data = select_data(data)
    display_discribe_data(selected_data)
    display_html_p2(selected_data)
    display_matplot_lib(selected_data)
    print_questions_p3(selected_data)
    print_question_p5(selected_data)
    print_question_p6(selected_data)