from PIL import Image
import numpy as np

a = [[[255, 0, 0], [0, 255, 0]], [[0, 255, 0], [255, 0, 0]]]

Image.fromarray(np.uint8(a)).convert('RGB').save('my.png')

#PIL_image = Image.fromarray(numpy_image.astype('uint8'), 'RGB')