
# resize 函数

import math
from PIL import Image

class Resize():
    def __init__(self, size, interpolation=Image.BILINEAR):
        self.size = size
        self.interpolation = interpolation

    def __call__(self, img):
        w, h = img.size

        min_edge = min(img.size)
        rate = min_edge / self.size

        new_w = math.ceil(w / rate)
        new_h = math.ceil(h / rate)

        return img.resize((new_w, new_h))
