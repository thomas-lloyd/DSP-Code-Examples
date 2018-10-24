# DSP-Code-Examples

## Overview

Contained here are various code examples for implementing basic DSP algorithms using C and Python

## Prerequisites

* Python 3
  * You will need an installation of Python 3 along with the necessary libraries for Numpy (numerical python), Scipy (scientific python) and matplotlib.  I recommend downloading [Anaconda](https://www.anaconda.com/download/), which comes with all these libraries along with a nice command line and IDE.

## Some Basics (Python)

### Reading a Wav File
```python
#import scipy library for importing wav files
import scipy.io.wavfile as sw
#define filepath
fp ='folder\\audio.wav'
#read audio
#fs=sample rate
#x=audio data
fs,x=sw.read(fp);
```
### Plotting a graph
```python
#import library for plotting graphs
import matplotlib.pyplot as plt
#plot data
plt.plot(x);
#show plot
plt.show();
```


## Some Basics (C)
Coming soon...
