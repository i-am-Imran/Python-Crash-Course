#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''A simple attempt to model a restaurant'''
class Restaurant:
    def __init__(self,name,cusine_type):
        """Creating a restaurant class"""
        self.name = name
        self.cusine_type = cusine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """this method is for displaying name and type only"""
        print(f"The Restaurant name is {self.name.title()}.")
        print(f"A {self.cusine_type.title()}-type of restaurant.")
        
    def open_restaurant(self):
        """Check if restaurant is open/closed."""
        print(f"The restaurant, {self.name.title()} is open now.")
        
    def customer_served(self):
        """How many customer we have served"""
        print(f'This restaurant has served over-{self.number_served} customers.')
        
    def set_number_served(self,number):
        """change value of customer we have served"""
        self.number_served = number
        
    def increment_number_served(self,number):
        '''increment value od customer served'''
        self.number_served += number
    
    

