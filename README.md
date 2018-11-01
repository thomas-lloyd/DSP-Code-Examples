# DSP-Code-Examples

## Overview

Contained here are various code examples for implementing basic DSP algorithms using Python.

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
### Generating a Sine wave
```python
import numpy as np
#Set Frequency
f=1000;
#Set Length (samples)
length=1024;
T=1/fs;
t = (np.linspace(0,length-1,num = length))*T
s = np.sin(2*(np.pi)*t*f)
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