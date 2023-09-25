from PIL import Image, ImageChops
import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import librosa
from scipy import signal
from scipy.fft import fft, fftfreq
import wavio as wv
import soundfile as sf


def spectrogram(audio, sr):

    window_size = 1024
    hop_length = int(window_size / 4)
    n_fft = window_size
    spectrogram = librosa.stft(audio, n_fft=n_fft, hop_length=hop_length, window=signal.hann(window_size))
    spectrogram_db = librosa.amplitude_to_db(np.abs(spectrogram), np.max)
    plt.figure(figsize=(12, 5))
    librosa.display.specshow(spectrogram_db, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log') 
    plt.xlabel('Время')
    plt.ylabel('Частота')
    return plt

def filter(audio,sr):
    window = 51
    polynom = 3
    data = audio.astype(float)
    filtered = signal.savgol_filter(data, window, polynom)
    return filtered, sr


def lab9():
    SOURE_DIR = 'C:\\Users\\vadik\\OneDrive\\Рабочий стол\\lab12\\sound\\'
    content = os.listdir(SOURE_DIR)
    print(content)
    name = input()
    samples, sampling_rate = librosa.load(SOURE_DIR+name+'.wav')
    samples = samples.astype(float)
    s = spectrogram(samples, sampling_rate)
    #s.show()
    s.savefig(name+'.png')
    rand = np.random.rayleigh(0.05,(1,samples.shape[0]))
    withnoise = samples + rand/50
    sf.write('withnoise'+name+'.wav',np.ravel(withnoise), sampling_rate)
    samples, sampling_rate = librosa.load('withnoise'+name+'.wav')
    s = spectrogram(samples, sampling_rate)
    #s.show()
    s.savefig('noised'+name+'.png')
    samples, sampling_rate = filter(samples, sampling_rate)
    s = spectrogram(samples, sampling_rate)
    #s.show()
    s.savefig('denoised'+name+'.png')
    sf.write('denoised'+name+'.wav',np.ravel(samples), sampling_rate)
