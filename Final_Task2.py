#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
from sklearn import utils
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\Hrishita\Desktop\New folder\DS_ML_FinalTask\Student-Math2.xlsx')

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

df['school']= le.fit_transform(df['school'])
df['Pstatus']= le.fit_transform(df['Pstatus'])
df['sex']= le.fit_transform(df['sex'])
df['address']= le.fit_transform(df['address'])
df['famsize']= le.fit_transform(df['famsize'])
df['Mjob']= le.fit_transform(df['Mjob'])
df['Fjob']= le.fit_transform(df['Fjob'])
df['reason']= le.fit_transform(df['reason'])
df['guardian']= le.fit_transform(df['guardian'])
df['schoolsup']= le.fit_transform(df['schoolsup'])
df['famsup']= le.fit_transform(df['famsup'])
df['paid']= le.fit_transform(df['paid'])
df['activities']= le.fit_transform(df['activities'])
df['nursery']= le.fit_transform(df['nursery'])
df['higher']= le.fit_transform(df['higher'])
df['internet']= le.fit_transform(df['internet'])
df['romantic']= le.fit_transform(df['romantic'])

col = df.loc[: , "G1":"G3"]
df['final_grade'] = col.mean(axis=1)

df.to_excel(r'C:\Users\Hrishita\Desktop\New folder\DS_ML_FinalTask\final_student-math.xlsx')

y = df['final_grade'].to_numpy()

col = df.loc[:,"school":"G2"]
x = col.to_numpy()

def predict(x):
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test = train_test_split(x,y)

    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()
    reg.fit(x_train,y_train)
    
    prediction = reg.predict(x_test)
    
    from sklearn.metrics import r2_score
    accuracy = r2_score(y_test, prediction)
    print("Accuracy = ",accuracy*100, "%")
    
    plt.scatter(y_test, prediction, color = 'b')
    plt.xlabel('True Value --->')
    plt.ylabel('Predicted Value --->')
    plt.show()

import statsmodels.api as sm
def bkwdelm(x,sl):
    numvars = len(x[0])
    for i in range(0,numvars):
        reg_OLS = sm.OLS(y,x).fit()
        maxvar = max(reg_OLS.pvalues).astype(float)
        if maxvar > sl:
           for j in range(0,numvars-i):
               if (reg_OLS.pvalues[j].astype(float) == maxvar):
                  x = np.delete(x,j,1)
    print(reg_OLS.summary())
    return x
    
sl = 0.005
x_opt = x[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]]
x_modeled = bkwdelm(x_opt, sl)

predict(x_modeled)


# In[ ]:




