
from pandas.plotting import register_matplotlib_converters
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt

# 图 2 新型冠状病毒疫情数据线性图

# 注册
register_matplotlib_converters()

# read
df = pd.read_csv('china_daily_status_2020-02-21.csv')
test_confirm = pd.read_csv('predication_confirm.csv')


# 获取标签
df_date = df.loc[:,['date']]
df_con = df.loc[:,['confirm']]
df_dead = df.loc[:,['dead']]
df_heal = df.loc[:,['heal']]



# 设置画布
fig = plt.figure(figsize=[10, 6])
ax = fig.add_subplot(1,1,1)

date = pd.pivot_table(df,index=['date'],aggfunc='count')
print(date.index)


# plt
ax.plot(date.index,df['confirm'],'-',label='confirm', alpha=1)
ax.plot(date.index,df['dead'],'-',label='dead', alpha=1)
ax.plot(date.index,df['heal'],'-',label='heal', alpha=1)

# //title
ax.set_title('coronavirus')

# 显示多标签
plt.legend()

# # 标签
plt.xlabel('time')
plt.ylabel('number of people')
ax.yaxis.grid(True)

# 自动旋转标签
plt.xticks(date.index, rotation=45, fontsize=8)

# 隐藏部分坐标轴
for label in ax.get_xticklabels()[1::2]:
    label.set_visible(False)

plt.show()



# ----------------------------------------------------
# 预测后的线性与之前数据比较
# 读取数据
# train = pd.read_csv('china_daily_status_2020-02-21.csv')
# test = pd.read_csv('predication.csv')
# test_confirm = pd.read_csv('predication_confirm.csv')
#
# # df = pd.DataFrame(pd.read_csv('国民经济数据.csv', encoding='gb2312'))
#
# # print(train)
# # 提取对应列
#
# # Remove rows or columns by specifying label names and corresponding axis,
# # or by specifying directly index or column names
# # seqence_train = train.drop(columns=['Cumulativediagnosis'])
# # sum_train = train.drop(columns=['seqence'])
#
# seqence_train = train.loc[:,['seqence']]
# sum_train= train.loc[:,['confirm']]
#
# # print(seqence_train)
# # print(seqence_train)
#
#
# # linear regression
# linear = linear_model.LinearRegression()
#
# # 训练数据
# linear.fit(seqence_train,sum_train)
#
# # 预测
# # test_seqence = test['seqence'].values.tolist()
# perdicted_sum = linear.predict(test)
#
# # 输出
# predict_sequnce_number = len(test)
# print('predict for',predict_sequnce_number,'sequnce:')
# for i in range(0,predict_sequnce_number):
#     print('sequnce:',int(test.values[i]),'confirm:',int(perdicted_sum[i]))
#
#
#
#
# date = pd.pivot_table(test_confirm,index=['date'],aggfunc='count')
# # print(date.index)
# ax.plot(date.index,perdicted_sum,'-',label='confirm', alpha=1)
# plt.show()
#------------------------------------------------------------





