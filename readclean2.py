import pandas as pd
import numpy as np

###################################################################################
################# reading and cleaning the train data #############################
###################################################################################

bs1=pd.read_csv('bc.tsv',sep='\t')
print(bs1.shape)
bs2=pd.read_csv('yj.tsv',sep='\t')

bs1=bs1.drop(bs1[bs1.isnull().sum(axis=1) > 500].index)
bs2=bs2.drop(bs2[bs2.isnull().sum(axis=1) > 500].index)
bs1=bs1.drop(bs1[bs1.isna().sum(axis=1) > 500].index)
bs2=bs2.drop(bs2[bs2.isna().sum(axis=1) > 500].index)
bs1 = bs1.fillna(0)
bs2 = bs2.fillna(0)
bs1=bs1.drop('LOC_BC217',axis=1)
bs2=bs2.drop('LOC_YJF153',axis=1)
bs2=bs2.drop('gene',axis=1)
bs3=pd.read_csv('train1.txt',sep='\t')
bs3=bs3.drop('gene',axis=1)
print(bs1.shape,bs2.shape,bs3.shape)

bs12 = pd.concat([bs1, bs2], axis=1)
bs12.reset_index(drop=True, inplace=True)
bs3.reset_index(drop=True, inplace=True)

bs123 = pd.concat([bs12, bs3], axis=1)
print(bs123.shape)
bs123.to_csv('train.txt', sep='\t',index=False)

