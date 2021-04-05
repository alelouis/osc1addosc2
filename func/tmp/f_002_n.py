import numpy as np

f = 440
ratio = 7/8
tp = 2*np.pi

x = lambda t: np.sin(tp*f*t + np.pi/3*(np.sin(tp*t*2)+1))
y = lambda t: np.sin(tp*f*t - np.pi/6*(np.sin(tp*t*2)+1))