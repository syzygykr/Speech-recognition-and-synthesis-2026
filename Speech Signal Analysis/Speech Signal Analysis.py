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
plt.show()

#Spectrogram
#Frame settings
frame_length_ms = 25
frame_shift_ms = 10

win_length = int(sr * frame_length_ms / 1000)
hop_length = int(sr * frame_shift_ms / 1000)
n_fft = 400

# Short-Time Fourier Transform
X = librosa.stft(
    y,
    n_fft=n_fft,
    hop_length=hop_length,
    win_length=win_length
)

# Power Spectrogram
S = np.abs(X) ** 2

# Log Power Spectrogram
log_S = np.log(S + 1e-10)

print(np.min(S), np.max(S), S.shape)
print(np.min(log_S), np.max(log_S), log_S.shape)

# Plot Spectrogram
librosa.display.specshow(
    log_S,
    sr=sr,
    hop_length=hop_length,
    x_axis="time",
    y_axis="hz"
)

plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogram")
plt.show()
print(log_S.shape)

#Mel Spectrogram
# Mel filter settings
n_mels = 40

mel_filter = librosa.filters.mel(
    sr=sr,
    n_fft=n_fft,
    n_mels=n_mels,
    norm=None
)

print(mel_filter.shape)
print(mel_filter[0])

# Mel Spectrogram
mel_spec = mel_filter @ S
print(mel_filter.shape, S.shape, mel_spec.shape)

# Log-Mel Spectrogram
log_mel = np.log(mel_spec + 1e-10)
print 

# Plot Log-Mel Spectrogram
librosa.display.specshow(
    log_mel,
    sr=sr,
    hop_length=hop_length,
    x_axis="time",
    y_axis="mel"
)

plt.colorbar(format="%+2.0f dB")
plt.title("Log-Mel Spectrogram")
plt.show()



plt.show()
