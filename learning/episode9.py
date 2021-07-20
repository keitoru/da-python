#In[1]
from collections import OrderedDict
import pandas as pd
from sklearn import model_selection
examDict={
    '学习时间':[0.50,0.75,1.00,1.25,1.50,1.75,1.75,2.00,2.25,2.50,2.75,3.00,3.25,3.50,4.00,4.25,4.50,4.75,5.00,5.50],
    '分数':    [10,  22,  13,  43,  20,  22,  33,  50,  62,48,  55,  75,  62,  73,  81,  76,  64,  82,  90,  93]
}
examOrderDict = OrderedDict(examDict)
exam = pd.DataFrame(examOrderDict)
exam.head()


#### 2 看看适不适合用线性回归的模型（通过画图）
#接下来我们先大致看一下特征和标签之间的关系
#然后来判断是否适合使用简单线性回归模型
#如果不适合，就换用其他模型
#这里是举例，肯定可以用的
#特征是学习时间，标签是分数
#用散点图看一下大致情况

#从dataframe中把标签和特征导出来
exam_X = exam['学习时间']
exam_Y = exam['分数']

import matplotlib.pylab as plt
#绘制散点图
# plt.scatter(exam_X, exam_Y, color='green')
# #设定X,Y轴标签和title
# plt.ylabel('scores')
# plt.xlabel('times')
# plt.title('exam data')
# plt.show()

#### 3 分割数据
# 这里不能把这个数据集都作为训练数据集，那样的话就没有数据来测试一下我们的模型好坏了，
# 所以需要把数据集分割一下，要用到一个函数。

#train_test_split函数可以在样本数据集中随机的选取测试集与训练集
#比例可以自己指定
#第一个参数为特征，第二个参数为标签

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(exam_X, exam_Y, train_size = 0.8)
X_train.head()
X_train.shape
#可以发现训练集是16行一列的数据，测试集是四行一列，符合切分比例

#### 4 导入模型

#首先，改变一下数组的形状
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)
#从skl中导入线性回归的模型
from sklearn.linear_model import LinearRegression
#创建一个模型
model = LinearRegression()
#训练一下
model.fit(X_train, Y_train)

#因为线性回归一般方程为y = a+bx
#b为斜率，a为截距
#截距用intercept_方法获得
#斜率用model.coef_方法获得
a = model.intercept_
b = model.coef_
a = float(a)
b = float(b)
print('该模型的简单线性回归方程为y = {} + {} * x'.format(a, b))

#### 5 评估模型
#绘制散点图
plt.scatter(exam_X, exam_Y, color='green')
#设定X,Y轴标签和title
plt.ylabel('scores')
plt.xlabel('times')
plt.title('exam data')

#绘制最佳拟合曲线
Y_train_pred = model.predict(X_train)
plt.plot(X_train, Y_train_pred, color = 'black', label = 'best line')
#来个图例
plt.legend(loc = 2)
plt.show()

# 但是仅仅通过拟合曲线我们是无法准确判断模型的拟合程度的，我们还需要更加具体的评判方式。

# 在线性回归中，我们通过决定系数 R^{2} 来判别，这个数值越接近于1，说明模型的拟合度越好

# ，通过测试数据来判断一下模型的拟合程度。
model.score(X_test, Y_test)