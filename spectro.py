#Uses scipy to create spectrograms and waveforms
import scipy.io.wavfile as wav
import scipy.signal as signal
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

#Hard coded, assuming that all data files are in ./wavs and are all wav files
#Extra files like .DS_Store on MacOS or other extraneous files break the loop
files = sorted(os.listdir("./wavs"))
columns=5
fig, ax = plt.subplots(int(np.ceil(len(files)/columns))*2,columns,figsize=(50,15))
fig.suptitle("Frequency Spectrum & Oscillogram", x=0.5, y=0.91, fontsize=16)
for idx, file in enumerate(files):
    r,c = idx//columns*2, idx%columns
    rate, data = wav.read("./wavs/{}".format(file))
    f, t, Sxx = signal.spectrogram(data, fs=rate, nperseg=256)
    d = 20*np.log10(Sxx+1e-10)

    major_ticks = np.arange(0,101,1000)
    minor_ticks = np.arange(0,101,500)

    ax[r,c].pcolormesh(t,f,d, vmin=-1e1,vmax=d.max())
    ax[r,c].set_title(file)
    ax[r,c].set_ylabel('Time')
    ax[r,c].set_xticks(t[::16])
    ax[r,c].set_frame_on(False)
    ax[r,c].set_ylabel('Freqs')
    ax[r,c].set_yticks(f[::16])
    ax[r,c].set_ylim(0,4000)

    norm_data = (data -data.mean())/data.std()
    ax[r+1,c].plot(norm_data,lw=1)
    ax[r+1,c].axis("off")
    plt.savefig(file+".png")
