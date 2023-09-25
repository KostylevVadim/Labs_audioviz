import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import librosa
from scipy import signal
from scipy.fft import fft, fftfreq
import wavio as wv
import soundfile as sf
from lab9.lab9 import spectrogram

def lab10():
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\sound10\\'
    content = os.listdir(SOURE_DIR)
    print(content)
    names = ['A','GAV','I']
    for name in names:
        samples, sampling_rate = librosa.load(SOURE_DIR+name+'.wav')
        s = spectrogram(samples, sampling_rate)
        s.savefig(name+'.png')
        frequencies = np.fft.rfftfreq(len(samples), d=1/sampling_rate)
        magnitudes = np.abs(np.fft.rfft(samples))
    #plt.plot(xf, np.abs(yf))
        voice_frequencies = frequencies[np.where(magnitudes > np.mean(magnitudes))]
    #plt.show()
        print(max(np.abs(voice_frequencies)), min(np.abs(voice_frequencies)))
    #fundamental = min(np.abs(frequencies))
        fr = np.abs(voice_frequencies)
        d1 = {}
        for i in range(len(fr)):
            count = 0
            upper = []
            for j in range(i+1,len(fr)):
                if fr[j]%fr[i]==0 and fr[j]>fr[i]:
                    count+=1
                
        
            if fr[i] not in d1 and count!=0:
    #        print(fr[i], count)
                d1[fr[i]] = count
        k = 0.0
        m_value = 0.0
        for key, value in d1.items():
            if value>m_value:
                m_value = value
                k = key
        print(k)
        print('====')
