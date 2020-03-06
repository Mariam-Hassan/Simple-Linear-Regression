#The feature and label should be numpy array
#split ratio is the ratio of test

def Mariamz_TrainTestSplitter(X,y, split_ratio):
    import numpy as np
    key=int(np.size(y)*(1-split_ratio))
    print(key)
    X_train= X[0:key]
    Y_train= y[0:key]
    X_test= X[key:]
    Y_test= y[key:]
    return X_train, X_test, Y_train, Y_test 
