#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importing and Reading the dataset
df= pd.read_csv("blinkit_analysis/blinkit_data.csv")
print(df.head(20))
print(df.describe())
print(df.tail(20))
print(df.shape)
print(df.info())
print(df.isnull().sum())


# Handling duplicate data
print(df['Item Fat Content'].unique())
df["Item Fat Content"] = df["Item Fat Content"].replace({'LF' : 'Low Fat', 'low fat' : 'Low Fat', 'reg' : 'Regular', 'regular' :'Regular'})
print(df['Item Fat Content'].unique())


# Handling missing data
df.fillna({'Item Weight': df['Item Weight'].mean()}, inplace=True)


#finding business KPI

#total sales
Total_sales = df['Sales'].sum()

#Avergae sales
Avergae_sales= df['Sales'].mean()

#no of items sold 
No_of_items_sold = df['Sales'].count()

#average rating
Average_rating = df['Rating'].mean()

#displaying 
print(f"Total Sales: ${Total_sales:,.1f}")
print(f"Avergae Sales: ${Avergae_sales:,.1f}")
print(f"NO. of Items sold: {No_of_items_sold:,.1f}")
print(f"Avg. Ratings: {Average_rating:,.1f}")


# Visualizing the data
#total sales by fat content
sales_by_fat =df.groupby('Item Fat Content')['Sales'].sum()
plt.pie(sales_by_fat, labels= sales_by_fat.index, autopct='%1.1f%%', startangle=140)
plt.title('Total Sales by Item Fat Content')
plt.axis('equal')  
plt.show()

#total sales by item type
sales_by_type = df.groupby('Item Type')['Sales'].sum()
plt.bar(sales_by_type.index, sales_by_type.values)
plt.title('Total Sales by Item Type')
plt.xlabel('Item Type')
plt.ylabel('Total Sales')
plt.xticks(rotation=90)
plt.legend(title='Item Type')
plt.tight_layout()
plt.show()

#Fat content by outlet for total sales
grouped = df.groupby(['Outlet Type', 'Item Fat Content'])['Sales'].sum().unstack()
grouped = grouped[['Regular', 'Low Fat']]

ax = grouped.plot(kind='bar', stacked=False, figsize=(10, 6))
plt.xlabel('Outlet Type')
plt.ylabel('Total Sales')
plt.title('Total Sales by Outlet Type and Item Fat Content')
plt.xticks(rotation=45)
plt.legend(title='Item Fat Content')
plt.tight_layout()
plt.grid(True)
plt.show()

#total sales by outlet establishment year
sales_by_year = df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(sales_by_year.index, sales_by_year.values, marker='o', markersize=5 , linestyle='--', color='blue')
plt.title('Total Sales by Outlet Establishment Year')
plt.xlabel('Outlet Establishment Year')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Total Sales')
plt.grid(True)
plt.show()

#Sales by outlet size
sales_by_size = df.groupby('Outlet Size')['Sales'].sum()

plt.figure(figsize=(5,5))
plt.pie(sales_by_size, labels=sales_by_size.index, autopct='%1.1f%%', startangle=140)
plt.title('Total Sales by Outlet Size')
plt.axis('equal')
plt.tight_layout()
plt.legend(title='Outlet Size')
plt.show()

#sales by outlet location
sales_by_location = df.groupby('Outlet Location Type')['Sales'].sum().reset_index()
sales_b_location = sales_by_location.sort_values(by='Sales', ascending=False)

plt.figure(figsize=(8, 6))
ax = sns.barplot(x='Sales', y='Outlet Location Type', data=sales_b_location, palette='viridis')
plt.title('Total Sales by Outlet Location Type')
plt.xlabel('Total Sales')
plt.ylabel('Outlet Location Type')
plt.tight_layout()
plt.legend(title='Outlet Location Type')
plt.show()
 