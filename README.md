# Usage
Place wav files in /data in respective folders, or change path in collect_features.py. Run `python3 collect_features.py` to generate /output folder. /output contains respective folders, each containing csv files of mid-term features. This also generates short-term features which are saved in /output. Run `python3 mean_features.py` to generate a csv containing the mean of each folder.

# Project Proposal
## Team Members
* Carter Wilson
* Carlos Miguel Sayao
* Theodore Vixay
* Gabriel Miller

## Objective
Visualize a given set of audio speech data using a combination SciPy, MatPlotLib, Tableau, and PyAudioAnalysis. Use clustering algorithms and techniques to group the audio data.  

## Approach
We will be using the dataset provided by the Kaggle Speech Recognition challenge. This includes 65,000 one-second long utterances of 30 short words by thousands of different people. Using amplitude as a measurement, we will process the data and use SciPy and MatPlotLib to provide basic waveform and spectrogram visualizations, with some aggregation. We will then use Tableau and PyAudioAnalysis to apply clustering techniques to see if we can find trends in visualizations of different words and types of words (verbs, consonants, etc.).

## Team Structure
Our team consists of two sub-teams. One group works on classifying the dataset using machine learning techniques. Our group works on visualizing the dataset. The learning process will consist of regular meetings where we will study and work towards milestones.

## Milestones
* Successful processing of the audio data
* Successful build of basic wave and spectrogram visualizations
* Aggregated visualizations of the audio data
* Build clustered visualizations of the audio data
* Find trends and interpret data

## How to set up and use `virtual env`
    pip3 install virtualenv

    virtualenv -p python3 env

This will install virtualenv using pip3 and create a an `env` folder that will contain the libraries brought it.

    source env/bin/activate

This will put your shell into the virtual environment where you will have the libraries brought it.

    pip3 install -r requirements.txt
This will install the libraries that are found in the `requirements.txt`
When you are done working, use `deactivate` to get out of the virtual environment
