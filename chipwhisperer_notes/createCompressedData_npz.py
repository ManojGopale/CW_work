import sys
import time
import numpy as np
import pandas as pd
import os

########-------------------------------------------------------------------------##########
class Data:
    def npz2compress(self, dataPath, dataSetType, npzSavePath):
        ##Load data for all keys
        df_train = pd.DataFrame()
        for fileNum in range(256):
            print("Started data processing for %d file\n" %(fileNum))
            npzPath = dataPath + "/" + dataSetType + "_" + str(fileNum) + ".npz"
            df = pd.DataFrame(data=np.load(npzPath, allow_pickle=True,)["data"], columns=["trace", "key"])
            df_full = pd.concat([df.trace.apply(pd.Series), df.key.apply(lambda x: x[0])], axis=1)
            if(fileNum==0):
                df_train = df_full
            else:
                df_train = pd.concat((df_full, df_train),axis=0)
            
        ##save to npz format
        if (not os.path.exists(npzSavePath)):
            np.savez_compressed(npzSavePath, data=df_train)
            print("Saved fileNum= %s to %s" %(fileNum, npzSavePath))
        
        print("Done comverting pkl to npz for %s" %(dataSetType))


########-------------------------------------------------------------------------##########

dataDir = "/mnt/hgfs/cw_f303_tinyAES_7000_dataset/"
data= Data()

####-------------Convert pkl to npz---------------------####
npzSavePath = "/mnt/hgfs/compressed_dataset/cw_f303_tinyAES_1200trPerKey.npz"
data.npz2compress(dataDir, "train", npzSavePath)
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
