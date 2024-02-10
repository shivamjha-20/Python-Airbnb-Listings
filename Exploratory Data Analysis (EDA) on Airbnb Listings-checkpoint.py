#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv(r'E:\studies Material\Internship Project@Coding Samurai\Airbnb\listings.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())


# In[7]:


categorical_columns = df.select_dtypes(include=['object']).columns
df[categorical_columns] = df[categorical_columns].fillna('Unknown')


# In[9]:


# Basic Statistics
# Calculate average price of listings
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
# Now calculate the mean
average_price = df['price'].mean()
print("Average Price of Listings:", average_price)


# In[11]:


property_type_distribution = df['property_type'].value_counts()
print("Distribution of Property Types:")
print(property_type_distribution)


# In[12]:


# Distribution of neighborhoods
neighborhood_distribution = df['neighbourhood'].value_counts()
print("Distribution of Neighborhoods:")
print(neighborhood_distribution)


# In[13]:


# Visualization
# Price distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=30, kde=True)
plt.title('Price Distribution of Airbnb Listings')
plt.xlabel('Price (USD)')
plt.ylabel('Frequency')
plt.show()


# In[14]:


# Property type distribution
plt.figure(figsize=(10, 6))
sns.countplot(y='property_type', data=df, order=df['property_type'].value_counts().index)
plt.title('Distribution of Property Types')
plt.xlabel('Count')
plt.ylabel('Property Type')
plt.show()


# In[15]:


# Neighborhood distribution
plt.figure(figsize=(10, 12))
sns.countplot(y='neighbourhood', data=df, order=df['neighbourhood'].value_counts().index)
plt.title('Distribution of Neighborhoods')
plt.xlabel('Count')
plt.ylabel('Neighborhood')
plt.show()


# In[16]:


# Correlation Analysis
# Identify non-numeric columns
non_numeric_columns = df.select_dtypes(exclude=['float64', 'int64']).columns


# In[17]:


# Drop non-numeric columns
df = df.drop(columns=non_numeric_columns)


# In[18]:


# Compute correlation matrix
correlation_matrix = df.corr()


# In[19]:


# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()


# In[ ]:




