#In[1]
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib as mpl
import numpy as np


# 中文乱码的处理
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']# 设置微软雅黑字体
plt.rcParams['axes.unicode_minus'] = False # 避免坐标轴不能正常的显示负号

#要求：
# （1）生成两行三列15×10的6个子图；
# （2）第一个子图：
# 数据：x=[1, 2, 3]; y=[0.6, 0.8, 0.2];
# 图形：设置三种不同颜色，绘制条形图；
ax1 = plt.subplot(231)
plt.bar([1, 2, 3], [0.6, 0.8, 0.2], color = 'indianred')
# （3）第二个子图：
# 绘制sin(x)和cos(x)的图像；
# 样式：
# 横轴设为'x'，纵轴设为'f(x)'；
# 添加图例：sin(x)和cos(x);
# 颜色不同，线型不同；
# 图形：绘制线图；
ax2 = plt.subplot(232)
x = np.linspace(0, 10, 30)
plt.plot(x, np.sin(x),label='sin(x)')
plt.plot(x, np.cos(x), color='r', linestyle='--',label='cos(x)')
plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('f(x)')
# （4）第三个子图：
# 数据：x=[1,2,3,4,5,6,7,8]; y= [3,1,4,5,8,9,7,2]
# 样式：
# 纵轴标签设为：['A','B','C','D','E','F','G','H']
# 图形：绘制水平条形图；
ax3 = plt.subplot(233)
x= [1,2,3,4,5,6,7,8]
plt.barh(x, [3,1,4,5,8,9,7,2])
x_label = ['A','B','C','D','E','F','G','H']
plt.xticks(x, x_label)
# （5）第四个子图：
# 生成两组服从正态分布的100个随机数,设为x,y；
# 样式：
# 颜色主题：采用mpl.cm.RdYlBu；
# 标注：采用'o'；
# 图形：绘制气泡图；
ax4 = plt.subplot(234)
x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.randn(100)
plt.scatter(x, y, c=colors, cmap=mpl.cm.RdYlBu, marker='o')
# （6）第五个子图：
# 数据：
# x = np.linspace(0.5,2*np.pi,20)
# y = np.random.randn(20)
# 样式：
# 棉棒样式：'-.';
# 棉棒末端的样式:'o';
# 指定基线的样式:'-';
# 图形：绘制棉棒图；
ax5 = plt.subplot(235)
x = np.linspace(0.5,2*np.pi,20)
y = np.random.randn(20)
plt.plot(x, y, linestyle='-.', marker='o')
# （7）第六个子图：
# 数据：
# elements = ["Flour","Sugar","Cream","Strawberry","Nuts"]
# weight1 = [40,15,20,10,15]
# weight2 = [30,25,15,20,10]
# 样式：
# 颜色设为：["#e41a1c","#377eb8","#4daf4a","#984ea3","#ff7f00"]
# 百分数保留一位小数；
# 其他参数自行发挥；
# 图形：绘制双层环形图；
ax6 = plt.subplot(236)
elements = ["Flour","Sugar","Cream","Strawberry","Nuts"]
colors = ["#e41a1c","#377eb8","#4daf4a","#984ea3","#ff7f00"]
weight1 = [40,15,20,10,15]
weight2 = [30,25,15,20,10]
ax6.pie(weight1, colors=colors,labels=elements, radius=1.2, autopct='%.1f%%', frame = 1)
ax6.pie(weight2, colors=colors,labels=elements, radius=1, autopct='%.1f%%')
# %%
