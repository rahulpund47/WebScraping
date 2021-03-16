#!/usr/bin/env python
# coding: utf-8

# In[19]:





# In[20]:




import WebScrapPackage1 as k

df=k.get_page("YesBank")
df.to_csv(r'C:\Users\admin\Downloads\WebScrapping\Data\YesBank.csv') 

   
#print(df)
df=k.get_page("TTM")
df.to_csv(r'C:\Users\admin\Downloads\WebScrapping\Data\TTM.csv') 

df=k.get_page("LICT")
df.to_csv(r'C:\Users\admin\Downloads\WebScrapping\Data\LICT.csv') 


# In[ ]:





# In[ ]:





# In[11]:


pip install plotly


# In[21]:


import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv(r'C:\Users\admin\Downloads\WebScrapping\Data\YesBank.csv')

fig = go.Figure(data=[go.Candlestick(x=df['DateTime'],
                open=df['Open'], high=df["High"],
                low=df["Low"], close=df['Previous close'])
                     ])

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()


# In[ ]:




