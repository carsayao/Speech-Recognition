from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
from enum import Enum
import scipy.io.wavfile as wav
import scipy.signal as signal
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import os, sys, errno

#Enum for features
feat = Enum('ZCR',
            'ENERGY',
            'ENTENERGY',
            'SPECSENTROID',
            'SPECSPREAD',
            'SPECENT',
            'SPECFLUX',
            'SPECROLLOFF',
            'MFCC1',
            'MFCC2',
            'MFCC3',
            'MFCC4',
            'MFCC5',
            'MFCC6',
            'MFCC7',
            'MFCC8',
            'MFCC9',
            'MFCC10',
            'MFCC11',
            'MFCC12',
            'MFCC13',
            'CHROMA1'
            'CHROMA2'
            'CHROMA3'
            'CHROMA4'
            'CHROMA5'
            'CHROMA6'
            'CHROMA7'
            'CHROMA8'
            'CHROMA9'
            'CHROMA10'
            'CHROMA11'
            'CHROMA12'
            'CHROMADEV')

#Get current working directory
path = os.getcwd()

#Setup
outputDir = path + "/output" #Output directory
inputDir = path + "/data" #Input directory
inputFolders = [] #List of folders with data by name
df = pd.DataFrame() #Data frame to hold aggregated features

#Make output folder, catch error if it exists already, and print error
#Abort on other OS errors
try:
    os.mkdir(outputDir)

except OSError as e:
    if e.errno == errno.EEXIST:
        print("Output directory already exists")
    else:
        print(e.strerror)
        sys.exit(0)
else:
    print ("Successfully created %s " % outputDir)

#Get paths for subdirectories of input data folder
for dir in os.scandir(inputDir):
    inputFolders.append(dir)

#Go through folders extracting features and putting them in a dataframe
for folder in inputFolders:
    for clip in os.scandir(folder):
        try:
            [Fs, x] = audioBasicIO.readAudioFile(clip.path)
        except:
            print("Error processing %s " % clip)
            sys.exit(0)

        F, f_names = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
        tempdf = pd.DataFrame(F)
        df = df.append(tempdf)

    export = df.to_csv(outputDir+"/"+folder.name+"_features.csv")
    print("%s.csv done" % folder.name)
