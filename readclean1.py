import pandas as pd
import numpy as np


#############################################################
############# reading the train data ########################
#############################################################

bsdata=pd.read_csv('features_train.tsv',sep='\t')

#############################################################
############# cleaning the data #############################
#############################################################

thislist=[]
for col in bsdata.columns:
    if bsdata[col].dtype == 'float64' :
        thislist.append(col)
    
for col in bsdata.columns:
    if bsdata[col].dtype == 'int64' :
        thislist.append(col)

bsdata=bsdata.rename(columns={"gene" : "gene1"})
bsdata=bsdata.rename(columns={"SGD" : "gene"})
thislist.insert(0,'gene')
new1=bsdata[thislist]


#new1=new1.dropna(axis=1,how='any')
new1=new1.drop('len_intron',axis=1)
new1=new1.drop('len_5UTRintron',axis=1)
new1['BC217_MQ_gene'] = new1['BC217_MQ_gene'].fillna(0)
print(new1.shape)
list1=[198, 954, 1341, 1545, 1548, 1768, 1788, 1971, 2486]
for i in list1:
    new1=new1.drop(i)
print(new1.shape)
new1.to_csv('train1.txt', sep='\t',index=False)

