import os
from os.path import isdir, join
from pathlib import Path
import pandas as pd
import numpy as np
from scipy import signal
from scipy.io import wavfile
import matplotlib.pyplot as plt
import seaborn as sns

def length_of_segment_and_overlap(to_reduce, sample_rate):
    return int(to_reduce * sample_rate / 1000)

def log_spectrogram(audio, sample_rate, window_size=20,
                 step_size=10, eps=1e-10):
    '''
        fs is the sampling frequency of the x time series
        nperseg is the length of each segment
        noverlap is the numebr of points to overlap between segments
        detrend specifies how to detrend each segment
    '''
    frequencies, times, spectrogram = signal.spectrogram(audio,
                                    fs=sample_rate,
                                    nperseg=length_of_segment_and_overlap(window_size, sample_rate),
                                    noverlap=length_of_segment_and_overlap(step_size, sample_rate),
                                    detrend=False)
    return frequencies, times, np.log(spectrogram.T + eps)

def violinplot_frequency(dirs, frequency_index):
    all_spectrograms = [] 
    index = 0
    for direct in dirs:
        all_spectrograms.append([])

        waves = [f for f in os.listdir(join(speech_audio_path, direct)) if
                 f.endswith('.wav')]
        for wav in waves:
            sample_rate, samples = wavfile.read(
                speech_audio_path + direct + '/' + wav)
            frequencies, times, spectrogram = log_spectrogram(samples, sample_rate)
            all_spectrograms[index].extend(spectrogram[:, frequency_index])
        index += 1

    minimum = min([len(spectrogram) for spectrogram in all_spectrograms])
    all_spectrograms = np.array([spectrogram[:minimum] for spectrogram in all_spectrograms])

    plt.xlabel('Frequency')
    plt.ylabel('Words')
    sns.violinplot(data=pd.DataFrame(all_spectrograms.T, columns=dirs), orient='h')
    plt.show()

# Change this variable to whichever dir has the dir of wavs
speech_audio_path='./blerp/'
dirs = [files for files in os.listdir(speech_audio_path) if isdir(join(speech_audio_path, files))]
violinplot_frequency(dirs, 120)
