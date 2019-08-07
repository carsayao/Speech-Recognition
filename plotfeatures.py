from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
from enum import Enum
import scipy.io.wavfile as wav
import scipy.signal as signal
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import warnings
import os, sys, errno


#Get current working directory
path = os.getcwd()

#Setup
outputDir = path + "/output" #Output directory
inputDir = path + "/data" #Input directory
inputFolders = [] #List of folders with data by name
stdf = pd.DataFrame() #Data frame to hold aggregated short term features
mtdf = pd.DataFrame() #Data frame to hold aggregated mid term features

#Get paths for subdirectories of input data folder
for dir in os.scandir(outputDir):
    inputFolders.append(dir)

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_row', 500)
np.set_printoptions(suppress=True)

# importst = pd.read_csv(outputDir + '/bed_stfeatures.csv')
# print(importst)
# importmt = pd.read_csv(outputDir + '/bed_mtfeatures.csv')
importmt = np.loadtxt(outputDir + '/bed_mtfeatures.csv')

# Return a Numpy representation of the DataFrame
# stdf = importst.to_numpy
# mtdf = importmt.to_numpy
# stdf = importst.values
# mtdf = importmt.values
print(mtdf.size//2)
for i in range(mtdf.size//68):
    print(mtdf[i])
    for j in range(mtdf.size//68):
        # print(mtdf[i], 
        print(mtdf[j+68])
# print(stdf)
print(mtdf.size)


            
# tempFromFile = np.fromfile(outputDir+'/'+''+'_stfeatures')
# print('tempFromFile', tempFromFile)


    # exportst = stdf.to_csv(outputDir+"/"+folder.name+"_stfeatures.csv")
    # exportmt = mtdf.to_csv(outputDir+"/"+folder.name+"_mtfeatures.csv")
    # print("%s.csv done" % folder.name)
