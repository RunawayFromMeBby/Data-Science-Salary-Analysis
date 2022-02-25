#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


data_science_df = pd.read_csv('resources/data_cleaned_2021.csv')


# In[20]:


data_science_df.head()


# In[10]:


#remove tensor - google_an
#look at job titles
#filter out non-entry level roles('director', 'Data scientist project manager')
#make salaires int
#figure out how to find mean for salary ranges
#filter out non-US cities
#get rid of SR postions & degree


# In[21]:


data_science_df['seniority_by_title'].unique()


# In[ ]:




