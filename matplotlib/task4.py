#In[0]
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# 2. 加载seaborn自带数据集
filepath = 'data/seaborn'
tips = sns.load_dataset("tips", cache=True, data_home=filepath)
fmri = sns.load_dataset("fmri", cache=True, data_home=filepath)
exercise = sns.load_dataset("exercise", cache=True, data_home=filepath)
titanic =  sns.load_dataset("titanic", cache=True, data_home=filepath)

# 3. 画布主题
def sinplot(flip = 1):
    x = np.linspace(0, 10, 100)
    for i in range(1, 4):
        plt.plot(x, np.sin(x + i * 0.5) * (4 - i) * flip)
# sns.set() # 默认主题：灰色网格；修改具有全局性
# sns.set_style('whitegrid')
# sinplot()
# sns.set_style("ticks")
# sinplot() # 这个主题比white主题多的是刻度线
# sns.despine() #

# plt.figure(figsize = (10, 8))
# sns.set_style('dark')
# with sns.axes_style('whitegrid'): # with内部的都是白色网格主题，对外部不受影响
#     plt.subplot(2, 1, 1) #绘制多图函数，两行一列第一个子图
#     sinplot()
# plt.subplot(2, 1, 2) # 两行一列第二个子图
# sinplot()

# sns.set()
# plt.figure(figsize=(8,3))
# sns.set_context("paper")
# sinplot()

# sns.relplot(x="total_bill", y="tip", hue='day', data=tips)

# plt.figure(figsize = (10, 8))
# sns.set_style('dark')
# with sns.axes_style('whitegrid'): # with内部的都是白色网格主题，对外部不受影响
#     plt.subplot(2, 1, 1) #绘制多图函数，两行一列第一个子图
#     sinplot()
# plt.subplot(2, 1, 2) # 两行一列第二个子图
# sinplot()

# 第一题：绘制多个分类的散点图
# 要求：
# 利用pandas构建时间序列数据，从2000-1-31开始，以月为频率，生成100条时间序列；
# 生成4列100个服从高斯分布的随机数，并按列求累计和（cumsum函数）；
# 合并所有列，并设置列名为a,b,c,d，生成散点图；
# dates = pd.date_range(start='2000-1-31', periods=100, freq='M')
# np.random.seed(1)
# data = np.random.randn(100,4)
# data_cum = np.cumsum(data,axis=0)
# df = pd.DataFrame(data,index=dates,columns=['a','b','c','d'])
# df.head()
# #绘制散点图
# plt.figure(figsize=(10,8))
# sns.set()
# sns.scatterplot(data=df)


# 第二题：绘制2010年人口年龄结构金字塔
# 步骤:
# 读取文件：people.csv
# 筛选数据：地区:全国；性别：男和女；年龄段：不等于合计；
# 添加一列：人口占比 = 每行的统计人数/总统计人数 * 100，并保留两位有效数字；
# file = filepath+'/people.csv'
# df = pd.read_csv(file)
# people = df[(df['年龄段'] != '合计') & (df['地区'] == '全国') & (df['性别'].isin(['男', '女']))]
# people.loc[:,~people.columns.str.contains('Unnamed')].reset_index(drop=True).head()
# sumP = people['统计人数'].sum()
# people['人口占比'] = round(people['统计人数'] / sumP * 100, 2)

# #设置中文编码和负号的正常显示
# plt.rcParams['font.family']='Microsoft YaHei'
# plt.rcParams['axes.unicode_minus'] = False
#绘制图形
# 绘制人口年龄结构金字塔（女左男右）：
# 横轴：人口占比；纵轴：年龄段(0岁,1-4岁,5-9岁.....)
# tips:金字塔实际相当于两个相反方向的水平条形图，然后以纵轴合并即可得到金字塔结构；
# 注:记住修改横轴刻度，两边对称显示；
# people_m = people[people['性别'] == '男']
# sns.barplot(x='人口占比',y='年龄段',color='indianred',data=people_m)
# people_f = people[people['性别'] == '女']
# people_f['人口占比'] = 0 - people_f['人口占比']
# sns.barplot(y='年龄段', x='人口占比',color = 'steelblue', data=people_f)

# 第三题：绘制各年龄段男VS女占比差异线图
# 步骤：
# 构建所需数据框：各年龄段，男占比，女占比；
# 占比差异即为：男占比-女占比；
# 横轴：各年龄段；纵轴：占比差异；
# 绘制线图
# 添加横纵轴标签；
# 添加标题；
# 设置横轴标签旋转45度；
# %%
