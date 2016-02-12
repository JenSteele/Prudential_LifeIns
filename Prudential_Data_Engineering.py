from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour
import csv
import pandas as pd
import matplotlib.pyplot as plt
traindf = pd.read_csv("train.csv")
traindf.head(n=10)

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




#Starting with continuous variables, check for truncation and if truncated re-name as discrete variable 
#with oldname_t = 1 if variable is greater than mean, and oldname_t = 0 if variable is <= mean
lower_trunc=[]
upper_trunc=[]
Cont = traindf[Continuous]
        
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


for i in lower_trunc:
    mean = descrip[i]['mean']
    nname = i + '_d'
    Cont[nname] = 0
    print i
    for j in range(0,len(Cont[i])):
        if Cont[i][j] > mean:
            Cont[nname][j] = 1
        print j    

#For categorical variables, determine the number of categories for each variable, 
#and create a dummy column for each variable category (except for the last category)

#Cat = traindf[Categorical]

for i in Categorical[4:8]:
    Cat[i] = traindf[i]
    name=Cat[i].name
    Cat_label = Cat[name].unique()    
    for j in range(0,len(Cat_label)-1):
        Cat_clabel = name + '_c' + str(Cat_label[j])
        Cat[Cat_clabel] = 0
        print Cat_clabel
        for k in range(0,len(Cat[i])):
            if Cat[i][k] == Cat_label[j]:
                Cat[Cat_clabel][k] = 1       

