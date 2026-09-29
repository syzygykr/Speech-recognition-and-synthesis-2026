Speech Signal Analysis in 4 different ways.

▪ Waveform

A waveform represents a speech signal in the time domain. It shows how the amplitude of the audio signal changes over time.
- X-axis: Time (seconds)
- Y-axis: Amplitude
- Main information: Signal amplitude, duration, and temporal structure.
Waveforms are useful for identifying silence, speech boundaries, pauses, and abrupt changes in amplitude.
However, a waveform does not directly show the frequency components of speech. Two signals with different frequency content may have similar waveform shapes.

▪ Spectrogram

A spectrogram represents the frequency content of a signal over time. It is typically calculated using the Short-Time Fourier Transform (STFT).
- X-axis: Time
- Y-axis: Frequency (Hz)
- Color intensity: Signal energy or magnitude at each frequency.
- Main information: How the frequency components of speech change over time.
Unlike a waveform, a spectrogram reveals the frequency structure of speech, including harmonics, formants, and transitions between phonemes.
It is useful for analyzing speech sounds, identifying phonetic characteristics, and visualizing how speech changes over time.
However, the frequency scale is linear, which does not reflect the way humans perceive pitch and frequency.

▪ Mel Spectrogram

A Mel Spectrogram is a frequency representation based on the Mel scale, which approximates the human auditory system's perception of frequency.
It is generally calculated by applying Mel filter banks to the power spectrogram.
- X-axis: Time
- Y-axis: Mel frequency
- Color intensity: Energy in each Mel frequency band.
- Main information: Speech energy distributed across perceptually scaled frequency bands.
The Mel scale provides greater frequency resolution at lower frequencies and less resolution at higher frequencies. This reflects the fact that humans perceive differences in lower frequencies more distinctly.
Mel Spectrograms are widely used in speech recognition and audio classification because they provide a compact, perceptually motivated representation of speech.
However, applying Mel filter banks reduces frequency resolution and loses some detailed spectral information.

▪ MFCC

MFCC is a compact representation of the spectral envelope of speech. It is derived from the Mel Spectrogram using a Discrete Cosine Transform (DCT).
The typical MFCC extraction process consists of the following steps:
1. Divide the audio signal into short frames.
2. Apply the Fourier Transform to each frame.
3. Apply Mel filter banks to obtain the Mel Spectrogram.
4. Take the logarithm of the Mel filter bank energies.
5. Apply the DCT to obtain the MFCC coefficients.
- X-axis: Time frames
- Y-axis: MFCC coefficient index
- Main information: Compact representation of the spectral envelope and timbral characteristics of speech.
MFCCs reduce redundancy in the Mel Spectrogram by decorrelating the log Mel filter bank energies. Typically, only a subset of coefficients is retained.
They are widely used in traditional speech recognition, speaker identification, and audio classification.
However, MFCCs discard some spectral detail and are not a direct representation of the original frequency spectrum.