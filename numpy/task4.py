#In[0]
import pandas as pd
import numpy as np

data = {"col1":['Python', 'C', 'Java', 'R', 'SQL', 'PHP', 'Python', 'Java', 'C', 'Python'],
       "col2":[6, 2, 6, 4, 2, 5, 8, 10, 3, 4],
       "col3":[4, 2, 6, 2, 1, 2, 2, 3, 3, 6]}
df = pd.DataFrame(data)

#In[1]
df['new_index'] = range(1,11)
df.set_index('new_index')

# df.reset_index(drop = True, inplace = True) # drop = True：原有索引就不会成为新的列
# %%

#In[2]
df
# df.loc[len(df)] = [2, 'css', 3]
# df.iloc[:, ::-1]

# %%

#In[3]

