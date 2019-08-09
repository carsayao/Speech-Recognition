from pyAudioAnalysis import audioAnalysis as aA
from enum import Enum
import scipy.io.wavfile as wav
import scipy.signal as signal
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import warnings
import os, sys, errno

# Get full path to file's directory
path = os.path.dirname(os.path.realpath(__file__))
inputDir = path + "/testData"

aA.featureVisualizationDirWrapper(inputDir)
