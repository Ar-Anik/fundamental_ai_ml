"""
বাস্তব project-এ dummy dictionary-এর চেয়ে CSV load করা বেশি practical।
"""

import pandas as pd

df = pd.read_csv('employees.csv')

print(df.head())

"""
প্রথম পাঁচটি row দেখা যায়।
"""
