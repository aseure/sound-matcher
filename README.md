## Install

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Run

Make sure you have installed everything and that your `virtualenv` is enabled.

```
python -W ignore app.py <WAV_FILE>
```

## Next steps
 
 - Implement a moving window to detect notes rather than scanning the soundtrack
 - Take input from the microphone rather than from a file
 - Find the closest notes with a dynamic algorithm (k-nn clustering maybe)
   rather than taking the 100 ones with the bigger amplitude

## Notes

 - [4. Frequency and the Fast Fourier Transform - Elegant SciPy Book](https://www.oreilly.com/library/view/elegant-scipy/9781491922927/ch04.html)
 - [Frequencies of Musical Notes, A4 = 440 Hz](http://pages.mtu.edu/~suits/notefreqs.html)
 - `gawk -F '\t' '{printf "\"%s\": %s,\n", $1, $2}' Frequencies\ of\ Musical\ Notes,\ A4\ =\ 440\ Hz.html`
 - [PyAudio documentation](https://people.csail.mit.edu/hubert/pyaudio/docs/)