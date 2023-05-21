#!/usr/bin/env python
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt
import numpy as np
x = np.array(["Python", "C", "Java", "C++", "C#", "Visual Basic"])
y = np.array([12.20, 11.91, 10.47, 9.63, 6.12, 5.42])

plt.bar(x,y)
plt.title("TIOBE index")
plt.show()


# In[15]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([12.20, 11.91, 10.47, 9.63, 6.12, 5.42])
mylabels = ["Python", "C", "Java", "C++", "C#", "Visual Basic"]

plt.pie(y, labels = mylabels)
plt.title("TIOBE index")
plt.show


# In[16]:


import matplotlib.pyplot as plt
import numpy as np
x = np.array(["Python", "Java", "JavaScript", "C#", "C++", "PHP"])
y = np.array([27.61, 17.64, 9.21, 7.79, 7.01, 5.27])

plt.bar(x,y)
plt.title("PYPL index")
plt.show()


# In[18]:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([27.61, 17.64, 9.21, 7.79, 7.01, 5.27])
mylabels = ["Python", "Java", "JavaScript", "C#", "C++", "PHP"]

plt.pie(y, labels = mylabels)
plt.title("PYPL index")
plt.show


# In[ ]:




