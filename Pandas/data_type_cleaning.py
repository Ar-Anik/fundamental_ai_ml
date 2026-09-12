import pandas as pd

data = {
    "Name": ["Rahim", "Karim", "Nadia", "Hasan"],
    "Salary": ["50000", "60000", "70000", "80000"]
}

df = pd.DataFrame(data)
print(df)

"""
Output:
    Name  Salary
0  Rahim   50000
1  Karim   60000
2  Nadia   70000
3  Hasan   80000

দেখতে number-এর মতো হলেও Salary বর্তমানে string/object হিসেবে থাকতে পারে।
"""

print(df.dtypes)
"""
Salary numerical type নয়।
"""

# String থেকে numeric
df['Salary'] = pd.to_numeric(
    df['Salary'],
    errors='coerce'
)
print(df.dtypes)


# why use errors='coerce'
"""
ধরা যাক data-তে একটি invalid value আছে:

data = {
    "Name": ["Rahim", "Karim", "Nadia", "Hasan"],
    "Salary": ["50000", "60000", "ABC", "80000"]
}

df = pd.DataFrame(data)
print(df)

এখন:
    Name  Salary
0  Rahim   50000
1  Karim   60000
2  Nadia     ABC
3  Hasan   80000

ABC numeric value নয়।

এখন:
df["Salary"] = pd.to_numeric(
    df["Salary"],
    errors="coerce"
)

Output:
    Name   Salary
0  Rahim  50000.0
1  Karim  60000.0
2  Nadia      NaN
3  Hasan  80000.0

ABC convert করা যায়নি, তাই NaN হয়েছে।
"""
