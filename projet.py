import pandas as pd 
import numpy as np
import seaborn as sb 
import matplotlib as mp 
import os
import webbrowser


#import data as dataframe
data = pd.read_csv("weather_madrid.csv")


#html part 
html = data[0:50].to_html()
with open("data.html", "w") as f:
    f.write(html)
full_filename = os.path.abspath("data.html")
webbrowser.open(f"file://{full_filename}")