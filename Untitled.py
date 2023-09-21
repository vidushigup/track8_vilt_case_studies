#!/usr/bin/env python
# coding: utf-8

# In[1]:


4+8


# In[2]:


print("hello world")


# In[3]:


print(2)


# In[4]:


var1 = 10
var2 =10.2
var3 ="testing"
print(type(var1))
print(type(var2))
print(type(var3))


# In[5]:


var4 ='testing'
print(type(var4))


# In[6]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
type(var1)
type(var2)
type(var3)


# In[7]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[8]:


type(var1)
type(var2)
type(var3)


# In[9]:


sales1=[9914, 40487,54324,50044,34719,42551,94871,118914,158484,131348,78504,36284]
spend1=[1000, 4000,5000,4500,3000,4000,9000,11000,15000,12000,7000,3000]


# In[10]:


from matplotlib import pyplot as plt


# In[11]:


plt.bar(sales1,spend1)


# In[12]:


x=[1,2,3,4,5,6,7,8,9,10,11,12]
plt.bar(x,sales1)


# In[13]:


plt.bar(x,spend1)


# In[15]:


import pandas as pd
spend1_df=pd.DataFrame(spend1,columns=["spend1"])
sales1_df=pd.DataFrame(sales1,columns=["sales1"])
test1=pd.DataFrame([2500])


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import model_selection
from sklearn import linear_model


# In[3]:


sales1=[9914, 40487,54324,50044,34719,42551,94871,118914,158484,131348]#,78504,36284]
spend1=[1000, 4000,5000,4500,3000,4000,9000,11000,15000,12000]#,7000,3000]


# In[8]:


spend1_df=pd.DataFrame(spend1,columns=["spend1"])
sales1_df=pd.DataFrame(sales1,columns=["sales1"])
test1=pd.DataFrame([12000])
type(spend1_df)


# In[9]:


from sklearn import linear_model
model1=linear_model.LinearRegression()
model1.fit(spend1_df,sales1_df)
result1=model1.predict(test1)
print(result1)


# In[10]:


type(result1)


# In[12]:


test2=pd.DataFrame([15000])
result2=model1.predict(test2)
print(result2)


# In[ ]:




