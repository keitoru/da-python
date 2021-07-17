import pandas as pd
import numpy as np
import datetime
import plotly.express as px

data = pd.read_csv('./file/hotel_bookings.csv')
# print(data.info())
# 数据清洗
# 1.
# nanList = data.isna().sum()
# print(nanList)
# 2. 清理缺省值
data = data.drop(['agent', 'company'], axis=1)
data = data.dropna(subset=['children', 'country'], axis=0)
# 3. 重置索引
data = data.reset_index(drop = True)
# 4. 数据类型
data['children'] = data['children'].astype('int')
# 月份转换为数字
datatime_object = data['arrival_date_month'].str[0:3]
month_number = np.zeros(len(datatime_object), dtype='i1')
# 字符串格式转化为日期格式: “%b”月份的简写; 如4月份为Apr
for i in range(0, len(datatime_object)):
    datatime_object[i] = datetime.datetime.strptime(datatime_object[i], "%b")
    month_number[i] = datatime_object[i].month
# 转为列表格式
month_number = pd.DataFrame(month_number).astype(int)
# 字符拼接
data['arrival_date'] =  data['arrival_date_year'].map(str) + '-' + month_number[0].map(str) + '-' + data['arrival_date_day_of_month'].map(str)

data = data.drop(['arrival_date_year', 'arrival_date_day_of_month', 'arrival_date_month'], axis=1)

# 转为日期类型
data['arrival_date'] = pd.to_datetime(data['arrival_date'])
data['reservation_status_date'] = pd.to_datetime(data['reservation_status_date'])
# print('Datatype of the arrival_date:', data['arrival_date'].dtype)
# print('Datatype of the reservation_status_date:', data['reservation_status_date'].dtype)

data['total_guests'] = data['adults'] + data['children']
data = data[data['total_guests'] != 0]
data['total_stays'] = data['stays_in_weekend_nights'] + data['stays_in_week_nights']

dataResort = data[data['hotel'] == 'Resort Hotel']
NumberOfGuests_Resort = dataResort[['arrival_date', 'total_guests']]
NumberOfGuests_ResortWeekly = data['total_guests'].groupby(dataResort['arrival_date']).sum()
# 按周统计
NumberOfGuests_ResortWeekly = NumberOfGuests_ResortWeekly.resample('w').sum().to_frame()
# print(NumberOfGuests_ResortWeekly)

country_freq = data['country'].value_counts().to_frame()
country_freq.columns = ['count']
fig = px.choropleth(country_freq, color='count',
                    locations=country_freq.index,
                    hover_name=country_freq.index,
                    color_continuous_scale=px.colors.sequential.Teal)
fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
fig.update_layout(title_text='Number of Records by Countries',
                  title_x=0.5, title_font=dict(size=22))  # Location and the font size of the main title
fig.show()
# print(data.info())