import pandas as pd
data = {
    "Name": ["Rahim", "Karim", "Nadia", "Hasan", "Sadia"],
    "Department": ["IT", "HR", "Finance", "IT", "HR"]
}

df = pd.DataFrame(data)

print(df)

"""
Output:
    Name Department
0  Rahim         IT
1  Karim         HR
2  Nadia    Finance
3  Hasan         IT
4  Sadia         HR

Department একটি categorical feature।

এর possible categories:
IT
HR
Finance

Machine Learning model সাধারণত এই raw text category সরাসরি numerical calculation-এর জন্য ব্যবহার করে না।
তাই category-কে numerical representation-এ convert করতে হয়।
"""

"""
-> One-Hot Encoding
One-Hot Encoding হলো categorical data-কে numerical representation-এ convert করার একটি technique।

Conceptually:

Department
IT
HR
Finance

এগুলোকে এমনভাবে represent করা যায়:
Department_IT
Department_HR
Department_Finance

যেমন:
Department   IT   HR   Finance
IT           1    0    0
HR           0    1    0
Finance      0    0    1
IT           1    0    0
HR           0    1    0

Pandas দিয়ে numerical representation-এ convert :
"""
encoded_df = pd.get_dummies(df, columns=['Department'])
print(encoded_df)

"""
Output-এর structure হবে:

    Name  Department_Finance  Department_HR  Department_IT
0  Rahim                   0              0              1
1  Karim                   0              1              0
2  Nadia                   1              0              0
3  Hasan                   0              0              1
4  Sadia                   0              1              0

এখানে:
IT      → 0 0 1
HR      → 0 1 0
Finance → 1 0 0

প্রতিটি category-এর জন্য একটি আলাদা binary column তৈরি হয়েছে।
"""

