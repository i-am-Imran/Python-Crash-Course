#!/usr/bin/env python
# coding: utf-8

# In[2]:


def make_pizza(size,*toppings):
    print(f"Making pizza of size-{size} with following toppings.")
    for topping in toppings:
          print('-'+topping)

