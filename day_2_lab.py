#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


import numpy as np


# In[9]:


pd.set_option('display.max_columns', None)


# In[10]:


pd.set_option('display.max_rows', None)


# In[ ]:





# In[11]:


file1 = pd.read_csv('C:\\Users\\mubar\\Desktop\\GitDemo\\Day_2\\file1.csv')


# In[29]:


file1.head()


# In[35]:


#file1 = pd.DataFrame({'Customer Lifetime Value':[5]*100})


# In[36]:





# In[ ]:





# In[ ]:





# In[16]:


file1.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


column_names = file1.columns


# In[ ]:


file1 = pd.DataFrame(columns=column_names)


# In[ ]:


file1.head()


# In[ ]:





# In[ ]:


cols = []
for i in range(len(file1.columns)):
    cols.append(file1.columns[i].lower())


# In[ ]:





# In[ ]:


file1.columns = cols


# In[ ]:


file1.head()


# In[ ]:


file1 = file1[['customer', 'gender',  'education', 'income', 'vehicle class', 'monthly premium auto', 'policy type', 'total claim amount', 'customer lifetime value', 'number of open complaints']]


# In[ ]:


file1.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


file2 = pd.read_csv('C:\\Users\\mubar\\Desktop\\GitDemo\\Day_2\\file2.csv')


# In[ ]:


file2.head()


# In[ ]:


column_names = file2.columns


# In[ ]:


file2 = pd.DataFrame(columns=column_names)


# In[ ]:


file2.shape


# In[ ]:





# In[ ]:


cols = []
for i in range(len(file2.columns)):
    cols.append(file2.columns[i].lower())


# In[ ]:


#file2.columns = cols


# In[ ]:


file2.head()


# In[ ]:


#file2 = file2[['customer', 'gender', 'state', 'education', 'income', 'vehicle class', 'monthly premium auto', 'policy type', 'total claim amount', 'customer lifetime value', 'number of open complaints']]


# In[ ]:


file2.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


file3 = pd.read_csv('C:\\Users\\mubar\\Desktop\\GitDemo\\Day_2\\file3.csv')


# In[ ]:


file3.head()


# In[ ]:





# In[ ]:


column_names = file3.columns


# In[ ]:


file3 = pd.DataFrame(columns=column_names)


# In[ ]:


file3.shape


# In[ ]:





# In[ ]:


cols = []
for i in range(len(file3.columns)):
    cols.append(file3.columns[i].lower())


# In[ ]:


file3.columns = cols


# In[ ]:


#pd.DataFrame()


# In[ ]:


file3 = file3[['customer', 'gender', 'state', 'education', 'income', 'vehicle class', 'monthly premium auto', 'policy type', 'total claim amount', 'customer lifetime value', 'number of open complaints']]


# In[ ]:


file3


# In[ ]:





# In[ ]:


file1 = pd.DataFrame(columns=column_names)


# In[ ]:


#file1.head()


# In[ ]:


file1 = pd.concat([file1,file2,file3], axis=0)


# In[ ]:


file1.head()


# In[ ]:


#file1.shape


# In[ ]:


file1.dtypes


# In[ ]:


file1._get_numeric_data()


# In[ ]:





# In[ ]:


file1 = pd.DataFrame(columns=column_names)


# In[ ]:


#file1 = file1.drop(['education','number of open complaints', ], axis =1)


# In[ ]:


file1.head()


# In[ ]:


file1.shape


# In[ ]:


columns=column_names


# In[ ]:


column_names


# In[ ]:





# In[ ]:


data = file1.rename(columns={ 'Education':'education','Customer Lifetime Value':'customer lifetime value', 'Number of Open Complaints':'number of open complaints', 'Total Claim Amount':'total claim amount', 'Monthly Premium Auto':'monthly premium auto', 'Vehicle Class':'vehicle class',})


# In[ ]:


file1.head()


# In[ ]:





# In[ ]:


#data= file1.drop(['customer lifetime value', 'customer', 'state', 'gender', 'income', 'monthly premium auto', 'policy type', 'total claim amount', 'vehicle class'], axis = 1)


# In[ ]:


file1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




