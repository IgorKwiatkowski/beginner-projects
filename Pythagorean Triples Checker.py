#!/usr/bin/env python
# coding: utf-8

# In[3]:


while True:

    side_a = int(input('Give me one side of a triangle\n'))
    side_b = int(input('\nGive me another side of the triangle\n'))
    side_c = int(input('\nAlright, last side of the triangle\n'))

    sides = [side_a, side_b, side_c]
    sides.sort()

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print('That is a right angled triangle alright.')

    else:
        print('Nope, that is not a right angled triangle.') 
        
    user_input = input('\nOne more triangle?')
    if user_input.lower() == 'n':
        print('thanks for playing')
        break
    else:
        continue


# In[ ]:




