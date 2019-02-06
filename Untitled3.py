#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_notebook
from bokeh.io import show
from math import pi


# In[2]:


output_notebook()


# In[3]:


df = pd.read_csv("nacimientos2014.csv")


# In[4]:


df


# In[5]:


datos = ColumnDataSource(df.sample(10))


# In[6]:


datos.column_names


# In[7]:


grafico = figure(title='hola')


# In[8]:


grafico.square(x='talla', y='peso',color="olive", source=datos)


# In[9]:


show(grafico)


# In[10]:


grafico = figure(title="linea")

grafico.step(x='talla', y='peso', line_width=2, source=datos , color="olive")

show(grafico)


# In[33]:


grafico = figure(title="barras")
dat = ColumnDataSource(df.sample(30))
grafico.vbar(x="anio_nac",width= 0.05, top="anio_mad", color="blue",source=dat)

show(grafico)


# In[23]:


p = figure(plot_width=400, plot_height=400)
p.rect(x="peso", y="talla", width=5, height=50, color="#CAB2D6",
       angle="anio_nac", height_units="screen", source=datos)

show(p)


# In[24]:


p = figure(plot_width=400, plot_height=400)

p.patch(x="peso", y="talla", alpha=0.5, line_width=2,source=datos)

show(p)


# In[29]:


p = figure(plot_width=400, plot_height=400)
p.oval(x="peso", y="talla", width=40, height=40, color="#CAB2D6",
       angle=pi/3, height_units="screen",source=datos)

show(p)


# In[27]:


p = figure(plot_width=400, plot_height=400)
p.annulus(x=[1, 2, 3], y=[1, 2, 3], inner_radius=0.1, outer_radius=0.25,
          color="orange", alpha=0.6)

show(p)


# In[ ]:





# In[ ]:




