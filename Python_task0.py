#!/usr/bin/env python
# coding: utf-8

# In[1]:


from array import*
Scores = array('i',[100,108,112,115,150,178,143,132,190,235,253,298,328,390,257,288,393,425,458,450,473,333,452,490,495,488,543,532,590,605])
for x in Scores:print (x)


# In[3]:


import numpy as np
days=np.arange(1,31)
print (days)


# In[11]:


import matplotlib.pyplot as plt
import numpy as np
y= array('i',[100,108,112,115,150,178,143,132,190,235,253,298,328,390,257,288,393,425,458,450,473,333,452,490,495,488,543,532,590,605])
x=np.arange(1,31)
plt.xlim(1,31)
plt.ylim(100,1000)
plt.xlabel('Score')
plt.ylabel('Days')
plt.title('Performance')
plt.plot(x,y)
plt.show()


# In[14]:


import numpy as np
Scores = array('i',[100,108,112,115,150,178,143,132,190,235,253,298,328,390,257,288,393,425,458,450,473,333,452,490,495,488,543,532,590,605])
print("Score:",Scores)
print("mean of scores:",np.mean(Scores))


# In[6]:


import numpy as np
Scores=array('i',[100,108,112,115,150,178,143,132,190,235,253,298,328,390,257,288,393,425,458,450,473,333,452,490,495,488,543,532,590,605])
print("Score:",Scores)
print("median of score:",np.median(Scores))


# In[12]:


import numpy as np
Scores=array('i',[100,108,112,115,150,178,143,132,190,235,253,298,328,390,257,288,393,425,458,450,473,333,452,490,495,488,543,532,590,605])
maxElement= np.amax(Scores)
minElement= np.amin(Scores)
print('Maximum score:', maxElement)
print('Minimum score:', minElement)





