from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
traindf = pd.read_csv("train.csv")
descrip = traindf.describe()

Categorical = ['Product_Info_1', 'Product_Info_2', 'Product_Info_3', 'Product_Info_5', 
'Product_Info_6', 'Product_Info_7', 'Employment_Info_2', 'Employment_Info_3', 
'Employment_Info_5', 'InsuredInfo_1', 'InsuredInfo_2', 'InsuredInfo_3', 'InsuredInfo_4', 
'InsuredInfo_5', 'InsuredInfo_6', 'InsuredInfo_7', 'Insurance_History_1', 
'Insurance_History_2', 'Insurance_History_3', 'Insurance_History_4', 
'Insurance_History_7', 'Insurance_History_8', 'Insurance_History_9', 'Family_Hist_1', 
'Medical_History_2', 'Medical_History_3', 'Medical_History_4', 'Medical_History_5', 
'Medical_History_6', 'Medical_History_7', 'Medical_History_8', 'Medical_History_9', 
'Medical_History_11', 'Medical_History_12', 'Medical_History_13', 'Medical_History_14', 
'Medical_History_16', 'Medical_History_17', 'Medical_History_18', 'Medical_History_19', 
'Medical_History_20', 'Medical_History_21', 'Medical_History_22', 'Medical_History_23', 
'Medical_History_25', 'Medical_History_26', 'Medical_History_27', 'Medical_History_28',
'Medical_History_29', 'Medical_History_30', 'Medical_History_31', 'Medical_History_33', 
'Medical_History_34', 'Medical_History_35', 'Medical_History_36', 'Medical_History_37', 
'Medical_History_38', 'Medical_History_39', 'Medical_History_40', 'Medical_History_41']

Continuous = ['Product_Info_4', 'Ins_Age', 'Ht', 'Wt', 'BMI', 'Employment_Info_1', 
'Employment_Info_4', 'Employment_Info_6', 'Insurance_History_5', 'Family_Hist_2', 
'Family_Hist_3', 'Family_Hist_4', 'Family_Hist_5']

Discrete = ['Medical_History_1', 'Medical_History_10', 'Medical_History_15', 
'Medical_History_24', 'Medical_History_32']
Cate = traindf[Categorical].copy()
Cont = traindf[Continuous].copy()
Disc = traindf[Discrete].copy()


lower_trunc = []
upper_trunc = []
Cont.is_copy = False        
for i in Continuous:
    y=traindf[i]
    name = y.name
    if y.dtype == 'float64':
        if descrip[name]['75%'] == descrip[name]['max']:
            upper_trunc.append(name)
            print upper_trunc + 'upper truncated'
        if descrip[name]['min'] == descrip[name]['25%']:
            lower_trunc.append(name)
            print name + ' lower truncated'

for i in Cont:
    if Cont[i].mean != 0:
        Cont[i] -= Cont[i].mean()
    if Cont[i].std != 1:
        Cont[i] /= Cont[i].std()

        
for i in Continuous:
    y=traindf[i]
    name = y.name
    if y.dtype == 'float64':
        if descrip[name]['75%'] == descrip[name]['max']:
            upper_trunc.append(name)
            print upper_trunc + 'upper truncated'
        if descrip[name]['min'] == descrip[name]['25%']:
            lower_trunc.append(name)
            print name + ' lower truncated'

count = []
for i in lower_trunc:
    median = descrip[i]['50%']
    nname = i + '_d'
    Cont[nname] = 0
    Cont[nname][Cont[i]>median] = 1
    Cont[nname][Cont[i].isnull()] = None

#Categorical Variables - make into dummy variables ensuring n-1 categories:
Categorical_dummies = pd.DataFrame(index=Cate.index)
low_count = {}
for i in Categorical:
    test1 = pd.get_dummies(Cate[i],prefix=i)
    dummy_count = test1.sum()
    for j in range(len(dummy_count)):
        if dummy_count[j]<100:
            print 'Note:  Low dummy count of ' + str(int(dummy_count[j])) + ' for ' + str(test1.columns[j])
            low_count[test1.columns[j]] = int(dummy_count[j])
    Categorical_dummies = pd.concat([Categorical_dummies,test1],axis=1)

#Combine continuous, categorical and discrete variables into one dataset:
Cleaner_Data = pd.concat([Cont,Categorical_dummies,Disc], axis = 1)
