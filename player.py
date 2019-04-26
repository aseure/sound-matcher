import pyaudio


def play(audio_output, volume, rate, channels=1, format=pyaudio.paFloat32):
    sound = pyaudio.PyAudio()
    stream = sound.open(
        format=format,
        channels=channels,
        rate=rate // channels,
        output=True,
    )
    stream.write(volume * audio_output, num_frames=len(audio_output) // channels)
    stream.stop_stream()
    stream.close()
    sound.terminate()
