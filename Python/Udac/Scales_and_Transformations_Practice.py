#!/usr/bin/env python
# coding: utf-8

# In[1]:


# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

from solutions_univ import scales_solution_1, scales_solution_2


# Once again, we make use of the Pokémon data for this exercise.

# In[2]:


pokemon = pd.read_csv('./data/pokemon.csv')
pokemon.head()


# **Task 1**: There are also variables in the dataset that don't have anything to do with the game mechanics, and are just there for flavor. Try plotting the distribution of Pokémon heights (given in meters). For this exercise, experiment with different axis limits as well as bin widths to see what gives the clearest view of the data.

# In[11]:


# YOUR CODE HERE
plt.hist(data = pokemon, x = 'height', bins = 100);
plt.xlim(0,6)


# In[3]:


# run this cell to check your work against ours
scales_solution_1()


# **Task 2**: In this task, you should plot the distribution of Pokémon weights (given in kilograms). Due to the very large range of values taken, you will probably want to perform an _axis transformation_ as part of your visualization workflow.

# In[22]:


# YOUR CODE HERE

binsize = 10 ** np.arange(-1,3+0.1, 0.1)
ticks = [0.1,1,10,100,1000]
labels = ['{}'.format(v) for v in ticks]
plt.hist(data = pokemon, x = 'weight', bins = binsize);
plt.xscale('log')
plt.xticks(ticks,labels);
#np.log10(pokemon['weight'].describe())


# In[14]:


# run this cell to check your work against ours
scales_solution_2()


# In[ ]:




