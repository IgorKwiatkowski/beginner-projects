#!/usr/bin/env python
# coding: utf-8

# In[36]:


# Between 1 and 1000, there is only 1 number that meets the following criteria.
# While it could be manually figured out with pen and paper, it would be much more
# efficient to write a program that would do this for you.
# With that being said, your goal is to find out which number meets these criteria.
# To find out if you have the correct number, click the link at the bottom of this main post.
# NOTE: since 0 is even, there are two such numers


from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

isPrime(5)

for num in range(10,1000):
    num_str = str(num)
    num_list = []
    for char in num_str:
        num_list.append(char)
    if isPrime(num) and '1' not in num_str and '7' not in num_str and sum(int(digit) for digit in num_str) < 11 and (int(num_list[0]) + int(num_list[1])) % 2 != 0 and int(num_list[-2]) % 2 == 0 and int(num_list[-1]) == len(num_str):
        print(num)
    


# In[28]:


num = 987
num_str = str(num)
num_list = []
for char in num_str:
    num_list.append(char)


# In[29]:


'e' not in num_str


# In[30]:


print(num)


# In[31]:


num_list


# In[35]:


(int(num_list[0]) + int(num_list[1])) % 2 != 0


# In[ ]:




