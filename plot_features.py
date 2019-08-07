# Make sure to run collect_features.py first

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
pd.set_option("display.width", 1000)
pd.set_option("display.max_columns", 500)
pd.set_option("display.max_row", 500)
np.set_printoptions(suppress=True)

#Get current working directory
path = os.getcwd()

#Setup
outputDir = path + "/output" #Output directory
inputDir = path + "/data" #Input directory
inputFolders = [] #List of folders with data by name

#Get paths for subdirectories of input data folder
for dir in os.scandir(outputDir):
    # Skip over stfeatures
    if "stfeatures" in dir.name:
        continue
    inputFolders.append(dir)

for folder in inputFolders:
    # Instantiate numpy array
    summed = np.zeros((68, 1))

    print("/"+folder.name)
    print("\t"+"Processing...")
    
    # Number of samples in folder
    samples = 0
    for f in os.scandir(folder):
        # Skip over
        if "mean" in f.name:
            continue
        
        # Import mt csv, reshape for compatibility in array operations
        importmt = np.loadtxt(outputDir+"/"+folder.name+"/"+f.name, delimiter=",", skiprows=1)
        importmt = importmt.reshape((68,1))
        summed = summed + importmt
        samples = samples + 1
        print("\t\t"+f.name)
    
    summed = summed / samples
    # Save to folder name
    np.savetxt(outputDir+"/"+folder.name+"/"+folder.name+"_"+"mean"+"_mtfeatures.csv", summed)
    print ("Successfully saved %s " % folder.name+"_"+"mean"+"_mtfeatures.csv\n")

