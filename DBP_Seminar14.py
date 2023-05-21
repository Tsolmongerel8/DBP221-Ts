#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Өгөгдөл
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10)
y = x*2 
z = x**2 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Даалгавар1
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10)
y = x*2
z = x**2
plt.plot(x, y)
plt.title("Граф1")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# In[6]:


#Даалгавар2
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10)
y = x*2
z = x**2
plt.plot(x, y, color = 'r')
plt.show()


# In[5]:


#Даалгавар4
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10)
y = x**2
z = x**2
plt.plot(x, y, color = 'r')
plt.show()


# In[7]:


# Даалгавар3
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 10)
y = x*2 
z = x**2 
plt.plot(x, y, linestyle = 'dashed' )
plt.show()


# In[ ]:




