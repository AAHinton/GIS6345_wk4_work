#!/usr/bin/env python
# coding: utf-8

# In[1]:


word='banana'
letter=word.count('a')
print(letter)


# In[2]:


fruit='banana'
fruit[0:5:2]


# In[3]:


fruit[::-1]


# In[4]:


fruit[0::]


# In[5]:


fruit[:-1]


# In[6]:


def is_palindrome(word):
    return word ==word[::-1]


# In[7]:


is_palindrome("hello")


# In[8]:


is_palindrome("deleveled")


# In[ ]:




