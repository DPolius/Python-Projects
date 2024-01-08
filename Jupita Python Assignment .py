
##### PART 1: DATA IMPORTATION

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

# Browse through dataset 
df.head()

# General overview of dataset info
df.info()

# NOTE: no null values in the dataset

#Summary statistics for columns
df.describe()

# #### PART 3: DATA CLEANING

# Check for duplicates 
df[df.duplicated()] 
# No Duplicate values

# Check for missing values 
df.isnull().sum()

# There are no missing values

# The rating column data type must be converted to a numerical data type. Currently is classified as an object due to the "NOT given" values.

df['rating'].unique()

# Delete rows that have the rating of 'Not given'
df.drop(df.index[df['rating'] == 'Not given'], inplace = True)

#Confirm that 'Not given' values were dropped
df['rating'].unique()

# Convert the rating column to integer data type 
df['rating'] = df['rating'].astype('int64')

#Confirm the change 
df.describe()

# NOTE: The rating column is now included in the summary statistics and can be referenced in the data analysis. 

##### PART 4: DATA ANALYSIS

# Question 1: What is the average cost of orders in the dataset?

df['cost_of_the_order'].mean()
# Answer: Average cost per order is $16.76

# Question 2: Which restaurant has the highest average cost per order?

highest = df.groupby('restaurant_name')['cost_of_the_order'].mean().sort_values(ascending = False)

# Use head() to call only the highest result
highest.head(1)
# Ramen house has the highest averag cost per order at $32.93

# Question 3: What is the distribution of cuisine types?

cuisine = df['cuisine_type'].unique()
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

order_days = df.groupby('day_of_the_week')['order_id'].sum().sort_values(ascending = False)
print(order_days)

# create labels for pie chart 
day_labels = df['day_of_the_week'].unique()

# visualize with pie chart 

plt.figure(figsize = (6,6))
plt.pie(order_days, labels = day_labels)


# Order are placed more on weekdays.

# Question 5: What restaurants have an average rating of 5?

rest_rating = df.groupby('restaurant_name')['rating'].mean().sort_values(ascending = False)

# Identify restaurants with average rating of 5 
high_rated = rest_rating[rest_rating == 5]

print(high_rated)

# Question 6: Which cuisine type has the highest average rating

cuisine_rating = df.groupby('cuisine_type')['rating'].mean().sort_values(ascending = False)
print(cuisine_rating)

# Answer: Mexian food has the highest average rating of 4.833.

#### Temporal Anaylsis 

# Question 1: How does the distribution of food preparation times look across different cuisine types?


# Average prep time for each cuisine
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


mean_delivery_time = df.groupby('day_of_the_week')['delivery_time'].mean()
print(mean_delivery_time)

# Answer: Weekend mean delivery time is 22.43 mins while weekday delivery time is 28.30 mins

# Question 3: How does the rating vary for different cuisine types?


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

mean_prep_time = df.groupby('day_of_the_week')['food_preparation_time'].mean()


# Answer: Based on the above analysis there is no substantial change in prep time between weekdays and weekends. However average delivery time is about 6 minutes longer on weekdays when compared to weekends. This could be due to the heavier traffic during the week due to workers commuting. 
