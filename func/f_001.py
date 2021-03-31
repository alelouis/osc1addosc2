import numpy as np

f = 440
ratio = 7/8
tp = 2*np.pi

x = lambda t: np.sin(tp*f*t + np.sin(tp*t*440))
y = lambda t: np.sin(tp*f*ratio*t + x(t)*np.sin(tp*t*230*t) + 40*np.sin(tp*t/2))