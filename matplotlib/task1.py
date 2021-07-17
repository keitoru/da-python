
import matplotlib.pyplot as plt
import numpy as np

#In[1]

# 画出直线 y = x-1, 线型为虚线，线宽为1，
x = np.linspace(-1, 2, 50)
y = x - 1
# 纵坐标范围（-2，1），横坐标范围（-1，2），横纵坐标在（0，0）坐标点相交。
plt.figure(num = 1, figsize=(8,5))
plt.plot(x, y, linewidth=1.0, linestyle='--')

plt.xlim((-1,2))
plt.ylim((-2,1))
plt.xlabel('X')
plt.ylabel('Y')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.xticks([-1,-0.5,1], [r'$bad$', r'$normal$', r'$good$'])
plt.show()
# 横坐标的 [-1,-0.5,1] 分别对应 [bad, normal, good]
# %%

#In[2]
# 假设大家在30岁的时候，根据自己的实际情况，统计出来了你和同桌从11岁到30岁每年交的朋友的数量如列表a和b,
# 请绘制出该数据的折线图,以便分析自己和同桌每年交朋友的数量走势
x = range(11, 31)
a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
b = [1,0,3,1,2,2,2,3,1,1,1,1,1,2,1,1,2,3,2,2]

x_label = [i for i in x]
plt.figure(figsize=(20, 8), dpi=80)
plt.rcParams['font.family']='Microsoft YaHei'#设置中文字体
plt.xlabel("年龄")
plt.ylabel("交友数")
plt.title("自己和同桌每年交朋友的数量走势")
plt.plot(x, a,label="我")
plt.plot(x, b, color='red',label="同桌")
plt.xticks(x, x_label)
plt.yticks(range(0, 10, 1))
plt.legend(loc="best")

ax = plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 11))
plt.show()
# %%
