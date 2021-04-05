add_library('VideoExport')
import pickle
import colorsys

func_id = '001'
path = '/home/alelouis/Projects/fm/out/'+ func_id
with open(path + '/x.pkl', 'rb') as h: x = pickle.load(h)
with open(path + '/y.pkl', 'rb') as h: y = pickle.load(h)

h_back, s_back, v_back = int(func_id)/20., 0.3, 1
h_front, s_front, v_front = h_back, s_back + 0.2, v_back - 0.2
r_back, g_back, b_back = list(map(lambda x: 255*x, colorsys.hsv_to_rgb(h_back, s_back, v_back)))
r_front, g_front, b_front = list(map(lambda x: 255*x, colorsys.hsv_to_rgb(h_front, s_front, v_front)))

render = True
if render:
    fs = 44100 * 4
    w_size = 1000
else:
    fs = 44100
    w_size = 400

frame_rate = 60
samples_per_sec = fs/frame_rate
t = 0
l = samples_per_sec*2

def setup():
    size(w_size, w_size)
    stroke(r_front, g_front, b_front)
    strokeWeight(3)
    background(r_back, g_back, b_back)
    frameRate(frame_rate)
    rectMode(CENTER)
    if render:
        global videoExport
        videoExport = VideoExport(this, path + "/render.mp4")
        videoExport.setFrameRate(60)
        videoExport.startMovie()
    
def draw():
    global t, videoExport
    background(r_back, g_back, b_back)
    for i in range(l-1):
        line(width/2 * (1 + 0.8*y[t+i]), height/2 * (1 + 0.8*x[t+i]), width/2 * (1 + 0.8*y[t+i+1]), height/2 * (1 + 0.8*x[t+i+1]))
    if t < len(x)-l:
        t += samples_per_sec
    else:
        if render:
            videoExport.endMovie()
        exit()
    if render:
        videoExport.saveFrame()
    
