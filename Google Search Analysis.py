#!/usr/bin/env python
# coding: utf-8

# # Google Search Analysis with Python

# ##### Importing the necessary Python libraries

# In[2]:


import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()


# ##### Here I will be analyzing the Google search trends on the queries based on “Machine Learning”, so let’s create a DataFrame of the top 10 countries which search for “Machine Learning” on Google:

# In[3]:


trends.build_payload(kw_list=["Machine Learning"])
data = trends.interest_by_region()
data = data.sort_values(by="Machine Learning", ascending=False)
data = data.head(10)
print(data)


# ##### So, according to the above results, the search queries based on “Machine learning” are mostly done in China. We can also visualize this data using a bar chart:

# In[4]:


data.reset_index().plot(x="geoName", y="Machine Learning", 
                        figsize=(20,15), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()


# ##### So as we all know that Machine Learning has been the focus of so many companies and students for the last 3-4 years, so let’s have a look at the trend of searches to see how the total search queries based on “Machine Learning” increased or decreased on Google:

# In[5]:


data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Machine Learning'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(20, 15))
data['Machine Learning'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Machine Learning', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()


# # Conclusion
# 
# So we can see that searches based on “machine learning” on Google started to increase in 2017 and the highest searches were done in 2020 till today. This is how we can analyze Google searches based on any keyword. A business can perform Google search analysis to understand what people are looking for on Google at any given time.
