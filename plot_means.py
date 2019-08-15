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

means = pd.DataFrame()
names = []
i = 1

path = os.path.dirname(os.path.realpath(__file__))

inputDir = path + "/mt_feat_means"

for csv in os.scandir(inputDir):
    temp = pd.read_csv(csv)
    means = means.append(temp)
    names.append(csv.name)

print(means)

figure, axs = plt.subplots(2,2)
axs[0,0].set_title("zcr vs energy")
for f in names:
    axs[0,0].plot(means.get_value((feature.ZCR.value * i), 0), means.get_value(feature.ENERGY.value * i), 0)
    axs[0,0].annotate(names[i], (means.iloc[feature.ZCR.value * i]), (means.iloc[feature.ENERGY.value * i]))
    i = i + 1
i = 1

axs[0,1].set_title("energy vs spectral sentroid")
for f in names:
    axs[0,1].plot(means.iloc[feature.ENERGY.value * i], means.iloc[feature.SPECSENTROID.value * i])
    axs[0,1].annotate(names[i], (means.iloc[feature.ENERGY.value * i]), (means.iloc[feature.SPECSENTROID.value * i]))
    i = i + 1
i = 1

axs[1,0].set_title("entropy of energy vs spectral flux")
for f in names:
    axs[1,0].plot(means.iloc[feature.ENTENERGY.value * i], means.iloc[feature.SPECFLUX.value * i])
    axs[1,0].annotate(names[i], (means.iloc[feature.ENTENERGY.value * i]), (means.iloc[feature.SPECFLUX.value * i]))
    i = i + 1
i = 1

axs[1,1].set_title("energy vs spectral flux")
for f in names:
    axs[1,1].plot(means.iloc[feature.ENERGY.value * i], means.iloc[feature.SPECFLUX.value * i])
    axs[1,1].annotate(names[i], (means.iloc[feature.ENERGY.value * i]), (means.iloc[feature.SPECFLUX.value * i]))
    i = i + 1
i = 1

plt.show()
