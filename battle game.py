#!/usr/bin/env python
# coding: utf-8

# In[47]:


import random

class Player:
    
    def __init__(self, health = 100):
        self.health = health
        
    def take_damage(self, damage):
        self.health -= damage

ai = Player()
human = Player()

playing = True

human_player_active = True

def ask_action():
    pass

def weak_punch():
    
    hit_strength = random.randint(18, 25)
    
    if human_player_active:
        
        if hit_strength >= ai.health:
            player_win()
            
        else:
            ai.take_damage(hit_strength)
            print(f'\nYou used the Cautious Punch, hitting the enemy for {hit_strength}. They have {ai.health} health left.')
          
    else:
        
        if hit_strength >= human.health:
            ai_win()
            
        else:    
            human.health -= hit_strength
            print(f'\nThe enemy used the Cautious Punch, hitting you for {hit_strength}. You got {human.health} health left.')
            

def strong_punch():
    hit_strength = random.randint(10, 35)
    
    if human_player_active:
        
        if hit_strength >= ai.health:
            player_win()
            
        else:
            ai.take_damage(hit_strength)
            print(f'\nYou used the Reckless Punch, hitting the enemy for {hit_strength}. They have {ai.health} health left.')
          
    else:
        
        if hit_strength >= human.health:
            ai_win()
            
        else:    
            human.health -= hit_strength
            print(f'\nThe enemy used the Reckless Punch, hitting you for {hit_strength}. You got {human.health} health left.')
    
def heal():
    if human_player_active:
        human.take_damage(-10)
        if human.health > 100:
            human.health = 100
        print(f'\nYou healed 10 and now have {human.health} left.')
    
    else:
        ai.take_damage(-10)
        if ai.health > 100:
            ai.health = 100
        print(f'\nThe enemy healed 10 and now has {ai.health} left.')
def ai_action():
    # while health >90 do not heal
    # while health low more likely to heal
    pass

# def check_death():
#     pass


# In[39]:


def player_win():
    print(f'You got him for {hit_strength}, bringing his health down to 0. You won!\n')
    # decision = lower(input('Play again? y/n '))
    # if decision[0] == 'y':
        # pass
    # else:
        # playing = False
        # break
    playing = False

def ai_win():
    pass


# In[48]:


weak_punch()


# In[49]:


human.take_damage(30)


# In[51]:


human.health


# In[55]:


heal()


# In[ ]:




