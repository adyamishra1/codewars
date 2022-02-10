#!/usr/bin/env python
# coding: utf-8

# In[23]:


def find_short(s):
    return min([len(x) for x in s.split()])

