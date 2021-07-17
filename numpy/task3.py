#In[0]
import pandas as pd
import numpy as np
data = {"grammer":['Python', 'C', 'Java', 'R', 'SQL', 'PHP', 'Python', 'Java', 'C', 'Python'],
       "score":[6, 2, 6, 4, 2, 5, 8, 10, 3, 4],
       "cycle":[4, 2, 6, 2, 1, 2, 2, 3, 3, 6]}
df = pd.DataFrame(data)
#查看最后5行数据
# df[5:10]
#查看列数
# len(df)
#
len(df['grammer'].unique())
# %%
