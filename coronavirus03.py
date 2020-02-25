from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
train = pd.read_csv('china_daily_status_2020-02-21.csv')
test = pd.read_csv('predication03.csv')
test_confirm = pd.read_csv('predication03_confirm.csv')

seqence_train = train.loc[:,['seqence']]
sum_train= train.loc[:,['confirm']]

# linear regression
linear = linear_model.LinearRegression()

# 训练数据
linear.fit(seqence_train,sum_train)

# 预测
# test_seqence = test['seqence'].values.tolist()
predicted_sum = linear.predict(test)


# 预测折线图
fig = plt.figure(figsize=[8.5, 5])
ax = fig.add_subplot(1,1,1)
# print(perdicted_sum)
date = pd.pivot_table(test_confirm,index=['date'],aggfunc='count')
# print(date.index)
ax.plot(date.index,predicted_sum,'-',label='prediction', alpha=1,c='r')
plt.xticks(date.index, rotation=45, fontsize=8)

ax.yaxis.grid(True)

# 散点图
date1 = pd.pivot_table(train,index=['date'],aggfunc='count')
ax.scatter(date1.index,train['confirm'],label='confirm',s=30, alpha=0.5,marker='>')

# 隐藏
for label in ax.get_xticklabels()[1::2]:
    label.set_visible(False)

# 显示多标签
plt.legend()
plt.ylabel('number of people')

# title
ax.set_title('Fit Test')
plt.ylim(0,100000)
plt.show()
