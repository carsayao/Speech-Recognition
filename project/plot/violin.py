##Uses pyAudioANalysis to extract featrues and currently creates stacked violin plots
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns

#Set features to extract from files, see documentaion for feature extraction
#in pyAudioAnalysis. Ex. 0 = zero crossing rate, 1 = energy, etc.
feature1 = 0
feature2 = 0
#For use later to push features into arrays for plotting, not implemented
F1 = np.array([])
F2 = np.array([])
#Hard coded, assuming that all data files are in ./wavs and are all wav files
#Extra files like .DS_Store on MacOS or other extraneous files break the loop
for file in os.listdir("./wavs/"):
    fname = os.fsdecode(file)
    [Fs, x] = audioBasicIO.readAudioFile("./wavs/" + fname)
    F, f_names = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
    sns.set(style="whitegrid")
    vplot = sns.violinplot(F[feature1,:], orient="v")
    
    # M
    plt.savefig("./plots/violin/violin_"+file+".png")

#plt.show()
