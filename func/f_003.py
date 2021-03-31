import numpy as np

f = 440
ratio = 3/4
tp = 2*np.pi

x = lambda t: np.sin(tp*f*t)
y = lambda t: np.sin(tp*f*ratio*t + 0.1*np.sin(tp*2*t))