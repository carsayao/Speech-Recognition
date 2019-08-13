#
# mean_features.py
#


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

# Get full path to file's directory
path = os.path.dirname(os.path.realpath(__file__))

#Setup
inputDir = path + "/csvs"
# inputDir = path + "/../../output/csvs"
inputFolders = [] #List of folders with data by name

try:
    os.mkdir(path+"/../test/mtfeatures")
except:
    print()

#Get paths for subdirectories of input data folder
for dir in os.scandir(inputDir):
    # Skip over stfeatures
    if "stfeatures" in dir.name:
        continue
    inputFolders.append(dir)

for folder in inputFolders:
    # Skip empty folders
    dirContents = os.listdir(folder)
    if len(dirContents) == 0:
        print("/%s is empty" % folder.name)
        continue
    # Instantiate numpy array
    summed = np.zeros((68, 1))

    print("/"+folder.name)
    print("Processing...")
    
    # Number of samples in folder
    samples = 0
    for f in os.scandir(folder):
        # Skip over
        if "mean" in f.name:
            continue
        # print("isfile(f)",os.path.isfile(f))
        
        # Import mt csv, reshape for compatibility in array operations
        print(f.name)
        importmt = np.loadtxt(inputDir+"/"+folder.name+"/"+f.name, delimiter=",", skiprows=1)
        importmt = importmt.reshape((68,1))
        summed = summed + importmt
        samples = samples + 1
    
    summed = summed / samples
    # Save to folder name
    #np.savetxt(outputDir+"/"+folder.name+"/"+folder.name+"_"+"mean"+"_mtfeatures.csv", summed)
    # Output to test folder
    np.savetxt(path+"/mtfeatures/"+folder.name+".csv", summed)
    print ("Successfully saved %s " % folder.name+"_"+"mean"+"_mtfeatures.csv\n")

