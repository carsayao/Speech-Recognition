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


#Enum for features
class feature(Enum):
    ZCR = 0
    ENERGY = 1
    ENTENERGY = 2
    SPECSENTROID = 3
    SPECSPREAD = 4
    SPECENT = 5
    SPECFLUX = 6
    SPECROLLOFF = 7
    MFCC1 = 8
    MFCC2 = 9
    MFCC3 = 10
    MFCC4 = 11
    MFCC5 = 12
    MFCC6 = 13
    MFCC7 = 14
    MFCC8 = 15
    MFCC9 = 16
    MFCC10 = 17
    MFCC11 = 18
    MFCC12 = 19
    MFCC13 = 20
    CHROMA1 = 21
    CHROMA2 = 22
    CHROMA3 = 23
    CHROMA4 = 24
    CHROMA5 = 25
    CHROMA6 = 26
    CHROMA7 = 27
    CHROMA8 = 28
    CHROMA9 = 29
    CHROMA10 = 30
    CHROMA11 = 31
    CHROMA12 = 32
    CHROMADEV = 33

#Get current working directory
path = os.getcwd()

#Setup
outputDir = path + "/output" #Output directory
binDir = path + "/output/bin"
inputDir = path + "/data" #Input directory
inputFolders = [] #List of folders with data by name
stdf = pd.DataFrame() #Data frame to hold aggregated short term features
mtdf = pd.DataFrame() #Data frame to hold aggregated mid term features
stbinaries = []
mtbinaries = []

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

try:
    os.mkdir(binDir)

except OSError as e:
    if e.errno == errno.EEXIST:
        print("%s directory already exists" % binDir)
    else:
        print(e.strerror)
        sys.exit(0)
else:
    print ("Successfully created %s " % binDir)

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

        # Get rid of runtime warnings, shouldn't be an issue
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)

        # Short term
            S, sf_names = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
            tempstdf = pd.DataFrame(S)
            stdf = stdf.append(tempstdf)
            stbinaries.append(S)

        # Mid term
        # Found some documentation for matlab audio feature extraction that used these window sizes - seems to work
            M, S, mf_names = audioFeatureExtraction.mtFeatureExtraction(x, Fs, 1.0*Fs, 1.0*Fs, 0.050*Fs, 0.025*Fs)
            # print(M)
            tempmtdf = pd.DataFrame(M)
            # print(tempmtdf)
            mtdf = mtdf.append(tempmtdf)
            mtbinaries.append(M)

    exportst = stdf.to_csv(outputDir+"/"+folder.name+"_stfeatures.csv")
    exportmt = mtdf.to_csv(outputDir+"/"+folder.name+"_mtfeatures.csv")
    # print('stbinaries',stbinaries)
    # stbinaryNp = np.array(stbinaries)
    # print('np.array(stbinaries)',stbinaries)

    # print('mtbinaries',mtbinaries)
    # mtbinaryNp = np.array(mtbinaries)
    # print('np.array(mtbinaries)',mtbinaries)
    # stbinaryNp.tofile(binDir+'/'+folder.name+'_stbinaries')
    # mtbinaryNp.tofile(binDir+'/'+folder.name+'_mtbinaries')

    # stbinaryNp.savetext(binDir+'/'+folder.name+'_stbinaries')
    # mtbinaryNp.savetext(binDir+'/'+folder.name+'_mtbinaries')

    print("%s.csv done" % folder.name)
