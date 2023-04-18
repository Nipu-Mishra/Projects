#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.Display Top 10 Rows of The Dataset
# 2. Check Last 10 Rows of The Dataset
# 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
# 4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
# 5. Fetch Random Sample From the Dataset (50%)
# 6.Check Null Values In The Dataset
# 7.Perform Data Cleaning [ Replace '?' with NaN ]

# 8. Drop all The Missing Values
# 9. Check For Duplicate Data and Drop Them

# 10. Get Overall Statistics About The Dataframe
# 11. Drop The Columns education-num, capital-gain, and capital-loss
# 12. What Is The Distribution of Age Column?
# 13. Find Total Number of Persons Having Age Between 17 To 48 (Inclusive) Using Between Method
# 14. What is The Distribution of Workclass Column?
# 15. How Many Persons Having Bachelors and Masters Degree?


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv(r'C:\Users\cp\Desktop\Fut_Price\adult.csv')


# In[4]:


# 1.Display Top 10 Rows of The Dataset
data.head(10)


# In[5]:


#  2. Check Last 10 Rows of The Dataset
data.tail(10)


# In[6]:


# 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print('Number of Rows',data.shape[0])
print('Number of Columns',data.shape[1])


# In[7]:


4 # Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
data.info()


# In[8]:


data


# In[9]:


# 5 Fetch Random Sample From the Dataset (50%)

data.sample(frac = 0.5)


# In[10]:


#6  Check Null Values In The Dataset

data.isna().sum()


# In[11]:


sns.heatmap(data.isna())


# In[12]:


# 7 Perform Data Cleaning [ Replace '?' with NaN ]
import numpy as np
data.isin(['?']).sum()

data['workclass'] = data['workclass'].replace('?',np.nan)
data['occupation'] = data['occupation'].replace('?',np.nan)
data['native-country'] = data['native-country'].replace('?',np.nan)

data.isin(['?']).sum()

data.isnull().sum()


# In[21]:


sns.heatmap(data.isnull())


# In[23]:


# 8  Drop all The Missing Values
per_null = data.isnull().sum()*100/len(data)
per_null


# In[26]:


data.dropna(how = 'any', inplace = True)
data.shape


# In[29]:


# 10. Get Overall Statistics About The Dataframe

data.describe()


# In[30]:


# 11. Drop The Columns education-num, capital-gain, and capital-loss

data.columns

data.drop(['educational-num','capital-gain','capital-loss'], axis = 1, inplace = True)


# In[33]:


# 12. What Is The Distribution of Age Column?

data.columns

data['age'].describe()

data['age'].hist()


# In[43]:


# 13. Find Total Number of Persons Having Age Between 17 To 48 (Inclusive) Using Between Method
sum((data['age'] >= 17) & (data['age'] <= 48))

sum(data['age'].between(17,48))


# In[47]:


# 14. What is The Distribution of Workclass Column?
data.columns
data['workclass'].describe()


# In[49]:


plt.figure(figsize = (10,10))
data['workclass'].hist()


# In[50]:


# 15. How Many Persons Having Bachelors and Masters Degree?
data.columns

filter1 = data[(data['education'] == 'Bachelors')]
filter2 = data[(data['education'] == 'Masters')]

data[(data['education'].isin(['Bachelors','Masters']))]


# In[65]:


data.columns

