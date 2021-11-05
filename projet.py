import pandas as pd 
import numpy as np
import seaborn as sb 
import matplotlib as mp 
import matplotlib.pyplot as plt
import os
import webbrowser


#import data as dataframe
data = pd.read_csv("weather_madrid.csv")

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
#data.hist(figsize=(12, 10), bins=30, edgecolor="black")
#plt.subplots_adjust(hspace=0.7, wspace=0.4)
#plt.show()

#------------------------------------------------------------