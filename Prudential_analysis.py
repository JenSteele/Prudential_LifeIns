from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour
import csv
import pandas as pd
import matplotlib.pyplot as plt
traindf = pd.read_csv("train.csv")
traindf.head(n=10)

#Histogram for response variables to get an idea of distribution of response
traindf.hist(column='Response', grid=False, bins=8)

#Create age bin column for age quintiles
traindf['Age_Bins']=pd.qcut(traindf['Ins_Age'], 5, labels=False)

#Plot the data for Response variables by age
axes = traindf['Response'].hist(by=traindf['Age_Bins'], bins=8, grid=False)
plt.suptitle('Risk category by age quintile')
plt.show()

#Plot the data for float variables across all ages

for i in range(1,128):
    y=traindf.iloc[:,i]
    yname = y.name
    if y.dtype == 'float64':
        traindf.boxplot(column=yname,by='Response')
        show()

#Plot the data for float variables by age

for j in range(0,5):
    traindf_age = traindf[traindf.Age_Bins == j]
    for i in range(1,128):
        y=traindf_age.iloc[:,i]
        yname=y.name + ' age bin ' + str(j)
        if y.dtype == 'float64':
            traindf_age.boxplot(column=y.name,by='Response')
            plt.title(yname)
            plt.suptitle('')
            show()
        
        















