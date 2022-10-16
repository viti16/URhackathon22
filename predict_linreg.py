import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

data=pd.read_csv('train.txt',sep='\t')

xorig=data.drop(["gene","DIFF"],axis=1)
yorig=data["DIFF"]


#################################################################################################
#################### scaling the data ###########################################################
#################################################################################################

scale=StandardScaler()
scale.fit(xorig)
xorigscaled=scale.transform(xorig)



#################################################################################################
#################### principal compnenet analysis (PCA) #########################################
#################################################################################################



nf = 50
pca100 = PCA(n_components=nf)#,random_state=2020)
pca100.fit(xorigscaled)
xorig100 = pca100.transform(xorigscaled)

#################################################################################################
#################### split and predict ##########################################################
#################################################################################################

xtrain, xtest, ytrain, ytest = train_test_split(xorig100, yorig, test_size=1 / 3)

sgdr = LinearRegression()
sgdr.fit(xtrain, ytrain)
ypredict = sgdr.predict(xtest)
rms = mean_squared_error(ytest, ypredict, squared=False)
print(rms)
