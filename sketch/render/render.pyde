add_library('VideoExport')
import pickle

func_id = '003'
path = '/home/alelouis/Projects/fm/out/'+ func_id
with open(path + '/x.pkl', 'rb') as h: x = pickle.load(h)
with open(path + '/y.pkl', 'rb') as h: y = pickle.load(h)

frame_rate = 60
fs = 44100*4
samples_per_sec = fs/frame_rate
t = 0
l = samples_per_sec*2
def setup():
    size(1000, 1000)
    stroke(255)
    strokeWeight(3)
    background(0)
    frameRate(frame_rate)
    rectMode(CENTER)
    global videoExport
    videoExport = VideoExport(this, path + "/render.mp4")
    videoExport.setFrameRate(60)
    videoExport.startMovie()
    
def draw():
    global t, videoExport
    background(0)
    for i in range(l-1):
        line(width/2 * (1 + 0.8*y[t+i]), height/2 * (1 + 0.8*x[t+i]), width/2 * (1 + 0.8*y[t+i+1]), height/2 * (1 + 0.8*x[t+i+1]))
    if t < len(x)-l:
        t += samples_per_sec
    else:
        videoExport.endMovie()
        exit()
    videoExport.saveFrame()
    
