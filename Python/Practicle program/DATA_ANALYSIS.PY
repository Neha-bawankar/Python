import pandas as pd

# Create DataFrames
data1 = {'ID': [1, 2, 3],
         'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35]}

data2 = {'ID': [1, 2, 4],
         'City': ['New York', 'London', 'Berlin'],
         'Salary': [70000, 80000, 90000]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge DataFrames
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print("Merged DataFrame:")
print(merged_df)

# Group data by City and calculate average Salary
grouped_df = merged_df.groupby('City')['Salary'].mean().reset_index()
print("\nAverage Salary by City:")
print(grouped_df)

# Filter data for employees with Salary > 75000
filtered_df = merged_df[merged_df['Salary'] > 75000]
print("\nFiltered DataFrame (Salary > 75000):")
print(filtered_df)

# Add a new column based on a condition
merged_df['Age Group'] = merged_df['Age'].apply(lambda x: 'Young' if x < 30 else 'Experienced')
print("\nDataFrame with Age Group:")
print(merged_df)