#!/usr/bin/env python
# coding: utf-8

# ### PYTHON DATA ANALYSIS ASSIGNMENT

# #### PART 1: DATA IMPORTATION

# In[5]:


# Importing necessary packages 

import pandas as pd 
import numpy as np
import  matplotlib.pyplot as plt

# Inline matplotlib visuals
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


# Load the dataset    
df = pd.read_csv(r"C:\Users\dtori\Downloads\archive (3)\food_order.csv")


# #### PART 2: DATA EXPLORATION 

# In[7]:


# Browse through dataset 
df.head()


# In[8]:


# General overview of dataset info
df.info()


# NOTE: There appears to be no null values in the dataset

# In[9]:


#Check summary statistics for columns
df.describe()


# #### PART 3: DATA CLEANING

# In[10]:


# Check for duplicates 
df[df.duplicated()] 


# NOTE: Dataset does not contain any duplicate values. 

# In[11]:


# Check for missing values 
df.isnull().sum()


# NOTE: Confirmation that there are no missing values in any columns

# The rating column data type must be converted to a numerical data type. Currently is classified as on object due to the "NOT given" values.

# In[12]:


# Check the unique values of the rating column 
df['rating'].unique()


# In[13]:


# Delete rows that have the rating of 'Not given'
df.drop(df.index[df['rating'] == 'Not given'], inplace = True)


# In[14]:


#Confirm that 'Not given' values were dropped
df['rating'].unique()


# In[15]:


# Convert the rating column to integer data type 
df['rating'] = df['rating'].astype('int64')


# In[16]:


#Confirm the change 
df.describe()


# NOTE: The rating column is now included in the summary statistics and can be referenced in the data analysis. 

# #### PART 4: DATA ANALYSIS
# #### Answering the Business Questions

# Question 1: What is the average cost of orders in the dataset?

# In[17]:


# Use means function 
df['cost_of_the_order'].mean()


# Answer: Average cost per order is $16.76

# Question 2: Which restaurant has the highest average cost per order?

# In[18]:


# Group data by restaurant name, and find the mean of order cost and sort the values in descending order.
highest = df.groupby('restaurant_name')['cost_of_the_order'].mean().sort_values(ascending = False)

# Use head() to call only the highest result

highest.head(1)


# Ramen house has the highest averag cost per order at $32.93

# Question 3: What is the distribution of cuisine types?

# In[19]:


# List of cuisines types
cuisine = df['cuisine_type'].unique()

# List of cuisine type count 
count_cuisine = df['cuisine_type'].value_counts()

#Creat bar chart 
plt.figure(figsize = (15,8))
plt.bar(cuisine, count_cuisine, color = 'blue', width = 0.6, align = 'center')
plt.xticks(color = 'black')
plt.title('DISTRIBUTION OF CUISINE TYPES', color = 'black')
plt.xlabel('Cuisine', color = 'black')
plt.ylabel('Count', color = 'black')
plt.show


# Question 4: Are orders more frequently placed on weekdays or weekends?

# In[20]:


# Group by days of the week and count the number of orders
order_days = df.groupby('day_of_the_week')['order_id'].sum().sort_values(ascending = False)
print(order_days)

# create labels for pie chart 
day_labels = df['day_of_the_week'].unique()

# visualize with pie chart 

plt.figure(figsize = (6,6))
plt.pie(order_days, labels = day_labels)


# Order are placed more on weekdays.

# Question 5: What restaurants have an average rating of 5?

# In[21]:


# group by restaurants and find average rating 
rest_rating = df.groupby('restaurant_name')['rating'].mean().sort_values(ascending = False)

# Identify restaurants with average rating of 5 
high_rated = rest_rating[rest_rating == 5]

print(high_rated)


# Question 6: Which cuisine type has the highest average rating

# In[22]:


# Group by cuisine type and find the average rating for each 

cuisine_rating = df.groupby('cuisine_type')['rating'].mean().sort_values(ascending = False)
print(cuisine_rating)


# Answer: Mexian food has the highest average rating of 4.833.

# ### Temporal Anaylsis 

# Question 1: How does the distribution of food preparation times look across different cuisine types?

# In[23]:


# Calculate average prep time for each cuisine type
cuisine_prep = df.groupby('cuisine_type')['food_preparation_time'].mean().sort_values()

# List of cuisine types
cuisine = df['cuisine_type'].unique()


#Creat bar chart 
plt.figure(figsize = (20,8))
plt.bar(cuisine, cuisine_prep, color = 'blue', width = 0.6, align = 'center')
plt.xticks(color = 'black')
plt.title('DISTRIBUTION OF PREPARATION TIME ACROSS CUISINES', color = 'black')
plt.xlabel('Cuisine', color = 'black')
plt.ylabel('Prep Time', color = 'black')
plt.show


# Question 2: What is the average delivery time for orders placed on weekends versus weekdays?

# In[24]:


# Group by day of the week and find the mean delivery time 

mean_delivery_time = df.groupby('day_of_the_week')['delivery_time'].mean()

print(mean_delivery_time)


# Answer: Weekend mean delivery time is 22.43 mins while weekday deilvery time is 28.30 mins

# Question 3: How does the rating vary for different cuisine types?

# In[25]:


ratings = df.groupby('cuisine_type')['rating'].mean().sort_values()

#Create bar chart 
plt.figure(figsize = (20,8))
plt.bar(ratings.index, ratings, color = 'blue', width = 0.6, align = 'center')
plt.xticks(color = 'black')
plt.title('AVERAGE RATINGS ACROSS CUISINES', color = 'black')
plt.xlabel('Cuisine', color = 'black')
plt.ylabel('Rating', color = 'black')
plt.show


# Question 4: Can we identify any trends in food preparation times and delivery times over the dataset's timeline?
#  

# In[26]:


# Group by day of the week and find mean of preptime 

mean_prep_time = df.groupby('day_of_the_week')['food_preparation_time'].mean()

mean_prep_time


# Answer : Based on the above analysis there is no substantial change in prep time between weekdays and weekends. However average delivery times is about 6 minutes longer on weekdays when compared to weekends. This could be due to the heavier traffic during the week due to workers commuting. 
