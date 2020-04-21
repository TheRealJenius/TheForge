#!/usr/bin/env python
# coding: utf-8

# In workspaces like this one, you will be able to practice visualization techniques you've seen in the course materials. In this particular workspace, you'll practice creating single-variable plots for categorical data.

# In[2]:


# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

# solution script imports
from solutions_univ import bar_chart_solution_1, bar_chart_solution_2


# In this workspace, you'll be working with this dataset comprised of attributes of creatures in the video game series Pokémon. The data was assembled from the database of information found in [this GitHub repository](https://github.com/veekun/pokedex/tree/master/pokedex/data/csv).

# In[3]:


pokemon = pd.read_csv('./data/pokemon.csv')
pokemon.head()


# **Task 1**: There have been quite a few Pokémon introduced over the series' history. How many were introduced in each generation? Create a _bar chart_ of these frequencies using the 'generation_id' column.

# In[4]:


# YOUR CODE HERE
sb.countplot(data = pokemon, x = 'generation_id')


# Once you've created your chart, run the cell below to check the output from our solution. Your visualization does not need to be exactly the same as ours, but it should be able to come up with the same conclusions.

# In[5]:


bar_chart_solution_1()


# **Task 2**: Each Pokémon species has one or two 'types' that play a part in its offensive and defensive capabilities. How frequent is each type? The code below creates a new dataframe that puts all of the type counts in a single column.

# In[6]:


pkmn_types = pokemon.melt(id_vars = ['id','species'], 
                          value_vars = ['type_1', 'type_2'], 
                          var_name = 'type_level', value_name = 'type').dropna()
pkmn_types.head()


# Your task is to use this dataframe to create a _relative frequency_ plot of the proportion of Pokémon with each type, _sorted_ from most frequent to least. **Hint**: The sum across bars should be greater than 100%, since many Pokémon have two types. Keep this in mind when considering a denominator to compute relative frequencies.

# In[13]:


# YOUR CODE HERE
n_pokemon = pokemon.shape[0]
pkmn_types_count = pkmn_types['type'].value_counts()
pkmn_types_order = pkmn_types_count.index
max_type_count = pkmn_types_count[0]
max_prop = max_type_count / n_pokemon
#print(max_prop)
tick_props = np.arange(0,max_prop,0.02)
tick_names = ['{:0.2f}'.format(v) for v in tick_props]
sb.countplot(data = pkmn_types, y = 'type', order = pkmn_types_order)
plt.xticks(tick_props * n_pokemon, tick_names)
plt.xlabel('Proportion');


# In[14]:


bar_chart_solution_2()


# If you're interested in seeing the code used to generate the solution plots, you can find it in the `solutions_univ.py` script in the workspace folder. You can navigate there by clicking on the Jupyter icon in the upper left corner of the workspace. Spoiler warning: the script contains solutions for all of the workspace exercises in this lesson, so take care not to spoil your practice!
