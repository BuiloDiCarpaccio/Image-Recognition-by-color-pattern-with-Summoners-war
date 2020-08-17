#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from datetime import datetime
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys
from source.resizedImage import ResizedImage
import matplotlib.pyplot as plt

class Crop:
    def __init__(self, imagePath):
        self.imagePath = imagePath
        self.resize = []
        self.space = 0
        self.columns = 0
        self.widthStart = 0
        self.widthEnd = 0
        self.mobSize = 0
        self.heightStart = 0
        self.heightEnd = 0

        iar1 = cv.imread(imagePath)
        iar1 = cv.cvtColor(iar1, cv.COLOR_BGR2GRAY)
        iar1, thresh = cv.threshold(iar1, 127, 255, cv.THRESH_TOZERO)
        self.getWidthDetails(thresh)
        self.getHeightDetail(thresh)
        im = Image.open(imagePath)
        box = (self.widthStart, self.heightStart, self.widthEnd, self.heightEnd)
        resized = im.crop(box)
        self.resize = ResizedImage(resized, self.mobSize, self.space, self.columns)

    def getWidthDetails(self, thresh):
        spaceBetween = []
        height, width = thresh.shape
        i = 0
        while i < width:
            if np.mean(thresh[round(0.8 * height):height-1, i:i+1]) == 0:
                newArray = []
                while i < width :
                    if np.mean(thresh[round(0.8 * height):height-1, i:i+1]) < 20:
                        newArray.append(i)
                    else:
                        spaceBetween.append(newArray)
                        break
                    i+=1
            i+=1
        for i in range(1, len(spaceBetween)):
            if len(spaceBetween[i]) > round(self.space / i * 4) and self.space != 0:
                self.space = self.space / (i - 1)
                self.columns = i
                break
            self.space += len(spaceBetween[i])
        self.widthStart = spaceBetween[0][-1]
        self.widthEnd = spaceBetween[self.columns][0]
        self.mobSize = ((self.widthEnd - self.widthStart) - self.space * (self.columns - 1)) / self.columns

    def getHeightDetail(self, thresh):
        height, width = thresh.shape
        while self.heightStart < height:
            if np.mean(thresh[self.heightStart:self.heightStart+1, 0:round(height*0.5)]) == 0:
                while self.heightStart < width and np.mean(thresh[self.heightStart:self.heightStart+1, round(height*0.25):round(height*0.5)]) < 10:
                    self.heightStart += 1
                break
            self.heightStart += 1
        self.heightEnd = self.heightStart + self.mobSize * 6 + self.space * 5
