#Uses scipy to create spectrograms and waveforms
import scipy.io.wavfile as wav
import scipy.signal as signal
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

# Get full path to file's directory
path = os.path.dirname(os.path.realpath(__file__))

#Setup
outputDir = path + "/../../output/plots" #Output directory
inputDir = path + "/../../data" #Input directory
inputFolders = [] #List of folders with data by name

#Get paths for subdirectories of input data folder
for dir in os.scandir(inputDir):
    # Skip over stfeatures
    if "stfeatures" in dir.name:
        continue
    inputFolders.append(dir)
    print("dir", dir)

#Hard coded, assuming that all data files are in dirs in /data and are all wav files
#Extra files like .DS_Store on MacOS or other extraneous files break the loop

columns=5
for folder in inputFolders:
    print("folder",folder.name)
    files = sorted(os.listdir(folder))

    fig, ax = plt.subplots(int(np.ceil(len(files)/columns))*2,columns,figsize=(50,15))
    fig.suptitle("Frequency Spectrum & Oscillogram", x=0.5, y=0.91, fontsize=16)
    for idx, file in enumerate(files):
        try:
            print("file",file.name)
        r = idx//columns*2
        c = idx%columns
        rate, data = wav.read(folder+"{}".format(file))
        f, t, Sxx = signal.spectrogram(data, fs=rate)
        d = 20*np.log10(Sxx+1e-10)
        ax[r,c].pcolormesh(t,f,d, vmin=-1e1,vmax=d.max())
        ax[r,c].set_title(file);
        ax[r,c].set_xticks([])
        ax[r,c].set_frame_on(False)
        ax[r,c].set_yticks([])

        norm_data = (data -data.mean())/data.std()
        ax[r+1,c].plot(norm_data,lw=1)
        ax[r+1,c].axis("off")
        #plt.savefig(file+".png")
        # Save to /spectro
        plt.savefig(outputDir+"/plots/spectro/"+file+".png")
