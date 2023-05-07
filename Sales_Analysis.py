#!/usr/bin/env python
# coding: utf-8

# ## Importing the Libraries

# In[87]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# ## upload the csv file using pdf
# 

# In[88]:


df = pd.read_excel(r"C:\Users\SAROJ\Desktop\Python_Diwali_Sales_Analysis\Diwali_sales.csv.xlsx")
df


# ## Exploring the dataset

# ### check for head and tail
# 

# In[89]:


df.head()


# In[90]:


df.tail()


# from here we see that the last two columnghs have literally null values throught

# ### check the shape of the dataset

# In[91]:


df.shape


# ### analysing the status column

# In[92]:


value_counts1 = df['Status'].value_counts()
value_counts2 = df['unnamed1'].value_counts()

value_counts1
value_counts2


# ## Data Wrangling

# In[93]:


### removing the uncessary column
df = df.drop('Status', axis=1)
df = df.drop('unnamed1', axis=1)
df.head()


# ### checking for the null values and removing them

# In[94]:


df.isnull().sum()


# In[95]:


#we remove the null value rows
df = df.dropna()
df.shape


# ### analyzing the data once

# In[96]:


df.info()


# In[97]:


df.describe()


# ## Exploratory data analysis

# In[98]:


df.columns


# ### Gender Analysis

# In[99]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[101]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

# Annotate the values on the bars
for index, row in sales_gen.iterrows():
    plt.annotate(row['Amount'], xy=(row.name, row['Amount']), ha='center', va='bottom')
    
# Show the plot
plt.show()


# From the above two charts, we notice that majority of the buyers are female and also their purchasing power is more

# ### Age Wise Analysis

# In[102]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[103]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# ### State Wise Analysis
# 

# In[105]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[106]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# ### Occupation Wise Analysis

# In[107]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[108]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# ### Product Wise Analysis

# In[110]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[111]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# 
# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category but huge amount is spent on food as compared to other categories

# ### Martial Status Analysis

# In[113]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(5,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[114]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# ## Conclusion

# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




