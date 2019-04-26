import sys
import time

import numpy as np
import pyaudio
from scipy import fftpack
from scipy.io import wavfile

import notes
from player import play

if len(sys.argv) < 2:
    print(f'Usage: python app.py <WAV_FILE>')
    sys.exit(1)

audio_input_file = sys.argv[1]
fs, audio_input = wavfile.read(audio_input_file)
print(f'Playing input file: {audio_input_file}')
play(audio_input, volume=1, rate=fs, channels=2, format=pyaudio.paInt32)

start = time.time()

audio_input_normalized = np.mean(audio_input, axis=1) / 2 ** 32
freqs = fftpack.fftfreq(audio_input_normalized.size) * fs
X = fftpack.fft(audio_input_normalized)
indices = np.flip(np.argsort(np.abs(X)))
freqs_ordered = np.abs(freqs[indices])[:100]
dist = np.vectorize(lambda f1, f2: abs(f1 - f2))
closest_frequencies_idx = np.fromiter(
    (np.argmin(dist(f, notes.frequencies())) for f in freqs_ordered),
    int,
)
_, idx = np.unique(closest_frequencies_idx, return_index=True)
closest_frequencies_idx = closest_frequencies_idx[np.sort(idx)]
closest_frequencies = notes.frequencies()[closest_frequencies_idx]
closest_notes = notes.frequencies_to_notes(closest_frequencies)

elapsed_time = time.time() - start

print(f'Playing detected notes (ordered by overall amplitude): {closest_notes} (took {elapsed_time:.3f}s)')

audio_output = np.concatenate([
    notes.generate_sound_from_note(note, fs, 500)
    for note in closest_notes
], axis=0).astype(np.float32)
play(audio_output, volume=1, rate=fs)
