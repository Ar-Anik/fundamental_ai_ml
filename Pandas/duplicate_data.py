import pandas as pd

data = {
    "Name": ["Rahim", "Karim", "Rahim", "Nadia", "Karim"],
    "Age": [25, 30, 25, 28, 30],
    "Salary": [40000, 50000, 40000, 45000, 50000]
}

df = pd.DataFrame(data)

print(df)

"""
এখানে:
Row 0 == Row 2
Row 1 == Row 4

অর্থাৎ একই row একাধিকবার এসেছে।
"""

# Duplicate check
print(df.duplicated())
"""
duplicated() প্রতিটি row-এর জন্য Boolean result দেয়।

False → প্রথমবার পাওয়া row
True → একই data আগে পাওয়া গেছে
"""

# How Many Duplicate Have
print(df.duplicated().sum())
"""
Output: 2 কারণ duplicate হিসেবে row 2 এবং row 4 পাওয়া গেছে।
"""


# Duplicate Data Remove
df = df.drop_duplicates()
print(df)
