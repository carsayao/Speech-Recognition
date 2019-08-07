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

# Set pandas view options
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_row', 500)
np.set_printoptions(suppress=True)

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

# Number of samples in folder
#samples = len(inputFolders)
#print("samples", samples)

# Instantiate numpy array to have shape of input files (float64)
summed = np.zeros((68, 2))
print(summed)

for folder in inputFolders:
    #print(folder.name)
    for f in os.scandir(folder):
        #print("\t"+f.name)

        importmt = np.loadtxt(outputDir+"/"+folder.name+"/"+f.name, delimiter=',', skiprows=1)
        print("shape", importmt.shape)
        #importmt2 = np.loadtxt(outputDir + '/bed/bed_0b09edd3_nohash_0_mtfeatures.csv', delimiter=',', skiprows=1)
        #summed = importmt+importmt2

#print(importmt)
#print(importmt2)
#print(summed)
#print(summed/2)
#print(importmt.dtype)

# Return a Numpy representation of the DataFrame
# stdf = importst.to_numpy
# mtdf = importmt.to_numpy
# stdf = importst.values
# mtdf = importmt.values
# Size = 
#print(mtdf.size//2)
#for i in range(mtdf.size//68):
#    print(mtdf[i])
#    for j in range(mtdf.size//68):
#        # print(mtdf[i], 
#        print(mtdf[j+68])
## print(stdf)
#print(mtdf.size)


            
# tempFromFile = np.fromfile(outputDir+'/'+''+'_stfeatures')
# print('tempFromFile', tempFromFile)


    # exportst = stdf.to_csv(outputDir+"/"+folder.name+"_stfeatures.csv")
    # exportmt = mtdf.to_csv(outputDir+"/"+folder.name+"_mtfeatures.csv")
    # print("%s.csv done" % folder.name)
