import sys
import time
import numpy as np
import pandas as pd
import os

########-------------------------------------------------------------------------##########
class Data:
    def pkl2npz(self, dataPath, tracesPerKey, dataSetType):
        ##Load data for all keys
        npzPath = "/mnt/hgfs/cw_f415_6000_dataset/"
        for key in range(256):
            print("Started data processing for %d key\n" %(key))
            pklPath = dataPath + "/" + dataSetType + "_" + str(key) + ".pkl.zip"
            npzSavePath = npzPath + "/" + dataSetType + "_" + str(key) + ".npz"
            df = pd.read_pickle(pklPath)
            df_full = pd.concat([df.trace.apply(pd.Series), df.key.apply(lambda x: x[0])], axis=1)
            
            ##save to npz format
            if (not os.path.exists(npzSavePath)):
                np.savez_compressed(npzSavePath, data=df_full)
                print("Saved key= %s to %s" %(key, npzSavePath))
            ##Clearing variable
            df_full=None
        
        print("Done comverting pkl to npz for %s" %(dataSetType))


########-------------------------------------------------------------------------##########

dataDir = "/mnt/hgfs/cw_f415_6000_dataset/"
data= Data()

####------------Data Split------------####
trainSize = 7500
devSize = 500
testSize = 500
####----------------------------------####

####-------------Convert pkl to npz---------------------####
data.pkl2npz(dataDir, trainSize, "train")
data.pkl2npz(dataDir, devSize, "dev")
data.pkl2npz(dataDir, testSize, "test")
####----------------------------------####




#M##Saving data in a common path, makes scrit reusable from single architecture to multi-architecture runs.
#M##So, not creating any sub-directories in the folder.
#MnpzTrainPath = "/mnt/hgfs/cw_f303_6000_dataset/cw_f303_6000_train.npz"
#MnpzTestPath  = "/mnt/hgfs/cw_f303_6000_dataset/cw_f303_6000_test.npz"

#M###----------Train + Dev + Test------------------###
#Mx_train = pd.DataFrame()
#My_train = pd.DataFrame()
#Mx_dev = pd.DataFrame()
#My_dev = pd.DataFrame()
#MtrainFlag = False
#MtestFlag = True
#M
#Mif(trainFlag):
#M    print("Train dataset compiation")
#M    x_train, y_train = data.getData(dataDir, trainSize, "train")
#M    x_dev, y_dev = data.getData(dataDir, devSize, "dev")
#M    
#M    x_train, y_train = data.shuffleData(x_train, y_train)
#M    x_dev, y_dev = data.shuffleData(x_dev, y_dev)
#M    
#M    if (not os.path.exists(npzTrainPath)):
#M    	np.savez_compressed(npzTrainPath, x_train=x_train, y_train=y_train, x_dev=x_dev, y_dev=y_dev)
#M    
#Melif (testFlag):
#M    print("Test dataset compiation")
#M    x_test, y_test = data.getData(dataDir, testSize, "test")
#M    x_test, y_test = data.shuffleData(x_test, y_test)
#M
#M    if (not os.path.exists(npzTestPath)):
#M    	np.savez_compressed(npzTestPath, x_test=x_test, y_test=y_test)
#M
#Melse:
#M    print("Mention correct flags")
#M
#M###--------------------------------###
