"""
 created by:
     101903527
     ADITI
     COE20
"""
import numpy as np
import pandas as pd
from datetime import datetime,timezone
import os
import sys
import pytz
import statistics as stat
import matplotlib.pyplot as plt
from collections import Counter


os.chdir('E:/6th sem/predictive_analysis/assignments') #change working directory to read files from this directroy
n=len(sys.argv)
log=open('E:/6th sem/predictive_analysis/assignments/logg.txt','a')
file_name=sys.argv[1]
if file_name.endswith('csv'):                          #showing exception for wrong file format
  pass
else:
  dt=datetime.now(pytz.timezone('Asia/Kolkata'))
  log.write('Datetime: %s , Exception : Output file parameter not correct. Non csv file entered\n'%(dt))
  raise Exception('Wrong input file format')
try:
  df=pd.read_csv(file_name)
except FileNotFoundError:                              #showing exception when file not found
  dt=datetime.now(pytz.timezone('Asia/Kolkata'))
  log.write('Datetime: %s , Exception : Output file not found\n'%(dt))
else:
  print(df.head())
  

df.reset_index()
tot=[]
for i in range(len(df)):
    l=list(df.loc[i])
    checkna=0
    sum=0
    for j in range(1,6):
        add=0 
        print(l[j])
        if np.isnan(l[j]):
            #print('ok')
            checkna=1
        else:
            add=l[j]
        sum+=int(add)
    if sum==0 and checkna==1:
        tot.append(np.NaN)
    else:
        tot.append(sum)
    
print(tot)
newdf=df
newdf['Tot']=tot
print(newdf)


#generate statistics
stats=open('E:/6th sem/predictive_analysis/assignments/statistics.txt','w+')
stats.close()
stats=open('E:/6th sem/predictive_analysis/assignments/statistics.txt','a')
stats.write('Statistics of current data:\n')
cols=list(newdf.columns)
print(cols)
for i in range(len(cols)):
    if i==0:
        continue
    stats.write('----Statistics of %s-------\n'%cols[i])
    stats.write('Mean: %f\n'%(newdf[cols[i]].mean()))
    stats.write('Median: %f\n'%(newdf[cols[i]].median()))
    stats.write('Min marks:%d\n'%(newdf[cols[i]].min()))
    stats.write('Max marks:%d\n'%(newdf[cols[i]].max()))
    stats.write('Std deviation:%f\n'%(stat.stdev(newdf[cols[i]].fillna(0))))
    stats.write('Count of missing values:%d\n\n'%(newdf[cols[i]].isnull().count()))
    stats.write('Statistical summary:\n')
    stats.write(str(newdf[cols[i]].describe()))
    stats.write('\n\n')

#making different plots
#plt.savefig('name.png')
fig = plt.gcf()
fig.set_size_inches(15, 10,forward=True)
label=[]

for i in range(len(cols)):
    if i==0:
        continue
    label.append(cols[i])
    


for i in range(len(cols)):
    if i==0:
        continue
    #histogram
    plt.title('Histogram for %s'%cols[i])
    newdf[cols[i]].fillna(0).plot(kind='hist',bins=15)
    plt.xlabel('Marks distribution')
    plt.ylabel('Frequency')
    #plt.show()
    plt.savefig('E:/6th sem/predictive_analysis/assignments/101903527-histogram-%s.png'%cols[i])
    plt.clf()
    plt.cla()
    
    #box plots
    plt.boxplot(newdf[cols[i]].fillna(0))
    plt.title('Boxplot for %s'%cols[i])
    #plt.show()
    plt.savefig('E:/6th sem/predictive_analysis/assignments/101903527-boxplot-%s.png'%cols[i])
    plt.clf()
    plt.cla()
    
    #line plot
    plt.plot(newdf[cols[0]],newdf[cols[i]].fillna(0),linestyle='dashed')
    plt.title('Line plot for %s'%cols[i])
    series = newdf[cols[i]]
    plt.plot(newdf.iloc[:, 0], series)
    plt.xlabel('RollNumber')
    plt.ylabel(cols[i])
    plt.tight_layout()
    #plt.show()
    #fig.savefig('test2png.png', dpi=100)
    plt.savefig('E:/6th sem/predictive_analysis/assignments/101903527-line-%s.png'%cols[i],dpi=100)
    plt.clf()
    plt.cla()
    
    #scatter plot
    #plt.scatter(marksrange, newdf[cols[i]], label=cols[i], color='g')
    #plt.title('Scatter plot for %s'%cols[i])
    #plt.show()
    
    #pie chart
    series = newdf[cols[i]]
    series.dropna(inplace=True)
    counter = dict(Counter(series))
    plt.pie(counter.values(), labels=counter.keys())
    plt.legend()
    plt.title('Pie chart for %s'%cols[i])
    plt.savefig('E:/6th sem/predictive_analysis/assignments/101903527-pie-%s.png'%cols[i])
    #plt.show()
    plt.clf()
    plt.cla()
    