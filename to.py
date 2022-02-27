from PIL import Image
import numpy as np
import random

a = []

def randout():
    out = []
    for i in range(10000):
        out.append([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    return out
for i in range(10000):
    print(i+1)
    a.append(randout())
    
Image.fromarray(np.uint8(a)).convert('RGB').save('my.png')
