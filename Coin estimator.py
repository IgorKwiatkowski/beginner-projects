#!/usr/bin/env python
# coding: utf-8

# In[2]:


# possible_weights = [0, 1.64, 2.13, 2.59]

# coin_weight = possible_weights[int(input('Jaki nominał?\n1 - 1 grosz\n2 - 2 grosze\n3 - 5 groszy\n'))]

# masa = int(input('Jaka masa?\n'))


# In[6]:


# print(f'{coin_weight}')


# In[13]:


import math

coin_weights = [1.64, 2.13, 2.59]

masa_groszowek = int(input('Ile ważą Twoje groszówki?\n'))
masa_dwugroszowek = int(input('\nIle ważą Twoje dwugroszówki?\n'))
masa_pieciogroszowek = int(input('\nIle ważą Twoje pięciogroszówki?\n'))

liczba_groszowek = round(masa_groszowek / coin_weights[0])
liczba_dwugroszowek = round(masa_dwugroszowek / coin_weights[1])
liczba_pieciogroszowek = round(masa_pieciogroszowek / coin_weights[2])

print(f'Masz {liczba_groszowek} groszówek, które są warte {liczba_groszowek} groszy, {liczba_dwugroszowek} dwugroszówek wartych {liczba_dwugroszowek*2} groszy i {liczba_pieciogroszowek} pięciogroszówek wartych {liczba_pieciogroszowek*5} groszy.')
print(f'W sumie masz {(liczba_groszowek + liczba_dwugroszowek*2 + liczba_pieciogroszowek*5) / 100} złotych.')
print(f'Potrzebujesz {math.ceil(liczba_groszowek / 25)} rulonów na groszówki, {math.ceil(liczba_dwugroszowek / 25)} rulonów na dwugroszówki i {math.ceil(liczba_pieciogroszowek / 25)} rulonów na pięciogroszówki.')


# In[4]:





# In[8]:





# In[ ]:




