#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
df = pd.read_csv('data.csv')


# In[15]:


X = df[['date','first','second','third']]
y = df[['peak_load(MW)']]
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)
linreg = LinearRegression()
linreg.fit(X, y)


# In[16]:


Ddate = [20190402,20190403,20190404,20190405,20190406,20190407,20190408]
First = [30560,30560,28140,27060,26970,26930,30600]
Second = [1860,1960,2440,2460,2670,2430,2100]
Third = [6.48,6.85,9.48,9.98,10.98,9.9,7.37]
Ddict = {
    "date" : Ddate,
    "first" : First,
    "second" : Second,
    "third" : Third
}
Ddict_df = pd.DataFrame(Ddict)
y_pred = linreg.predict(Ddict_df)

import csv
with open('submission.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['date', 'peak_load(MW)'])
    for i in range(0,7):
        writer.writerow([Ddate[i],y_pred[i][0]])
y_pred


# In[ ]:




