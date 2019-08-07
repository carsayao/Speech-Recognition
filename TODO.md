# what needs to be done in terms of processing?
- ~~get midterm features to produces feature vector~~
    - ~~take individual statistics of each word and average them~~
    
    note: mean and std deviation are separated by 34 in the index
- ~~import csv files as np.array~~
- compute similarity matrix based on cosine distances of individual feature vectors

# what other models should we build?
- [3d spectrogram](https://www.kaggle.com/davids1992/speech-representation-and-data-exploration)
  
## [chordial diagram](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144610)

Given: a set of audio files (e.g. stored in WAV files stored in a particular path). Prior and manual categorization information can also be provided through the filenames theirselves: if the filename format: <category name> --- <sample name> is provided, then the input signals are supposed to be classified to the given categories. This information is either used only for visualization or for supervised dimensionality reduction. For example, the filename Blur --- Charmless Man.wav assigns the category label “Blur” to the signal. Such information can also be driven from MP3 tag information: for example pyAudioAnalysis provides an MP3-to-WAV conversion functionality that produces files with the aforementioned filename format, where the category name is taken from the “artist” MP3 tag.
    
Extract mid-term features and long-term averages in order to produce one feature vector per audio signal.
    
The feature representation can be (optionally) projected to a lower dimension. Towards this end, either Principal Component Analysis (PCA) or Linear Discriminant Analysis (LDA) is used. PCA is unsupervised, however LDA requires some type of supervised information. If available, this infomartion is stemming from the aforementioned “category” label.
    
A similarity matrix is computed based on the cosine distances of the individual feature vectors.
    
The similarity matrix is used to extract a chordial representation (Fig 8) that visualize the content similarities between the audio recordings. Towards this end, d3js is used (http://d3js.org/). d3js is a JavaScript library for manipulating and visualizing documents based on data.
