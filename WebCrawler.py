# —*— coding: utf-8 —*—
import requests
import json
import time
import pandas as pd

# 请求的URL
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'

# 伪装请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'referer': 'https://news.qq.com/zt2020/page/feiyan.htm?from=timeline&isappinstalled=0'
}

# 抓取数据
r = requests.get(url % time.time(), headers=headers)

data = json.loads(r.text)
data = json.loads(data['data'])

lastUpdateTime = data['lastUpdateTime']
print('数据更新时间 ' + str(lastUpdateTime))

# part 2. 采集中国历史数据

print('采集中国历史数据...')

china_day_list = data['chinaDayList']

col_names_cd =  ['date','confirm','suspect','dead', 'heal', 'nowConfirm', 'nowSevere','deadRate','healRate']

my_df_cd = pd.DataFrame(columns = col_names_cd)

for day_item in china_day_list:
    date ='2020.'+day_item['date']
    confirm = day_item['confirm']
    suspect = day_item['suspect']
    dead = day_item['dead']
    heal = day_item['heal']
    nowConfirm = day_item['nowConfirm']
    nowSevere = day_item['nowSevere']
    deadRate = day_item['deadRate']
    healRate = day_item['healRate']

    # 向df添加数据
    data_dict = {'date': date,'confirm': confirm,'suspect': suspect,'dead': dead, 'heal': heal, 'nowConfirm': nowConfirm,
                 'nowSevers':nowSevere,'deadRate': deadRate,'healRate':healRate}
    my_df_cd.loc[len(my_df_cd)] = data_dict

my_df_cd.index += 1
my_df_cd.to_csv(r'./china_daily_status_{}.csv'.format(str(lastUpdateTime).split()[0]), encoding='utf_8_sig', header='true')

print('Success')