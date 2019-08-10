from __future__ import print_function
import shutil, struct, simplejson
from scipy.spatial import distance
from pylab import *
import ntpath
import sklearn
import sklearn.discriminant_analysis
import os
import sys
from pyAudioAnalysis import audioFeatureExtraction as aF
from pyAudioAnalysis import audioTrainTest as aT
from pyAudioAnalysis import audioVisualization as aV


def main():


    # inputFolders = []
    # for dir in os.scandir(inputDir):
    #     if len(os.listdir(dir)) == 0:
    #         continue
    #     inputFolders.append(dir)
    # print(inputFolders)
    # dirsWavFeatureExtraction([)

    # mtnoav, _, _ = aF.dirWavFeatureExtractionNoAveraging(path+"/testdata",1.0,1.0,0.050,0.025)

    # mtav, _, _ = aF.dirWavFeatureExtraction(path+"/testdata",1.0,1.0,0.050,0.025)
    # subbed = mtnoav - mtav
    # print(subbed)
    # print("allMtFeatures", allMtFeatures)
    # print("Ys", Ys)
    # print("wavFileList", wavFilesList)
    
    def mtPca(allMtFeatures, wavFilesList):

        if allMtFeatures.shape[0]==0:
            print("Error: No data found! Check input folder")
            return
        
        namesCategoryToVisualize = [ntpath.basename(w).replace('.wav','').split(" --- ")[0] for w in wavFilesList]; 
        namesToVisualize = [ntpath.basename(w).replace('.wav','') for w in wavFilesList]; 

        (F, MEAN, STD) = aT.normalizeFeatures([allMtFeatures])
        F = np.concatenate(F)
        
        # check that the new PCA dimension is at most equal to the number of samples
        K1 = 2
        K2 = 10
        if K1 > F.shape[0]:
            K1 = F.shape[0]
        if K2 > F.shape[0]:
            K2 = F.shape[0]
        pca1 = sklearn.decomposition.PCA(n_components = K1)
        pca1.fit(F)        
        pca2 = sklearn.decomposition.PCA(n_components = K2)
        pca2.fit(F)        

        finalDims = pca1.transform(F)
        finalDims2 = pca2.transform(F)

        # for i in range(finalDims.shape[0]):            
        #     plt.text(finalDims[i,0], finalDims[i,1], ntpath.basename(wavFilesList[i].replace('.wav','')), horizontalalignment='center', verticalalignment='center', fontsize=10)
        #     plt.plot(finalDims[i,0], finalDims[i,1], '*r')
        # plt.xlim([1.2*finalDims[:,0].min(), 1.2*finalDims[:,0].max()])
        # plt.ylim([1.2*finalDims[:,1].min(), 1.2*finalDims[:,1].max()])            
        # plt.show()
        
        SM = 1.0 - distance.squareform(distance.pdist(finalDims2, 'cosine'))
        for i in range(SM.shape[0]):
            SM[i,i] = 0.0;
            
        aV.chordialDiagram("vis", SM, 0.50, namesToVisualize, namesCategoryToVisualize)

        SM = 1.0 - distance.squareform(distance.pdist(F, 'cosine'))
        for i in range(SM.shape[0]):
            SM[i,i] = 0.0;
        aV.chordialDiagram("visInitial", SM, 0.50, namesToVisualize, namesCategoryToVisualize)

        # plot super-categories (i.e. artistname
        uNamesCategoryToVisualize = sort(list(set(namesCategoryToVisualize)))
        finalDimsGroup = np.zeros( (len(uNamesCategoryToVisualize), finalDims2.shape[1] ) )
        for i, uname in enumerate(uNamesCategoryToVisualize):
            indices = [j for j, x in enumerate(namesCategoryToVisualize) if x == uname]
            f = finalDims2[indices, :]
            finalDimsGroup[i, :] = f.mean(axis=0)

        SMgroup = 1.0 - distance.squareform(distance.pdist(finalDimsGroup, 'cosine'))
        for i in range(SMgroup.shape[0]):
            SMgroup[i,i] = 0.0;
        aV.chordialDiagram("visGroup", SMgroup, 0.50, uNamesCategoryToVisualize, uNamesCategoryToVisualize)
    
    def mtLda(folder):
        allMtFeatures, Ys, wavFilesList = aF.dirWavFeatureExtractionNoAveraging(folder, 1.0, 1.0, 0.050, 0.025)
        if allMtFeatures.shape[0]==0:
            print("Error: No data found! Check input folder")
            return

        # namesCategoryToVisualize = [ntpath.basename(w).replace('.wav','').split(" --- ")[0] for w in wavFilesList]; 
        namesToVisualize = [ntpath.basename(w).replace('.wav','') for w in wavFilesList]
    
        ldaLabels = Ys
        (F, MEAN, STD) = aT.normalizeFeatures([allMtFeatures])
        F = np.array(F[0])

        # clf = sklearn.discriminant_analysis.LinearDiscriminantAnalysis(n_components=10)
        clf = sklearn.discriminant_analysis.LinearDiscriminantAnalysis(n_components=10)
        print(clf)


        clf.fit(F, ldaLabels)    
        reducedDims =  clf.transform(F)


    # Get full path to file's directory
    path = os.path.dirname(os.path.realpath(__file__))
    inputDir = path + "/mtfeatures"
    # inputDir = path + "/testdata"
    # inputDir = path + "/../../data"

    mts = np.array([])
    wavs = []
    for f in os.scandir(inputDir):
        print(f.name)
        importmt = np.loadtxt(inputDir+"/"+f.name, delimiter=",", skiprows=1)
        wavs.append(f.name)
        if len(mts) == 0:
            mts = importmt
        else:
            mts = np.vstack((mts, importmt))
    mtPca(mts, wavs)

    # print(importmt)
    # visualizeFeaturesDir(inputDir)
    # aV.visualizeFeaturesFolder(path+"/testdata", dimReductionMethod="pca")
    # aV.visualizeFeaturesFolder(path+"/testnaming", dimReductionMethod="lda")

if __name__ == "__main__":
    main()