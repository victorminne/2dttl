import pandas as pd 
import numpy as np
import seaborn as sb 
import matplotlib as mp 
import matplotlib.pyplot as plt
from scipy.stats.mstats import winsorize
import os
import webbrowser


#import data as dataframe
data = pd.read_csv('C:\\Users\\SnRRk\\OneDrive\\Bureau\\Rka\\projets\\2DTTL-project\\2dttl\\weather_madrid.csv')
# ^ ^ ^ penser à remodif, j'ai dû mettre le path asbolu pour que ça marche et si tu vois ce commentaire, c'est que j'ai oublié de le retirer

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

data_dict = {"CET" : CET, "MeanTemp" : Mean_TemperatureC, "MinTemp" : Min_TemperatureC, "MaxTemp" : Max_TemperatureC, "MeanHum" : Mean_Humidity, "MaxHum" : Max_Humidity, "MinHum" : Min_Humidity, "MeanDew" : MeanDew_PointC,"MinDew" : Min_DewpointC, "Dew" : Dew_PointC, "CloudCover" : CloudCover, "Events" : Events}

#convert dict in dataframe 
select_data = pd.DataFrame(data = data_dict)

print(select_data.describe())





#----------------------- html part -----------------------
#convert data as an html board
html_board = data[0:50].to_html()
#wirte the html board in a file
with open("board.html", "w") as f:
    f.write(html_board)
#get the path of the file genrated
full_filename = os.path.abspath("board.html")
#launch the file in a browser
webbrowser.open(f"file://{full_filename}")

#----------------------- matplot lib -----------------------


#matplot lib graphs
data.hist(figsize=(12, 10), bins=30, edgecolor="black")
plt.subplots_adjust(hspace=0.7, wspace=0.4)
plt.show()


#------------------------------------------------------------


#Question 3.1 (0.5 point) : Quels sont les attributs numériques (quantitatifs) ?
print(data.select_dtypes(include=[float]))

#Question 3.2 (0.5 point) : Quels sont les attributs qui ne sont pas numériques (cathégoriques) ?
print(data.select_dtypes(include=[object]))

# Question 3.3 (0.5 point) : Avons-nous d'informations sur les dates ?
#pas bon, les dates c'est la galère rn mais je bosse dessus
#print(data.select_dtypes(include=[np.datetime64]))

# Question 3.4 (0.5 point) : Y a-t-il un attribut vide (NaN)? (utiliser la fonction isnull())
print(pd.isnull(data).sum())


#------------------------------------------------------------


# Question 5.1 (1 point) : Traiter les valeurs aberrantes : Corriger le(s) point(s) aberrant(s) et expliquer votre choix.
select_data = select_data - select_data.quantile(.05) - select_data.quantile(.95)

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
select_data["Events"].fillna("NoEvent", inplace=True)
#Choisissez maintenant une stratégie pour remplir toutes les valeurs numériques restantes (Temperature, Humidity, Dew, CloudCover).
# Question 5.7 (1 point) : Expliquez votre choix lorsque vous remplissez toutes les valeurs manquantes.
select_data["MeanTemp"].interpolate(method = 'linear', limit_direction = 'forward') #à défaut d'avoir une valeur pour la journée, on utilise une approximation calculée grâce à la fonction interpolate()
select_data["MeanHum"].interpolate(method = 'linear', limit_direction = 'forward') #même logique que pour MeanTemp
select_data["Dew"].interpolate(method = 'linear', limit_direction = 'forward')  #même logique que pour MeanTemp
select_data["CloudCover"].fillna(0) #Les valeurs présentes sont numériques et représentent la couverture nuageuse, une couverture nulle (NaN) peut être représentée par un 0

print(select_data)


#------------------------------------------------------------


# Question 6.1 (0.5 point) : Utilisez la fonction to_datetime() pour convertir la chaîne en une date. Utilisez la fonction dtypes pour vérifier si la conversion a été correctement effectuée.
select_data['CET'] = pd.to_datetime(select_data['CET'], infer_datetime_format=True, utc=True)
print(select_data.dtypes)

# Question 6.2 (1 point) : Ajouter un nouvel attribut "year" contenant l'année de la date sous forme d'entier (Vérifier les pandas).


# Question 6.3 (1 point) : Ajouter un nouvel attribut "day" contenant le jour de l'année [1-365].


# Question 6.4 (1 point) : Écrivez les données résultantes dans un fichier nommé weather_madrid_clean.csv.
