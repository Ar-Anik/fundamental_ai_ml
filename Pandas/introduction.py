"""
Q : Pandas কী?
-> Pandas হলো structured/tabular data analysis এবং manipulation-এর জন্য Python library।

বিশেষ করে:
- CSV read করা
- Excel data process করা
- DataFrame তৈরি করা
- missing value handle করা
- filtering
- sorting
- grouping
- aggregation
- duplicate removal
- data type conversion
- feature transformation

ইত্যাদির জন্য Pandas ব্যবহৃত হয়।


Q : DataFrame কী?
Pandas-এর সবচেয়ে গুরুত্বপূর্ণ structure DataFrame, এটি row এবং column ভিত্তিক tabular data represent করে।

উদাহরণ:
Name    Age    Salary
A       25     50000
B       30     60000
C       28     55000
"""

import pandas as pd

df = pd.DataFrame({
    "Name": ['A', 'B', 'C'],
    "Age": [25, 30, 28],
    "Salary": [50000, 60000, 55000]
})
print(df)

"""
-> Series
একটি DataFrame-এর একটি column সাধারণত Series হিসেবে পাওয়া যায়।

df["Age"] এটি একটি Series।

- Series হলো one-dimensional labeled data structure।
- DataFrame হলো two-dimensional labeled tabular data structure, যেখানে multiple Series column হিসেবে থাকে।
"""

print(df['Age'])
print(df['Salary'])


"""
Data cleaning শুরু করার আগে dataset-এর structure বুঝতে হবে।
"""

# shape
print(df.shape)

"""
Output : (3, 3)

অর্থ:
3 rows
3 columns
"""

# Columns
print(df.columns)

# Data Types
print(df.dtypes)

# Basic Information
print(df.info())

# Statistical summary
print(df.describe())

"""
Statistical summary, Numerical columns-এর:
- count
- mean
- standard deviation
- minimum
- quartiles
- maximum
ইত্যাদি দেখা যায়।
"""

