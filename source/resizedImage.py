#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from source.analyseImage import analyseImage

mobsIndex = 0

class ResizedImage:
    def __init__(self, image, mobSize, space, colNb):
        self.image = image
        self.mobSize = mobSize
        self.space = space
        self.colNb = colNb
        self.mobs = []

        self.getMobs()
        analyseImage(self.mobs)

    def getMobs(self):
        for i in range(6):  # loop to crop all the mobs on the screenshot
            for j in range(self.colNb):
                box = (self.mobSize * j + self.space * j, self.mobSize * i + self.space * i , self.mobSize * (j + 1) + self.space * j, self.mobSize * (i + 1) + self.space * i)
                self.mobs.append(self.image.crop(box))