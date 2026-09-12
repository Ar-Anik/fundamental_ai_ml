import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, np.nan, 30],
    'Salary': [50000, 60000, np.nan],
    'Department': ['IT', 'HR', np.nan]
})

print(df)

"""
এখানে NaN হলো missing value। বাস্তব dataset-এ missing value খুব common।
"""

# check column wise total NaN value
print(df.isnull().sum())

# check column wise total NaN value
print(df.isna().sum())


"""
Missing Value handle করার কোনো fixed rule নেই। Data এবং business meaning-এর ওপর decision depend করে।
"""

# Drop Rows
drop_nan = df.dropna()
print(drop_nan)
"""
এতে যেসব row-তে missing value আছে, ঐ row বাদ যাবে।
"""

# Mean দিয়ে fill
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)
"""
এখানে Age-এর missing value mean age দিয়ে fill হবে।
"""


# Median দিয়ে fill
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
print(df)
"""
এখানে Salary-এর missing value median salary দিয়ে fill হবে।
"""
