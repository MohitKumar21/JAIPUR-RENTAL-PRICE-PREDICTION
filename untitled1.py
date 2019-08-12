# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 22:56:12 2019

@author: Suman

                                                    JaipurRentals

Jaipur’s Real Estate Market is experiencing an incredible resurgence, with property prices soaring by double-digits on an
 yearly basis since 2013. While home owners have a lot of reasons to laugh about, the same cannot be said of people
 looking for a home to buy or rent.

In Jaipur, property rental market is said to be as crazy as property purchasing market. You are new to Jaipur and
 want to rent a decent apartment. Since you have the knowledge of Machine Learning you decided to build a model, 
 that could help you out to get a nice apartment at best price.

Get Your data from various apartment rental sites and move towards the following observation points like:
·       How does the general rental prices distribution looks like? (Graphical representation is appreciated)
·       Which are the hottest areas?
·       Which area would be more interesting to start hunting?
·       Are you able to predict rental price of an apartment?

"""
import pandas as pd

data = pd.read_csv('processed_data.csv')

from collections import Counter
top = Counter(data.location)

data.index = range(data.shape[0])
property_type = data.PropertyType.unique()
loc_price = {}
for i in range(len(data)):
    if loc_price.get(data.iloc[i].location):
        loc_price[ data.iloc[i].location] +=  data.iloc[i].price
    else:
        loc_price[data.iloc[i].location] = data.iloc[i].price

avg_price = {}
for items in loc_price.keys():
    avg_price[items] = loc_price.get(items)/top[items]
    
location = loc_price.keys()

#import matplotlib.pyplot as plt
#
#plt.figure(figsize=(30,10))
#plt.bar(height = avg_price.values(), x=avg_price.keys())
#plt.margins(x=0)
#plt.xticks(fontsize = 10,fontname = "Comic Sans MS", rotation = 90)
#plt.xlabel('Locations')
#plt.ylabel('Average Price')
#plt.savefig('chart.svg',format='svg',dpi=1500,bbox_inches = 'tight')
#plt.show()


#·       Which are the hottest areas?
import operator

a = dict(sorted(avg_price.items(), key=operator.itemgetter(1), reverse=True)[:10])

#print('Top 10 Locations\n')
#for item in a.keys():
#    print(item.title())
    
    
#    Which area would be more interesting to start hunting?

hunt = pd.DataFrame()
for loc,num in top.most_common(10):
    temp = []
    for i in range(1,11):
        try:
            temp.append(str(str(i)+' BHK Average rate: '+str(int(data['price'][(data.location==loc) & (data.BHK==i)].mean()))))
        except:
            temp.append(str(str(i)+' BHK Not Available'))
    hunt[loc] = temp

#
#hunt3 = pd.DataFrame()
#labels = []
#for loc,num in top.most_common(10):
#    top3price = []
#    for i in range(1,4):
#        top3price.append(int(data['price'][(data.location==loc) & (data.BHK==i)].mean()))
#    hunt3[loc] = top3price
#    labels.append(loc)
#    
#    
#newhunt3 = pd.DataFrame({'one':hunt3.iloc[0:1].values[0],'two':hunt3.iloc[1:2].values[0],'three':hunt3.iloc[2:3].values[0]})
#
#import matplotlib.pyplot as plt
#
#x = [1,2,3,4,5,6,7,8,9,10]
#y = newhunt3.one.values
#plt.plot(x, y, label='1 BHK',marker='o')
#y = newhunt3.two.values
#plt.plot(x, y, label='2 BHK',marker='o')
#y = newhunt3.three.values
#plt.plot(x, y, label='3 BHK',marker='o')
#
#plt.xticks(x, labels, rotation='vertical')
#plt.xlabel('Locations')
#plt.ylabel('Price')
#plt.margins(0.1)
#plt.subplots_adjust(bottom=0.15)
#plt.legend()
#plt.savefig('top10loc1.svg',dpi=1500,bbox_inches = 'tight')
#plt.show()



import pickle

with open('model.pkl','rb') as f1:
    model = pickle.load(f1)

