
"""
@author: 
ADITI
101903527
2CO20
"""
import pandas as pd
import os
import sys
import pytz
from pycaret.datasets import get_data
from pycaret.classification import *

#os.getcwd()
#os.chdir('/content/drive/Othercomputers/My Laptop/New Volume [E]/6th sem/predictive_analysis/assignments/ass3')

file_name=sys.argv[1]

#file_name='/content/drive/Othercomputers/My Laptop/New Volume [E]/6th sem/predictive_analysis/assignments/ass3/101903527.csv'
df=pd.read_csv(file_name,nrows=50)
df=df.drop(['Peptide Sequence'],axis=1)
print(df.head())
from pycaret.classification import *
setup(data=df, target='target',silent=True)
cm=compare_models()
print(cm)
df2=pull()
print(df2)
dfmod=df2['Model']
dfacc=df2['Accuracy']

#Q1

setup(data=df, target='target', normalize = True, normalize_method = 'zscore', silent=True)
cm = compare_models()
df3=pull()
dfacc1=df3['Accuracy']

setup(data=df, target='target', normalize = True, normalize_method = 'minmax', silent=True)
cm = compare_models()
df4=pull()
dfacc2=df4['Accuracy']


setup(data=df, target='target', normalize = True, normalize_method = 'maxabs', silent=True)
cm = compare_models()
df5=pull()
dfacc3=df5['Accuracy']

setup(data=df, target='target', normalize = True, normalize_method = 'robust', silent=True)
cm = compare_models()
df6=pull()
dfacc4=df6['Accuracy']

dfout=pd.DataFrame({
    'Accuracy wihout Normalization':list(dfacc),
    'Accuracy with zscore Normalization':list(dfacc1),
    'Accuracy with minmax Normalization':list(dfacc2),
    'Accuracy with maxabs Normalization':list(dfacc3),
    'Accuracy with robust Normalization':list(dfacc4),
},index=dfmod)
print(dfout)

dfout.to_csv('output-101903527-Normalization.csv')

#Q2


setup(data=df, target='target',feature_selection = True, feature_selection_method = 'classic', feature_selection_threshold = 0.2, silent=True)
cm = compare_models()
df3=pull()
dfacc1=df3['Accuracy']
setup(data=df, target='target',feature_selection = True, feature_selection_method = 'classic', feature_selection_threshold = 0.5, silent=True)
cm = compare_models()
df4=pull()
dfacc2=df4['Accuracy']
setup(data=df, target='target',feature_selection = True, feature_selection_method = 'boruta', feature_selection_threshold = 0.2, silent=True)
cm = compare_models()
df5=pull()
dfacc3=df5['Accuracy']
setup(data=df, target='target',feature_selection = True, feature_selection_method = 'boruta', feature_selection_threshold = 0.5, silent=True)
cm = compare_models()
df6=pull()
dfacc4=df6['Accuracy']

dfout=pd.DataFrame({
    'Accuracy wihout Feature Selection':list(dfacc),
    'Accuracy with 0.2 Classic Feature Selection':list(dfacc1),
    'Accuracy with 0.5 Classic Feature Selection':list(dfacc2),
    'Accuracy with 0.2 Boruta Feature Selection':list(dfacc3),
    'Accuracy with 0.5 Boruta Feature Selection':list(dfacc4),
},index=dfmod)
print(dfout)
dfout.to_csv('output-101903527-FeatureSelection.csv')

#Q3


setup(data=df, target='target', remove_outliers = True, outliers_threshold = 0.02, silent=True)
cm = compare_models()
df3=pull()
dfacc1=df3['Accuracy']
setup(data=df, target='target', remove_outliers = True, outliers_threshold = 0.04, silent=True)
cm = compare_models()
df4=pull()
dfacc2=df4['Accuracy']
setup(data=df, target='target', remove_outliers = True, outliers_threshold = 0.06, silent=True)
cm = compare_models()
df5=pull()
dfacc3=df5['Accuracy']
setup(data=df, target='target', remove_outliers = True, outliers_threshold = 0.08, silent=True)
cm = compare_models()
df6=pull()
dfacc4=df6['Accuracy']

dfout=pd.DataFrame({
    'Accuracy wihout Outlier Removal':list(dfacc),
    'Accuracy with 0.2 threshold Outlier Removal':list(dfacc1),
    'Accuracy with 0.4 threshold Outlier Removal':list(dfacc2),
    'Accuracy with 0.6 threshold Outlier Removal':list(dfacc3),
    'Accuracy with 0.8 threshold Outlier Removal':list(dfacc4),
},index=dfmod)
print(dfout)
dfout.to_csv('output-101903527-OutlierRemoval.csv')

#Q4


setup(data=df, target='target', pca = True, pca_method = 'linear', silent=True)
cm = compare_models()
df3=pull()
dfacc1=df3['Accuracy']
setup(data=df, target='target',pca = True, pca_method = 'kernel', silent=True)
cm = compare_models()
df4=pull()
dfacc2=df4['Accuracy']
setup(data=df, target='target',pca = True, pca_method = 'incremental', silent=True)
cm = compare_models()
df5=pull()
dfacc3=df5['Accuracy']

dfout=pd.DataFrame({
    'Accuracy wihout PCA':list(dfacc),
    'Accuracy with linear PCA':list(dfacc1),
    'Accuracy with kernel PCA':list(dfacc2),
    'Accuracy with incremental PCA':list(dfacc3),
},index=dfmod)
print(dfout)
dfout.to_csv('output-101903527-PCA.csv')



setup(data=df, target='target',silent=True)
rfModel = create_model('rf')

#Q5

plot_model(rfModel,plot='confusion_matrix',save=True)
os.rename('Confusion Matrix.png','output-101903527-ConfusionMatrix.png')

#Q6

plot_model(rfModel,plot='learning',save=True)
os.rename('Learning Curve.png','output-101903527-Learning Curve.png')

#Q7

plot_model(rfModel,plot='auc',save=True)
os.rename('AUC.png','output-101903527-AUC.png')


# Q8

plot_model(rfModel, plot='boundary',save=True)
os.rename('Decision Boundary.png','output-101903527-Decision Boundary.png')


# Q9

plot_model(rfModel, plot='feature',save=True)
os.rename('Feature Importance.png','output-101903527-Feature Importance.png')