from typing import Any, Iterator
import numpy as np


class Pouch:
    '''
    Итератор, цыфры от 1 до 90, в случайном порядке
    '''
    def __init__(self) -> None:
        self.pouch = np.arange(1, 91)
        np.random.shuffle(self.pouch)
        self.pouch = self.pouch.astype(np.str_).tolist()
        # self.pouch = [number.item() for number in self.pouch.astype(np.str_)]

    def __iter__(self) -> Iterator[str]:
        return iter(self.pouch)

