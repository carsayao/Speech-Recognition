import matplotlib.pyplot as plt
import librosa
from scipy.io import wavfile

# From https://www.kaggle.com/davids1992/speech-representation-and-data-exploration
path = './wavs/'
filename = '0a7c2a8d_nohash_0.wav'
sample_rate, samples = wavfile.read(str(path) + filename)

S = librosa.feature.melspectrogram(samples, sr=sample_rate, n_mels=128)

log_S = librosa.power_to_db(S, ref=np.max)

plt.figure(figsize=(12, 4))
librosa.display.specshow(log_S, sr=sample_rate, s_axis='time', y_axis='mel')
plt.title('Mel power spectrogram')
plt.colorbar(format='%+02.0f dB')
plt.tight_layout()

