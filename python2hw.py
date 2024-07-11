#!/usr/bin/env python
# coding: utf-8

# # Functions, Scoping, Data Collections 1 & List Comprehensions

# ## Tasks Today:
# 
# <i>Monday Additions (or, and ... if statements)</i>
# 
# 1) String Manipulation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) strip() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) title() <br>
# 2) Working With Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) min() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) max() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) sum() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) sort() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Copying a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) 'not in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Checking an Empty List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Removing Instances with a Loop <br>
# 3) List Comprehensions <br>
# 4) Tuples <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) sorted() <br>
# 5) Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) User-Defined vs. Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Accepting Parameters <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Default Parameters <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Making an Argument Optional <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Keyword Arguments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) Returning Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) *args <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Docstring <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Using a User Function in a Loop <br>
# 6) Scope

# ### String Manipulation

# ##### .lstrip()

# In[ ]:


# string.lstrip()



# ##### .rstrip()

# In[ ]:


# string.rstrip()


# ##### .strip()

# In[ ]:


# string.strip()


# ##### .title()

# In[ ]:


# string.title()


# ### String Exercise <br>
# <p>Strip all white space and capitalize every name in the list given</p>

# In[ ]:


names = ['    coNNor', 'max', ' EVan ', 'JORDAN']
# HINT: You will need to use a for loop for iteration



# ### Working With Lists

# ##### min()

# In[ ]:


# min(list)


# ##### max()

# In[ ]:


# max(list)



# ##### sum()

# In[ ]:


# sum(list)



# ##### sorted()

# In[1]:


# sorted(list)

people = {
    'Max': 'blue',
    'Lilly': 'brown',
    'Barney': 'blue',
    'Larney': 'brown',
    'Ted': 'purple',
}

print(sorted(people.items()))
print(sorted(people.keys()))
print(sorted(people.values()))


# ##### .sort() <br>
# <p>Difference between sort and sorted, is that sorted doesn't change original list it returns a copy, while .sort changes the original list</p>

# In[ ]:


# list.sort()


# use sorted when you don't want to alter original list, use .sort() when you want to alter original list


# ##### Copying a List

# In[ ]:


# [:] copies a list, doesn't alter original


# ##### 'in' keyword

# In[ ]:





# ##### 'not in' keyword

# In[ ]:





# ##### Checking an Empty List

# In[ ]:


# if l_1: or if l_1 = []



# ##### Removing Instances with a Loop

# In[ ]:


# while, remove



# ### List Exercise <br>
# <p>Remove all duplicates<br><b>Extra: Create a program that will remove any duplicates from a given list</b></p>

# In[ ]:


names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
# Hint 1: You will need an append
# Hint 2: Using an empty list will make life easier




# ### List Comprehensions <br>
# <p>Creating a quickly generated list to work with<br>*result*  = [*transform*    *iteration*         *filter*     ]</p>

# ##### In a list comprehension we have a few pieces:
# 1. The first is the counter/ variable - IN this the variable is x
# 2. then we have a transform for the variable
# 3. The finale part of a list comp is called the condition
# 
# ```python
#     [variable, transform, condition]
# ```

# In[ ]:


# number comprehension

# With a regular for loop


# IN a list comprehension we have a few pieces:
# The first is the counter/ variable - IN this the variable is x
# Then we have a transform for the variable 
# The finale part of a list comp is called the condition
#[variable, transform, condition]





# There are a few benefits to using List comprehensions. The most obvious would be that we now have shorter code to work with instead of using 3+ lines of code in the for loop variant.
# 
# Another is an added benefit to memory usage. Since the list's memory is allocated first before adding elements to it, we don't have to resize the list once we add elements to it.
# 
# Lastly, list comprehensions are considered the "pythonic" way to write code by the PEP8 standards (Python Style Guide)

# In[ ]:


# square number comprehension



# In[ ]:


# string comprehension





# In[ ]:





# In[ ]:





# ### Tuples <br>
# <p><b>Defined as an immutable list</b></p><br>Seperated by commas using parenthesis

# In[ ]:





# ##### sorted()

# In[ ]:





# ##### Adding values to a Tuple

# In[ ]:





# ## Functions

# ##### User-Defined vs. Built-In Functions

# In[ ]:





# ##### Accepting Parameters

# In[ ]:





# ##### Default Parameters

# In[ ]:





# ##### Making an Argument Optional

# In[ ]:





# ##### Keyword Arguments

# In[ ]:


# last_name='Max', first_name='Smith' in the function call

# see above


# # Creating a start, stop, step function

# In[ ]:





# ##### Returning Values

# In[ ]:





# ##### *args

# In[ ]:





# ##### Docstring

# In[ ]:





# ##### Using a User Function in a Loop

# In[ ]:





# ## Function Exercise <br>
# <p>Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names</p>

# In[ ]:


first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

# Output: ['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']


# ## Scope <br>
# <p>Scope refers to the ability to access variables, different types of scope include:<br>a) Global<br>b) Function (local)<br>c) Class (local)</p>

# In[ ]:





# # Exercises

# ## Exercise 1 <br>
# <p>Given a list as a parameter,write a function that returns a list of numbers that are less than ten</b></i></p><br>
# <p> For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]</p>

# In[6]:


# Use the following list - [1,11,14,5,8,9]

def numbers_less_than_ten(l_1):
    result = [num for num in l_1 if num < 10]
    return result

l_1 = [1, 11, 14, 5, 8, 9]
output = numbers_less_than_ten(l_1)
print(output)



# ## Exercise 2 <br>
# <p>Write a function that takes in two lists and returns the two lists merged together and sorted<br>
# <b><i>Hint: You can use the .sort() method</i></b></p>

# In[7]:


def merge_and_sort(l_1, l_2):
    merged_list = l_1 + l_2
    sorted_list = sorted(merged_list) 
    return sorted_list

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
result = merge_and_sort(l_1, l_2)
print(result)

