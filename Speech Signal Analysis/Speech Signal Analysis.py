#202121278 김도현

import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

sr = 16000
y, sr = librosa.load("Speech Signal Analysis/sample_data/sample.wav", sr=sr)

#.wav 파일의 샘플링 주파수와 오디오 신호의 길이를 출력합니다.
print (sr)
print (y.shape)
print (len(y)/sr)

#Waveform
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

#Spectrogram
frame_length_ms = 25
frame_shift_ms = 10

win_length = int(sr * frame_length_ms / 1000)
hop_length = int(sr * frame_shift_ms / 1000)
n_fft = 400

X = librosa.stft(
    y, 
    n_fft=n_fft, 
    hop_length=hop_length, 
    win_length=win_length
)

X[:2,:2]
array([[ 0.00024849+0.j, -0.00259107+0.j],
       [-0.00102268-0.00052152j, 0.00195318+0.00019787j]],
        dtype=complex64)




plt.show()
