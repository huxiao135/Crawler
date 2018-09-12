#! *-- coding:utf-8 --*
#by hu
#draw the crawled data with a pie chart
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']#让图表显示中文
data=pd.read_csv('domo.csv')
a,b,c,d,e=0,0,0,0,0
labels=['大于20万\n greater than 200000','20万-10万\n 200000-100000','10万-5万\n 100000-50000','5万-1万\n 50000-10000','1万以下\n less than 10000']
colors=['yellow','green','red','blue']

#统计各分类的个数
#count the number of categories
for num in data['see_num']:
    head_num=num.replace('万','')
    if float(head_num) > 20:
        a=a+1
    elif 20>=float(head_num)>10:
        b=b+1
    elif 10>=float(head_num)>5:
        c=c+1
    elif 5>=float(head_num)>1:
        d=d+1
    elif 1>=float(head_num):
        e=e+1
#draw chart
plt.title('see the number of hosts by category ratio\n 观看主播人数分类占比')
plt.pie([a,b,c,d,e],labels=labels,colors=colors,autopct='%1.1f%%')
plt.axis('equal')
plt.show()
