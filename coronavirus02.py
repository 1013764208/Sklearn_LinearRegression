from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt

# confirm LinearRegression 预测

# 读取数据
train = pd.read_csv('china_daily_status_2020-02-21.csv')
test = pd.read_csv('predication.csv')
test_confirm = pd.read_csv('predication_confirm.csv')


seqence_train = train.loc[:,['seqence']]
sum_train= train.loc[:,['confirm']]


# linear regression
linear = linear_model.LinearRegression()

# 训练数据
linear.fit(seqence_train,sum_train)

# 预测
# test_seqence = test['seqence'].values.tolist()
perdicted_sum = linear.predict(test)

# 输出
predict_sequnce_number = len(test)
print('predict for',predict_sequnce_number,'sequnce:')
for i in range(0,predict_sequnce_number):
    print('sequnce:',int(test.values[i]),'confirm:',int(perdicted_sum[i]))




# 绘图
fig = plt.figure(figsize=[10, 6])
ax = fig.add_subplot(1,1,1)
# print(perdicted_sum)
date = pd.pivot_table(test_confirm,index=['date'],aggfunc='count')
# print(date.index)
ax.plot(date.index,perdicted_sum,'-',label='confirm', alpha=1)
plt.xticks(date.index, rotation=45, fontsize=8)

plt.ylim(0,100000)
plt.show()
