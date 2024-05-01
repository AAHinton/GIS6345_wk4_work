#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[1]:


from arcgis.gis import GIS
gis = GIS("home")


# #### Now you are ready to start!

# In[2]:


map1=gis.map('John H Kerr Reservoir')
map1


# In[ ]:





# In[3]:


# Item Added From Toolbar
# Title: Boating Access Sites VA | Type: Feature Service | Owner: darcyca_vcu_ces
item = gis.content.get("ce868a7bd13547d08419ca9c9ac32d5f")
item


# In[ ]:





# In[4]:


# Item Added From Toolbar
# Title: Boating Access Sites VA | Type: Feature Service | Owner: darcyca_vcu_ces
item = gis.content.get("ce868a7bd13547d08419ca9c9ac32d5f")
item


# In[5]:


map1.add_layer(item)


# In[ ]:





# In[6]:


# Item Added From Toolbar
# Title: Virginia Trailheads 2020 | Type: Feature Service | Owner: david.boyd
item = gis.content.get("5cb5b561e4564d9b88ea986c71e7be4f")
item


# In[7]:


map1.add_layer(item)


# In[ ]:




