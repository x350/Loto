import numpy as np


class Pouch:
    def __init__(self):
        self.pouch = np.arange(1, 91)
        np.random.shuffle(self.pouch)
        self.pouch = self.pouch.astype(np.str_).tolist()
        # self.pouch = [number.item() for number in self.pouch.astype(np.str_)]

    def __iter__(self):
        return iter(self.pouch)
