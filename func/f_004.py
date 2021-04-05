import numpy as np

f = 440
ratio = 3/4
tp = 2*np.pi

x = lambda t: np.sin(tp*f*t + tp * (1+np.sin(tp*t/4))/2 - np.pi/2)
y = lambda t: np.sin(tp*f*ratio*t)