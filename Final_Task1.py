#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from sklearn import preprocessing
column=['school','sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','reason','guardian','traveltime','studytime','failures','schoolsup','famsup','paid','activities','nursery','higher','internet','romantic','famrel','freetime','goout','Dalc','Walc','health','absences','G1','G2','G3']
for i in column:
    data=pd.read_excel(r'C:\Users\Hrishita\Desktop\New folder\DS_ML_FinalTask\Student-Math2.xlsx')
    b=data[i].unique()
    print(b)
    label_encoder=preprocessing.LabelEncoder()
    data[i]=label_encoder.fit_transform(data[i])
    a=data[i].unique()
    print(a)


# In[5]:


import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
data=pd.read_excel(r'C:\Users\Hrishita\Desktop\New folder\DS_ML_FinalTask\Student-Math2.xlsx')
X=data.iloc[:, :-1].values
Y=data.iloc[:, -1].values
labelencoder_X=LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
X[:,1]=labelencoder_X.fit_transform(X[:,1])
print(X)
labelencoder_Y=LabelEncoder()
Y=labelencoder_Y.fit_transform(Y)
print(Y)


# In[6]:


import pandas as pd
data=pd.read_excel(r'C:\Users\Hrishita\Desktop\New folder\DS_ML_FinalTask\Student-Math2.xlsx')
data.tail(n=400)
a=data[['G1','G2','G3']].tail(400)
print(a)
b=a.sum(axis=1)
print(b)
loc=33
column=('final grade')
value=b
data.head(400)
data.insert(loc,column,value,allow_duplicates=False)
data.head(400)


# In[7]:


import pandas as pd
import numpy as np
data=pd.read_excel(r'C:\Users\Hrishita\Desktop\New folder\DS_ML_FinalTask\Student-Math2.xlsx')
data.tail(n=400)
a=data[['G1','G2','G3']].tail(400)
print(a)
b=a.sum(axis=1)
print(b)
loc=33
column=('final grade')
value=b
data.head(400)
data.insert(loc,column,value,allow_duplicates=False)
data.head(400)
data.dropna(inplace=True)
y=pd.DataFrame(data=['final grade'])
print(y.to_numpy())


# In[14]:


import pandas as pd
data=pd.read_excel(r'C:\Users\Hrishita\Desktop\New folder\DS_ML_FinalTask\Student-Math2.xlsx')
data.tail(n=400)
a=data[['G1','G2','G3']].tail(400)
print(a)
b=a.sum(axis=1)
print(b)
loc=33
column=('final grade')
value=b
data.head(400)
data.insert(loc,column,value,allow_duplicates=False)
data.head(400)
x_cols=[x for x in data.columns if x !='G3']
x_2=data[x_cols]
print(x_2)


# In[12]:


import pandas as pd
from sklearn.model_selection import train_test_split
data=pd.read_excel(r'C:\Users\Hrishita\Desktop\New folder\DS_ML_FinalTask\Student-Math2.xlsx')
data.head(400)
X=data.iloc[:,:-1].values
Y=data.iloc[:,-1].values
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
print('X_train:\n')
print(X_train)
print(X_train.shape)
print('X_test:\n')
print(X_test)
print(X_test.shape)
print('Y_train:\n')
print(Y_train)
print(Y_train.shape)
print('Y_test:\n')
print(Y_test)
print(Y_test.shape)


# In[ ]:




