#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# Load dataset
df = pd.read_csv('C:/Users/welcome/Downloads/archive/Electric_Vehicle_Population_Size_History_By_County_.csv')
df.head()


# In[14]:


# Check for missing values
missing_values = df.isnull().sum()
print("Missing values:\n", missing_values)

# Ensure consistency of counts
df['EV_Total_Check'] = df['Battery Electric Vehicles (BEVs)'] + df['Plug-In Hybrid Electric Vehicles (PHEVs)']
inconsistent_counts = df[df['EV_Total_Check'] != df['Electric Vehicle (EV) Total']]
print("Inconsistent counts:\n", inconsistent_counts)

# Drop the check column as it's no longer needed
df.drop(columns=['EV_Total_Check'], inplace=True)


# In[13]:


import matplotlib.pyplot as plt
import seaborn as sns

# Convert relevant columns to numeric
df['Electric Vehicle (EV) Total'] = pd.to_numeric(df['Electric Vehicle (EV) Total'], errors='coerce')
df['Total Vehicles'] = pd.to_numeric(df['Total Vehicles'], errors='coerce')

# Trend of Electric Vehicle Registrations Over Time
df['Date'] = pd.to_datetime(df['Date'])
trend_data = df.groupby('Date')['Electric Vehicle (EV) Total'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(trend_data['Date'], trend_data['Electric Vehicle (EV) Total'])
plt.title('Trend of Electric Vehicle Registrations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Electric Vehicles')
plt.show()

# Electric Vehicle Registrations by County
county_data = df.groupby('County')['Electric Vehicle (EV) Total'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(data=county_data, x='County', y='Electric Vehicle (EV) Total')
plt.title('Electric Vehicle Registrations by County')
plt.xlabel('County')
plt.ylabel('Total Electric Vehicles')
plt.xticks(rotation=90)
plt.show()

# Percentage of electric vehicles over time
df['Percent Electric Vehicles'] = (df['Electric Vehicle (EV) Total'] / df['Total Vehicles']) * 100
percent_trend_data = df.groupby('Date')['Percent Electric Vehicles'].mean().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(percent_trend_data['Date'], percent_trend_data['Percent Electric Vehicles'])
plt.title('Percentage of Electric Vehicles Over Time')
plt.xlabel('Date')
plt.ylabel('Percentage of Electric Vehicles')
plt.show()

