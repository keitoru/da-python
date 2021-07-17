#In[0]
import numpy as np
#In[1]
a = np.arange(10)
# s = slice(2,7,2)
# print(a[s])

#In[3]
a = np.arange(10)
b = a[2:7:2]
print(b)

#In[4]
a = np.arange([[1,2,3],[3,4,5],[4,5,6]])
print(a)
print('从数组索引 a[1:] 处开始切割')
print(a[1:])
# %%

# In[2]
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a+10
# %%

#In[3]
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
np.add(a,10)
a.mean()
# %%

#In[4]
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a.mean()

# %%
#In[5]
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a.mean(axis=1)
# %%

#In[6]
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a.mean(axis=0)
# %%

#In[5]
x = np.arange(6).reshape((3,2))
print(x)
# %%

#In[6]
x = np.array([[1, 2, 3], [4, 5, 6]])
# 将x扁平，赋值给y
y = np.ravel(x)
print(y)
# %%

#In[1]
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
# outX = np.concatenate((x,y))
# print(outX)
outY = np.concatenate((x,y), axis=1)
print(outY)
# %%
