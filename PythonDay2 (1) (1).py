#!/usr/bin/env python
# coding: utf-8

# In[1]:


# read data and do prediction

#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model #for creating ml model
#from sklearn.datasets import load_boston
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[49]:


data1=pd.read_csv(r"C:\Users\VIDUSHIG\Downloads\insurance_py.csv")
type(data1)
print(data1.head())
print(data1.shape)


# In[50]:


ind_var1=data1.iloc[:,1:-1]
ind_var1.head()
print(ind_var1.shape)


# In[51]:


type(ind_var1)


# In[52]:


dep_var1=data1.iloc[:,7]
dep_var1.head()


# In[53]:


type(dep_var1)


# In[54]:


test1=pd.read_csv(r"C:\Users\VIDUSHIG\Downloads\insurance_test.csv")
#test1=test1.iloc[1:,:]
type(test1)
print(test1)


# In[55]:


from sklearn import linear_model
model1=linear_model.LinearRegression()
model1.fit(ind_var1, dep_var1)


# In[56]:


result1=model1.predict(test1)
print(result1)
type(result1)


# In[ ]:


result2=()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




