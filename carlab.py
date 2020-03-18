import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#csv2012 = pd.read_csv("./2012.csv", sep=",")
#csv2013 = pd.read_csv("./2013.csv", sep=",")
#csv2014 = pd.read_csv("./2014.csv", sep=",")
csv2015 = pd.read_csv("./2015.csv" , sep=",")

var2015 = csv2015.shape
print(var2015)
