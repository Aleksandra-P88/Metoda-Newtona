#!/usr/bin/env python
# coding: utf-8

# In[39]:


import matplotlib.pyplot as plt
import numpy as np
import math


# In[42]:


# kryterium stopu
e=0.003
# liczba kroków

def New(x0):
    inter=0
    t1=1
    y = 2-x0**(1/2)+ math.sin(2*x0)*math.exp(-x0/3)
    z = -1/(2*x0**(1/2)) +2*math.exp(-x0/3)*math.cos(2*x0)-1/3*math.exp(-x0/3)*math.sin(2*x0)
    
    while t1>e:
        x= x0 - y/z
        t1= np.linalg.norm(x-x0)
        x0=x
        inter+=1
        y= 2-x0**(1/2)+math.sin(2*x0)*math.exp(-x0/3)
        z= -1/(2*x0**(1/2))+2*math.exp(-x0/3)*math.cos(2*x0)-1/3*math.exp(-x0/3)*math.sin(2*x0)
    
    
    
    pie=x
    
    print('Liczba iteracji wykonanych zanim kryterium stopu zostało spełnione:{0}'.format(inter))
    print('Dla przyjętego punktu początkowego x0 zwrócony pierwiastek wynosi:{0}'.format(pie))

    
    
    
    
    


# In[43]:


print(New(5))


# In[ ]:





# In[ ]:




