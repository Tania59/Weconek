from PIL import Image
import numpy as np
im = Image.open('WeConek.png').convert('RGB')
arr = np.array(im)
center = tuple(im.getpixel((im.width//2, im.height//2)))
unique, counts = np.unique(arr.reshape(-1,3), axis=0, return_counts=True)
idx = np.argsort(counts)[::-1]
print('center', center)
print('top5', [tuple(c) for c in unique[idx[:5]]])
