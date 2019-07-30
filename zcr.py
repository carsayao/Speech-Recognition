##Uses pyAudioAnalysis to extract and plot ZCR
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt

# M
import os
path = "./wavs"
dirs = os.listdir(path)
for file in dirs:

    #Hard coded for one file, need to add loop or argument handling to specify data location
    #[Fs, x] = audioBasicIO.readAudioFile("seven.wav")
    [Fs, x] = audioBasicIO.readAudioFile("./wavs/{}".format(file))
    F, f_names = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
    plt.subplot(2,1,1);
    ##F[0] is the first feature in the vector - ZCR
    plt.plot(F[0,:]);
    plt.xlabel('Frame no');
    plt.ylabel(f_names[0]);
    plt.subplot(2,1,2);

    # M
    plt.plot(F[1,:]);
    plt.xlabel('Frame no'); plt.ylabel(f_names[1]);

    norm_data = (x -x.mean())/x.std()
    plt.plot(x)
    #plt.show()

    # M
    plt.savefig("./plots/zcr/zcr_"+file+".png")
