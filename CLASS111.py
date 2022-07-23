from os import stat
import pandas as pd 
import plotly.figure_factory as ff 
import statistics
import csv 
import plotly.graph_objects as go
import random 


df = pd.read_csv('medium_data.csv')
data = df["reading_time"].tolist()

def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    Mean = statistics.mean(dataSet)
    return Mean

MeanList = []
for i in range(0,1000):
    MeanSet = randomSetOfMean(100)
    MeanList.append(MeanSet)

Mean = statistics.mean(MeanList)
Std = statistics.stdev(MeanList)
print("Mean is --->{},Std is {}".format(Mean,Std))

Std1S,Std1E = Mean - Std,Mean+ Std
Std2S,Std2E = Mean - (2*Std),Mean + (2*Std)
Std3S,Std3E = Mean - (3*Std),Mean + (3*Std)

df = pd.read_csv('medium_data.csv')
data = df["reading_time"].tolist()
Mean1 = statistics.mean(data)
print("Mean of sample1 -->{}".format(Mean1))

zScore1 = (Mean - Mean1)/Std 
print("zScore is -->{}".format(zScore1))