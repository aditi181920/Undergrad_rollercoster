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

os.chdir('E:/6th sem/predictive_analysis/assignments') #change working directory to read files from this directroy
log=open('E:/6th sem/predictive_analysis/assignments/logg.txt','w+')
log.close()
log=open('E:/6th sem/predictive_analysis/assignments/logg.txt','a')
file_name=sys.argv[1]


if file_name.endswith('csv'):                          #showing exception for wrong file format
  pass
else:
  dt=datetime.now(pytz.timezone('Asia/Kolkata'))
  log.write('Datetime: %s , Exception : Input parameter not correct. Non csv file entered\n'%(dt))
  raise Exception('Wrong input file format')
  
try:
  df=pd.read_csv(file_name)
except FileNotFoundError:                              #showing exception when file not found
  dt=datetime.now(pytz.timezone('Asia/Kolkata'))
  log.write('Datetime: %s , Exception : Input file not found\n'%(dt))
  raise SystemExit
else:
  print(df.head())


ncols=len(df.columns)      #checking for correct number of columns
if ncols==3:
    pass
else:
    dt=datetime.now(pytz.timezone('Asia/Kolkata'))
    log.write('Datetime: %s , Exception : Number of columns in input file not equal to 3\n'%(dt))
    raise Exception('Wrong number of columns in input file')
    
#creating output file
unqsub=df['Submission'].unique()
validsub=unqsub
unqsub=np.insert(unqsub,0,'RollNumber')
#print(unqsub)
dfout=pd.DataFrame(data=None,columns=unqsub)
dfout['RollNumber']=df['RollNumber'].unique()
for x in unqsub:
    if x=='RollNumber':
        pass
    dfout[x]=dfout[x].fillna(0)
    
#print(dfout)

#processing input
df=df.reset_index()  #make sure index pairs with number of rows
dfout=dfout.reset_index()
#print(df)
for i in range(len(df)):
    l=list(df.loc[i])
    #roll=np.array2string(df.loc[i,'RollNumber'])
    #sub=df.loc[i,'Submission']
    #mark=df.loc[i,'Marks']
    roll=str(l[1])
    sub=str(l[2])
    mark=str(l[3])
    #print(roll,sub,mark)
    check=0                #first let's check for all possible exceptions
    if roll.isnumeric():
        pass
    else:
        dt=datetime.now(pytz.timezone('Asia/Kolkata'))
        log.write('Datetime: %s , Exception : Roll number in %d row not an intger\n'%(dt,i))
        check=1
    if sub not in validsub:
        dt=datetime.now(pytz.timezone('Asia/Kolkata'))
        log.write('Datetime: %s , Exception :Submission in%d row not a valid submission\n'%(dt,i))
        check=1
    if check==1:
        continue
    if mark.isnumeric():
        pass
    else:
        mark=-1
        dt=datetime.now(pytz.timezone('Asia/Kolkata'))
        log.write('Datetime: %s , Exception :Marks in%d row missing \n'%(dt,i))
    
    
    #find index of this roll number 
    #iloc[row index,col]
    idx=dfout[dfout['RollNumber']==int(roll)].index
    if mark==-1:
        dfout.loc[idx,sub]=np.NaN
    else:
        dfout.loc[idx,sub]=mark
    #print(idx)
    
print(dfout)
dfout=dfout.drop(columns=['index'])
dfout.to_csv('E:/6th sem/predictive_analysis/assignments/output.csv',index=False)