#!/usr/bin/env python
# coding: utf-8

# In[1]:


path_to_zip_file = "datasets.zip"
directory_to_extract_to = ""

import zipfile
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()


# In[2]:


import pandas as pd

Location = "all_140_in_33.P1.csv"
df = pd.read_csv(Location)
df

