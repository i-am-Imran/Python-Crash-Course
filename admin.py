#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Separate admin profile and privileges class of """

from user import User

class Admin_Privileges:
    '''Separate privilege(offered to admin) class for admin'''
    def __init__(self):
        '''A admin have these privileges'''
        self.privileges = ['can add post','can delete post','can ban user','can update feed']
        
    def show_privileges(self):
        print('\nFollowing are privileges only for admin:')
        for x in self.privileges:
            print('-'+x)
            
            
class Admin(User):
    '''Inherited from User class, A class for admin'''
    def __init__(self,f_name,l_name,age,country):
        super().__init__(f_name,l_name,age,country)
        self.my_privileges = Admin_Privileges()

