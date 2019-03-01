import pyaudio
import numpy as np

CHUNK = 2**11
RATE = 48000
sdata = []
upper10 = []
next10 = []
third10 = []
forth10 = []
fifth10 =[]
sixth10 = []
seventh10 = []
eighth10 = []
nineth10 = []
tenth10 =[]
song_length_sec = 1000
#http://app.rawgraphs.io/

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input = True, output = True,
              frames_per_buffer=CHUNK)

for i in range(int((song_length_sec/2)*RATE/1024)): #go for around song_length_sec seconds, 23-24 readings per second (Rate*30 per min)
	data = np.frombuffer(stream.read(CHUNK),dtype=np.int16)
	peak=np.average(np.abs(data))*2
	bars="#"*int(50*peak/2**12)
	print("%04d %05d %s"%(i,peak,bars))
	sdata.append([i,int(50*peak/2**12)])
maxvol = 0
for q in range (0,1):
	for j in sdata:
		if j[1] > maxvol:
			maxvol = j[1]
for g in sdata:
	if g[1] > maxvol* .9:
		upper10.append(g)
	elif g[1] > maxvol* .8:
		next10.append(g)
	elif g[1] > maxvol* .7:
		third10.append(g)
	elif g[1] > maxvol* .6:
		forth10.append(g)
	elif g[1] > maxvol* .5:
		fifth10.append(g)
	elif g[1] > maxvol* .4:
		sixth10.append(g)
	elif g[1] > maxvol* .3:
		seventh10.append(g)
	elif g[1] > maxvol* .2:
		eighth10.append(g)
	elif g[1] > maxvol* .1:
		nineth10.append(g)
	else:
		tenth10.append(g)

beats = []
dif = 0
for w in range (2,len(sdata)-3):
	if (sdata[w][1] >= sdata[w-1][1]) and (sdata[w][1] > sdata[w-2][1]+3) and (sdata[w][1] >= sdata[w+1][1]) and (sdata[w][1] > sdata[w+2][1]+3): 
		beats.append(sdata[w])
		w += 1
print("bpm = " + str(int((len(beats))/(song_length_sec/60))))

#for k in range (0,len(upper10)-2):
#	if dif == 0:
#		dif = list(reversed(upper10))[k][0] - list(reversed(upper10))[k+1][0] 
#	elif (list(reversed(upper10))[k][0] - list(reversed(upper10))[k+1][0] > dif*.9) and (list(reversed(upper10))[k][0] - list(reversed(upper10))[k+1][0] < dif*1.1):
#		print(dif)
print (sdata)
#print ((upper10))
#print ((next10))
#print ((third10))
#print ((forth10))
#print ((fifth10))
#print ((sixth10))
#print ((seventh10))
#print ((eighth10))
#print ((nineth10))
#print ((tenth10))
stream.stop_stream()
stream.close()
p.terminate()
