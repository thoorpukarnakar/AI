#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


data = pd.read_csv("../Wine_quality/winequality-red.csv",delimiter = ';')


# In[5]:


data.head()


# In[10]:


data.iloc[3:10,0]


# In[11]:


data.iloc[1]


# In[21]:


print(data.loc[:3,['fixed acidity']])
print(data.loc[:3,['fixed acidity','chlorides']])


# In[15]:


data.groupby(['quality'])['sulphates'].count()
data.groupby(['quality'])['sulphates'].mean()


# In[22]:


data['sulphates'].fillna(data['sulphates'].mean(),inplace=True)


# In[ ]:


data['quality'] = data['quality'].map({'low':1,'medium':5,'high':10})

