#!/usr/bin/env python
# coding: utf-8

# In[68]:


def divisors(integer):
    assert integer > 1
    lst = []
    for i in range(2, integer):
        if integer % i == 0:
            lst.append(i)
    if len(lst) == 0:
        return  "{} is prime".format(integer)
    else:
        return lst


# In[69]:


divisors(12)

