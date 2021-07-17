import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#画图时用于显示中文字符
from pylab import mpl

def splitSaletime(timeColSer):
    timeList = []

    for value in timeColSer:
        dateStr = value.split(' ')[0]
        timeList.append(dateStr)

    timeSer = pd.Series(timeList)
    return timeSer

#1. 导入数据
file_name = "./file/朝阳医院2018年销售数据.xlsx"
xls = pd.ExcelFile(file_name)
#提取数据
dataDF = xls.parse('Sheet1', dtype = 'object')

# print(xls.sheet_names[0])
#查看数据几行几列
# print(dataDF.shape)
#查看索引
# print(dataDF.index)
#查看每一列数据统计数目
# print(dataDF.count())
dataDF.rename(columns={'购药时间':'销售时间'},inplace=True)

#2. 缺失值处理
# print('删除缺失值前:', dataDF.shape)
# 使用info查看数据信息,
# print(dataDF.info())
#删除缺失值
dataDF = dataDF.dropna(subset=['销售时间','社保卡号'], how='any')
# print('\n删除缺失值后',dataDF.shape)
# print(dataDF.info())

#3. 数据类型转换
dataDF['销售数量'] = dataDF['销售数量'].astype('float')
dataDF['应收金额'] = dataDF['应收金额'].astype('float')
dataDF['实收金额'] = dataDF['实收金额'].astype('float')
# print(dataDF.dtypes)

#4. 获取“销售时间”这一列
timeSer = dataDF.loc[:, '销售时间']
#对字符串进行分割，提取销售日期
dateSer = splitSaletime(timeSer)
#修改销售时间这一列的值
dataDF.loc[:, '销售时间'] = dateSer

#errors='coerce' 如果原始数据不符合日期的格式，转换后的值为空值NaT
dataDF.loc[:, '销售时间'] = pd.to_datetime(dataDF.loc[:, '销售时间'], format = '%Y-%m-%d', errors='coerce')
# print(dataDF.dtypes)
# print(dataDF.isnull().sum())
dataDF = dataDF.dropna(subset=['销售时间','社保卡号'], how='any')
dataDF = dataDF.reset_index(drop = True)
# dataDF.info()

# 5.排序
dataDF = dataDF.sort_values(by = '销售时间', ascending = True)
dataDF = dataDF.reset_index(drop = True)

# 6. 将'销售数量'这一列小于0的数据排除掉
pop = dataDF.loc[: , '销售数量'] > 0
dataDF = dataDF.loc[pop, :]

#构建模型及数据可视化
# 1:月均消费次数
#删除重复数据
kpil_Df = dataDF.drop_duplicates(subset = ['销售时间','社保卡号'])
totalI = kpil_Df.shape[0]
# print('总消费次数=',totalI)

kpil_Df = kpil_Df.sort_values(by = '销售时间', ascending = True)
kpil_Df = kpil_Df.reset_index(drop = True)
startTime = kpil_Df.loc[0, '销售时间']
endTime = kpil_Df.loc[totalI-1, '销售时间']
#计算月份(天数
dayI = (endTime - startTime).days
monthI = dayI // 30
# print('月份数=', monthI)

#月平均消费次数
kpil_I = totalI // monthI
# print('业务指标1：月均消费次数=', kpil_I)

# 2:月均消费金额 = 总消费金额 / 月份数
totalMoney = dataDF.loc[:, '实收金额'].sum()
monthMoney = totalMoney // monthI
# print('业务指标2：月均消费金额=', monthMoney)

# 3. 客单价= 总消费金额 / 总消费次数
totalTime = dataDF.shape[0]
pct = totalMoney // totalTime
# print('业务指标3：客单价=', pct)

#消费趋势​
mpl.rcParams['font.sans-serif'] = ['SimHei'] # SimHei是黑体的意思
#在操作之前先复制一份
#mpl.rcParams['font.sans-serif'] = ['Songti'] # SimHei是黑体的意思
#font = FontProperties(fname='/Library/Fonts/Songti.ttc') #设置字体
#在操作之前先复制一份数据，防止影响清洗后的数据
groupDF = dataDF
#将'销售时间'设置为index
groupDF.index = groupDF['销售时间']
print(groupDF.head())
gb = groupDF.groupby(groupDF.index)
print(gb)
dayDF = gb.sum()
print(dayDF)
#画图
plt.plot(dayDF['实收金额'])
plt.title('按天消费金额')
plt.xlabel('时间')
plt.ylabel('实收金额')
plt.show()

#查看描述统计信息
# print(dataDF.describe())
# print(dataDF.head())
