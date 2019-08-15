import os
from os.path import isdir, join
from pathlib import Path
import pandas as pd
import numpy as np
from scipy import signal
from scipy.io import wavfile
from scipy.linalg import logm
import matplotlib.pyplot as plt
import seaborn as sns

''' 
    We use a logarithmic scale because that is essentially how 
    pitch is perceived (the distance between octaves in the double
    from C(1) -> C'(2) -> C''(4)
'''
def log_spectrogram(audio, sample_rate):
    frequencies, times, spectrogram = signal.spectrogram(audio,
                                    fs=sample_rate,
                                    detrend=False)
    return frequencies, times, np.log(spectrogram.T + .0000000001)

def violinplot_frequency(dirs, frequency_index):
    all_spectrograms = [] 
    index = 0
    for direct in dirs:
        all_spectrograms.append([])

        waves = [f for f in os.listdir(join(speech_audio_path, direct)) if f.endswith('.wav')]
        for wav in waves[:100]:
            sample_rate, audio = wavfile.read(speech_audio_path + direct + '/' + wav)
            freqs, times, spectrogram = log_spectrogram(audio, sample_rate)

            frequencies, times, spectrogram = log_spectrogram(audio, sample_rate)
            all_spectrograms[index].extend(spectrogram[:, frequency_index])
        index += 1

    minimum = min([len(spectrogram) for spectrogram in all_spectrograms])
    all_spectrograms = np.array([spectrogram[:minimum] for spectrogram in all_spectrograms])

    plt.title('Frequency ' + str(frequencies[frequency_index]) + ' Hz')
    plt.xlabel('Amount of frequency')
    plt.ylabel('Words')
    #sns.violinplot(data=pd.DataFrame(all_spectrograms.T, columns=dirs), orient='h' )
    sns.boxplot(data=pd.DataFrame(all_spectrograms.T, columns=dirs), orient='h' )
    plt.show()

'''
Getting an error about dimensions not matching up...
def avg_wav(directory):
filename = './speech_commands_v0.01/go/9f869f70_nohash_0.wav'
sample_rate, audio = wavfile.read(filename)
freqs, times, spectrogram = signal.spectrogram(audio, sample_rate, detrend=False)

plt.title('Raw wave of ' + str(filename))
plt.ylabel('Amplitude')
plt.plot(np.linspace(0, sample_rate/len(audio), sample_rate), audio)
plt.show()
''' 

# Change this variable to whichever dir has the dir of wavs
speech_audio_path='./blerp/'
dirs = [files for files in os.listdir(speech_audio_path) if isdir(join(speech_audio_path, files))]

violinplot_frequency(dirs, 1)
#violinplot_frequency(dirs, 20)
#violinplot_frequency(dirs, 60)
#violinplot_frequency(dirs, 120)
