#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


def wrangle(filepath):
    df = pd.read_csv(filepath)
    
    # drop ENGINE LUBE OIL DAILY VISCOSITY ANALYSIS REPORT FOR AKSA ENERGY GHANA - 2023 column
    df.drop(
            columns = "ENGINE LUBE OIL DAILY VISCOSITY ANALYSIS REPORT FOR AKSA ENERGY GHANA - 2023",
        inplace = True
    )
    
    # rename index "1" in column "Unnamed: 0" to DG_No
    new_label = "DG_No"
    df.at[1, "Unnamed: 0"] = new_label  
    
    # drop irrelevant index namely "0, 2" and drop columns Unnamed: 1", "Unnamed: 3", "Unnamed: 4"
    df.drop(index = [0, 2], inplace = True)
    df.drop(columns = ["Unnamed: 1", "Unnamed: 3", "Unnamed: 4"], inplace = True)
    
    # Assign columns with date as new header
    new_header = df.iloc[0]
    df = pd.DataFrame(df.values[1:], columns = new_header)
    
    # set DG_No as index
    df.set_index("DG_No", inplace = True)  
               
    return df    


# In[4]:


df = wrangle("viscosity_data.csv")
df.tail()


# In[23]:


fig, ax = plt.subplots(figsize=(7, 5.8))
# set criteria for upper and lower limit verticle lines
upper_limit = 130*1.4
lower_limit = 130 - 130*0.25
plt.axvline(upper_limit, linestyle = "--", color = "r", label = "Upper Limit")
plt.axvline(lower_limit, linestyle = "--", color = "b", label = "Lower Limit")

# fetch last but one "non_na_values" from dafaframe and put into a dataframe
non_na_values = (df.iloc[:, -1][df.iloc[:, -1].notna()]).astype(float)
values = pd.DataFrame(non_na_values)

# plot horizontal bar graph
non_na_values.plot(kind = "barh", color = "green", label= f"Used Oil Viscosity [{df.columns[-1]}]")

# indicate viscosity values inside barchart close to the top
for index, value in enumerate(non_na_values):
    plt.text(
        value, index, str(value), ha='right',
        va='center', color = "white", weight = "bold", fontsize = 8)
    
# label axes, titles and position legend
plt.xlabel("Viscosity @ 40deg [cSt]")
plt.ylabel("Engine Number")
plt.title("Distribution of Online Engine Lube Oil Viscosity", weight = "bold")
plt.legend(loc = "upper left", fontsize = "8");
plt.show()


# In[18]:


df.columns[-1]


# In[ ]:




