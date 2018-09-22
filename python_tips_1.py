
# coding: utf-8

# # Lambda functions
# 
# They are used to make quick functions and do not have to be set as an object when used inside another operator.

# In[1]:


# Standard function

def addition(a, b):
    return a + b

addition(5,10)


# In[2]:


# lambda functions or anonnymous functions

lambda_addition = lambda a, b : a+b

lambda_addition(5,10)


# # Enumerate
# 
# This lets you take the element's index and use it as a variable.

# In[3]:


pies = ['apple', 'blueberry', 'lemon']

for num, i in enumerate(pies):
    print(num, ':', i)


# # List comprehension
# 
# A quicker way to create lists, they act like for loops.

# In[4]:


# Manual way to make a list

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(list_1)
print(list_2)


# In[1]:


# Using list()

list_1_with_list = list(range(1,11))
list_2_with_list = list(range(11,21))

print(list_1_with_list)
print(list_2_with_list)


# In[5]:


# List comprehension autogenerates the list, they function closely to for loops.

list_1_with_comp = [x for x in range(1, 11)]
list_2_with_comp = [x for x in range(11, 21)]

print(list_1_with_comp)
print(list_2_with_comp)


# In[6]:


# It works with functions, I'm using the lambda function from above.

[lambda_addition(x, x) for x in range(0, 3)]


# In[7]:


# Also works with conditions
# The % is modulus which gives you the remainder after division.

# If an number is even add 1 if it's odd add 3

[x + 1 if x%2 ==0 else x + 3 for x in range(1, 11)] 


# In[8]:


# Nested loop example to show how the function like for loops.

for a in range(0, 3):
    for b in range(0, 5):
        print(a, b)


# In[9]:


# List comp also works as a nested loop.

[[a, b] for a in range(0, 3) for b in range(0, 5)]


# # Map
# 
# Use them to quickly apply a function across a list(array), can be used in conjuncture with lambda to be done even quicker

# In[10]:


# Using a standard function.

list(map(addition, list_1, list_2))


# In[11]:


# Using a lambda function.

list(map(lambda x, y: x + y, list_1, list_2))


# In[12]:


# Using our lambda_function above to show you don't have to write them directly inline.

list(map(lambda_addition, list_1, list_2))


# # Reduce
# 
# Reduce is a really useful function for performing some computation on a list and returning the result. It applies a rolling computation to sequential pairs of values in a list. This one is tricky.

# In[13]:


# Reduce needs to be imported in Python3.x
from functools import reduce

# Easiest example to understnad is trying to multiply a whole list together i.e 1*2*3*4*5*6*7*8*9*10

reduce((lambda x, y: x * y), list_1) 


# In[14]:


# Another great example is using reduce to compare elements in a list against each other.

reduce(lambda x, y: y if y > x else x, list_1) # Finding the largest number in the list


# In[15]:


reduce(lambda x, y: y if y < x else x, list_1) # Finding the smallest number in the list


# # Filter
# 
# As its name suggests its used to filter things like a list(array), uses lambda functions as well. They're really good to know.

# In[16]:


list_1


# In[17]:


# Filter for elements greater than 5

list(filter(lambda x : x > 5, list_1))


# # Zip
# 
# Easy way to take two lists and put them together.

# In[18]:


# Very useful when making a dictionary

animals = ['dog', 'cat', 'sheep']
animal_names = ['Tim', 'Steve', 'Matt']

dict(zip(animal_names, animals))


# In[19]:


# Will make a tuple by default

list(zip(animal_names, animals))


# In[20]:


# it will return as an object so you need a list() or dict() call to return anything
zip(animal_names, animals)


# # Print Statements

# In[21]:


# Standard for loop print:
for i in list_1:
    print(i)


# In[22]:


# For loop printing on the same line

for i in list_1:  # defaults are sep=' ', end='\n'
    print(i, end=' ')


# In[23]:


# Quicker way than a for loop.
print(*list_1, sep='\n') 


# In[24]:


# Quickest way of unpacking of a list, although it prints on the same line.
print(*list_1)


# # Print Formatting

# In[25]:


# Format a print statement two ways

print('hello {}'.format('world'))


# In[26]:


print('hello %s' % 'world')


# In[27]:


# You can unpack a list to format they will align numerically

snacks = ['chips', 'candy', 'peanuts']

print('{}, {}, {}'.format(*snacks))


# In[28]:


# F strings allow you to put a variable by its name within a string.

var1 = 'cat'
var2 = 'dog'

print(f'{var1}{var2} is a show')


# In[29]:


# Raw strings will print out exactly what is in the string. 
# This is used in regex or regular expressions... import re

print('hello\n')

print(r'hello\n')


# In[30]:


# Formatting money, this one is really useful!

'${:,.2f}'.format(1234.54)

