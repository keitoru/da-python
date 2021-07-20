#In[1]
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

plt.rcParams['font.family']='Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False

# 1、导入数据集
train = pd.read_csv('data/train.csv')
train.head()

# 2/查看各列的数据类型
train.dtypes

# 3、统计各列的缺失值
train.isnull().sum()

# 4、对年龄缺失值用其中位数进行填充
train['Age'] = train['Age'].fillna(train['Age'].median())
train['Age']

#5、查看各个特征对应的人数分布，
# 即画出存活人数情况、各等级舱人数、男女人数和登船港口人数的条形图。
# 画在一个2*2的图像里。
# plt.subplot(221)
# sns.countplot(x='Survived', data=train)
# plt.title('存活情况')
# plt.subplot(222)
# sns.countplot(x='Pclass', data=train)
# plt.title('各等级舱人数')
# plt.subplot(223)
# sns.countplot(x='Sex', data=train)
# plt.title('男女人数')
# plt.subplot(224)
# sns.countplot(x='Embarked', data=train)
# plt.title('登船港口')
# plt.tight_layout()
#tight_layout会自动调整子图参数，使之填充整个图像区域。这是个实验特性，可能在一些情况下不工作。
# 它仅仅检查坐标轴标签、刻度标签以及标题的部分。

# 6、画一个饼图显示男女人数比例
# male = (train['Sex'] == 'male').sum()
# female = (train['Sex'] == 'female').sum()
# pieData = [male, female]

# plt.pie(pieData, labels = ['Males', 'Females'], explode = (0.15 , 0), startangle = 90, autopct = '%1.1f%%')
# plt.axis('equal')
# plt.title("性别比例")
# plt.tight_layout()
# plt.show()

# 7、用柱状图展示各等级船舱的存活死亡人数
# surviedData = train[['Pclass', 'Survived']].groupby('Pclass')['Survived'].sum()
# sns.countplot(x='Pclass',hue='Survived',data=train)
# plt.title('各船舱的等级的存活情况')

# 8、各等级船舱按性别展示存活情况，用seaborn画条形图
# sns.barplot(x = 'Pclass',y='Survived',hue='Sex',data=train)
# plt.title('各等级船舱的存活情况')

# 9、上船港口与存活人数的统计，画出堆叠条形图
Survived_0 = train.Embarked[train.Survived == 0].value_counts()
Survived_1 = train.Embarked[train.Survived == 1].value_counts()
Pclass_df = pd.DataFrame({'未获救': Survived_0, '获救': Survived_1})
Pclass_df.plot(kind='bar', stacked=True)
plt.title('不同上传港口乘客的获救情况')
plt.xlabel('乘客上传港口')
plt.ylabel('人数')
plt.show()