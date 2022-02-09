#!/usr/bin/env python
# coding: utf-8

# In[137]:


def unique_in_order(iterable):
    output = []
    for i in range(0, len(iterable)):
        if iterable[i:i+2].count(iterable[i]) == 1:
            output.append(iterable[i])
    return output

