import pandas as pd 
import numpy as np
import seaborn as sb 
import matplotlib as mp 
import matplotlib.pyplot as plt
import os
import webbrowser
import scipy.stats.mstats as sci

def get_data (filename = str) : 
    data = pd.read_csv(filename)
    data = select_data(data)
    return data

def select_data (data):
    #regarder pd.DataFrame.drop()
    #regarder pd.DataFrame.rename()
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
    select_data = pd.DataFrame(data = data_dict)

    return select_data

def data_describe_display (data) :
    print(data.describe())


def html_display () :

    #convert data as an html board
    html_board = data[0:50].to_html()
    with open("board.html", "w") as f:
        f.write(html_board)
    full_filename = os.path.abspath("board.html")
    webbrowser.open(f"file://{full_filename}")
    #get the path of the file genrated and launch in browser
    


def matplot_display (data) : 

    data.hist(figsize=(12, 10), bins=30, edgecolor="black")
    plt.subplots_adjust(hspace=0.7, wspace=0.4)
    plt.show()



if __name__ == "__main__":
    filename = input("what is the name of the file with the extension ?")
    data = get_data(filename)
    html_display()
    matplot_display(data)
    data_describe_display(data)