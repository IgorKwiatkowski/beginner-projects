#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
import time

answers = ['Yes','No','Maybe','Hard to say','Time will tell']

playing = True

while playing:
    
    input('What is your question?\n')
    print('Thinking...\n')
    time.sleep(3)
    print(random.choice(answers))
    user_input = input('\nOne more question?')
    if user_input.lower() == 'n':
        print('thanks for playing')
        break
    else:
        continue


# In[ ]:




