import pyaudio
import numpy as np

CHUNK = 2**11
RATE = 48000

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input = True, output = True,
              frames_per_buffer=CHUNK)

for i in range(int(100*48000/1024)): #go for a few seconds
    data = np.frombuffer(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    #dfft = 10.*np.log10(abs(np.fft.rfft(data)))
    #avrg = np.average(np.abs(dfft))*2
    bars="#"*int(50*peak/2**12)
    #bars2 = "0"*int(500*avrg/2**10)
    print("%04d %05d %s"%(i,peak,bars))

stream.stop_stream()
stream.close()
p.terminate()