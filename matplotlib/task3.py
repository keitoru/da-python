#In[0]
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
%matplotlib inline
#设置中文编码和负号的正常显示
plt.rcParams['font.family']='Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('data/电子产品销售分析.csv')
# df.head()

# 4、增加月、日、时间列
df['event_time'] = pd.to_datetime(df['event_time'].str[:19], format="%Y-%m-%d %H:%M:%S")
df['Month'] = df['event_time'].dt.month
df['Day'] = df['event_time'].dt.day
df['Hour'] = df['event_time'].dt.hour

# 6、将有缺失项的两列用missing填充
df['category_code'].fillna('missing', inplace=True)
df['brand'].fillna('missing', inplace=True)
# np.sum(df.isnull())

# 7、删除重复值
df.duplicated()
df.drop_duplicates()

#第一题：每月订单数量的折线图
plt.figure(figsize=(10, 5))
data = df[df['price'] > 0].groupby('Month')['order_id'].nunique()
plt.plot(data)
plt.xlabel('月份')
plt.ylabel('订单数量')
plt.title('每月订单数量')

#第二题：不同省份成交金额的水平柱状图
plt.figure(figsize=(10, 5))
data = df[df['price'] > 0].groupby('local')['price'].sum().sort_values(ascending=True)
data.plot.barh()
plt.xlabel('成交金额')
plt.ylabel('省份')
plt.title('不同省份成交金额')

#第三题：不同省份用户男女人数对比簇状柱形图
plt.figure(figsize=(10, 5))
data = df[df['price'] > 0]
city = data.drop_duplicates(['local'])['local']
male = data[data['sex'] == '男'].groupby('local')['sex'].count()
female = data[data['sex'] == '女'].groupby('local')['sex'].count()
plt.bar(city,male,color='blue',label='男')
plt.bar(city,female,bottom=male,color='pink',label='女')
plt.legend(loc='best')
plt.xlabel('性别')
plt.ylabel('省份')
plt.title('不同省份用户男女人数对比簇状图')
plt.show()

#In[2]
# 8、画出每月订单数量
plt.figure(figsize=(10, 5))
plt.plot(df[df['price'] > 0].groupby('Month')['user_id'].nunique())
plt.xlabel('月份')
plt.ylabel('订单数量')
plt.title('每月订单数量')

# 9、每月消费人数的折线图
plt.figure(figsize=(10, 5))
plt.plot(df[df['price'] > 0].groupby('Month')['user_id'].sum(), linestyle='--', color='g')
plt.xlabel('月份')
plt.ylabel('消费人数')
plt.title('每月消费人数')

# 10、不同省份用户数量的柱状图***
plt.figure(figsize=(10, 5))
df[df['price']>0].groupby('local')['user_id'].nunique().sort_values(ascending=True).plot.bar()
plt.xlabel('省份')
plt.ylabel('用户数量')
plt.title('不同省份用户数量')
plt.show()

# 11、不同省份订单数量的水平柱状图
plt.figure(figsize=(12,8))
df[df['price']>0].groupby('local')['order_id'].nunique().sort_values(ascending=True).plot.barh()
plt.xlabel('订单数量')
plt.ylabel('省份')
plt.title('不同省份订单数量')

# 12、下单小时分布的折线图
plt.figure(figsize=(12,8))
df[df['price']>0].groupby('Hour')['order_id'].nunique().plot()
plt.xlabel('小时')
plt.ylabel('订单数')
plt.title('订单随小时数变化')
plt.show()

# 13、查看未完成订单的数量
df[df['price']==0].count()

# 14、消费次数与消费金额关系的散点图
plt.figure(figsize=(12,8))
plt.scatter(x=df[df['price']>0].groupby('user_id')['order_id'].nunique(),
           y=df[df['price']>0].groupby('user_id')['price'].sum())
plt.xlabel('消费次数')
plt.ylabel('消费金额')
plt.title('消费次数与消费金额关系')
plt.show()

# 15、用户男女人数对比扇形图
df_sex = df['sex'].value_counts()
df = df[df['price']>0]

plt.figure(figsize=(8,8))
plt.pie(df_sex.values, labels=df_sex.index, autopct='%.2f%%',
       wedgeprops={'linewidth':0.5,'edgecolor':'green'},
       textprops={'fontsize':30,'color':'#003371'}
       )
plt.title('男女占比', size=30)
plt.show()

# 16、年龄分布直方图
plt.hist(df['age'], bins=10, color='steelblue', edgecolor='k', label='年龄', alpha=0.5)
plt.title('年龄分布直方图')
plt.legend()
plt.tick_params(top='off', right='off')
plt.show()

# 17、将年龄离散化，增加一列age_box
bins = [10,20,30,40,50]
labels = ['10-20','20-30','30-40','40-50']
df['age_box'] = pd.cut(df['age'], bins, labels=labels)
age_box = df['age_box'].value_counts()[labels]
age_box

# 18、不同年龄段与购买数量的关系，画出柱状图
plt.figure(figsize=(10,6))
plt.bar(labels, age_box.values, color='#cb3a56')
plt.ylabel('购买数量', size=22)
plt.xlabel('年龄分段', size=22)
plt.xticks(size=18)
plt.yticks(size=18)

plt.title('不同年龄分段的购买情况', size=25)
plt.show()

# %%
