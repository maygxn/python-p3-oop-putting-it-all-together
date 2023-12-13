#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self.condition = "Used"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val):
        if isinstance(val, int):
            self._size = val
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"