import numpy as np
import sounddevice as sd
import soundfile as sf
import os
import pickle
import sys
import importlib

def fade(z, start, end):
    if z <= start: return np.e**(z-start) - 1 + start
    elif z <= end: return z
    else: return 1 + end - np.e**(-(z-end))

args = sys.argv
func_id = args[1]
render_flag = bool(int(args[2]))
play_flag = bool(int(args[3]))
func = importlib.import_module(f'func.f_{func_id}')

stationary_duration = 8.
fade_duration =  2

fs = 44100*4 if render_flag else 44100

t = np.arange(0, stationary_duration, 1./fs)
t = np.array([fade(z, fade_duration, stationary_duration - fade_duration - 1) for z in t])

osc1 = func.x(t)
osc2 = func.y(t)
data = (osc1 + osc2)/2

if not os.path.exists(f'out/{func_id}'): os.makedirs(f'out/{func_id}')

with open(f'out/{func_id}/x.pkl', 'wb') as h:
    pickle.dump(x.tolist(), h, protocol=2)

with open(f'out/{func_id}/y.pkl', 'wb') as h:
    pickle.dump(y.tolist(), h, protocol=2)

if play_flag:
    sd.play(data, samplerate=fs, blocking=True)
sf.write(f'out/{func_id}/sound.wav', data, fs)

