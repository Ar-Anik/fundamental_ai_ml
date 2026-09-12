"""
Q : NumPy কী?

NumPy = Numerical Python

NumPy হলো Python-এর একটি fundamental numerical computing library, যা মূলত:
- numerical array
- vector
- matrix
- mathematical operation
- statistical operation
- linear algebra
- random number generation
ইত্যাদির জন্য ব্যবহৃত হয়।

AI/ML ecosystem-এ NumPy গুরুত্বপূর্ণ কারণ Machine Learning-এর data শেষ পর্যন্ত numerical representation-এ আসে।

উদাহরণ:
ধরা যাক একটি employee-এর data:
Age = 25
Salary = 50000
Experience = 3

এগুলোকে numerical vector হিসেবে represent করা যায়:
"""

ar = [25, 50000, 3]

import numpy as np

x = np.array(ar)

print(x)

"""
এখানে x একটি NumPy ndarray।
"""

"""
-> NumPy Array

NumPy-এর প্রধান data structure হলো numpy.ndarray, উদাহরণ:
"""
x = np.array([10, 20, 30, 40])
"""
এটি একটি 1-dimensional array। এর shape:
"""
print(x.shape)
"""
output : (4, ) এখানে 4 অর্থ 4টি element আছে।
"""

"""
-> Vector Vs NumPy Array
- Mathematics-এর Vector একটি mathematical concept।
- NumPy-এর ndarray হলো একটি programming data structure।

একটি NumPy array vector represent করতে পারে:
"""
x = np.array([1, 2, 3])
"""
কিন্তু প্রতিটি NumPy array-কে mathematical vector বলা ঠিক নয়। যেমন:
"""
matrix = np.array([
    [1, 2],
    [3, 4]
])
"""
এটি একটি 2D array, যা matrix represent করছে।
"""

"""
Q : NumPy কেন Python List-এর পরিবর্তে ব্যবহার করা হয়?
Python List:
numbers = [1, 2, 3, 4]

NumPy:
numbers = np.array([1, 2, 3, 4])

NumPy numerical computation-এর জন্য বিশেষভাবে optimized।

বিশেষ করে:
- homogeneous numerical data
- vectorized operations
- broadcasting
- linear algebra
- numerical functions

এর জন্য NumPy অত্যন্ত কার্যকর।
"""
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x+y)

"""
Python list-এ:
"""
x = [1, 2, 3]
y = [4, 5, 6]

print(x+y)

"""
অর্থাৎ NumPy array numerical vectorized operation-এর জন্য designed।
"""

"""
NumPy numerical computation-এর জন্য optimized এবং vectorized operations ব্যবহার করে। Large numerical arrays-এর ওপর অনেক ধরনের 
operation-এ Python loop-এর তুলনায় NumPy significantly faster হতে পারে।
"""

"""
NumPy array সাধারণত একই ধরনের data efficiently store করে এবং underlying implementation-এর কারণে numerical operations দ্রুত 
সম্পন্ন করতে পারে।
"""
