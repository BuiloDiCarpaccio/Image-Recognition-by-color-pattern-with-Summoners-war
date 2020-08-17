#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import cv2 as cv
import json
import pathlib

def getTestData(imagePath):
    blackSquare = Image.new('RGB', (100, 30), (0, 0, 0))
    secondBlackSquare = Image.new('RGB', (25, 25), (0, 0, 0))
    im1 = Image.open(imagePath)
    im1.thumbnail((100, 100), Image.ANTIALIAS)
    im1.paste(blackSquare)
    im1.paste(secondBlackSquare, (75, 75))
    im1.paste(secondBlackSquare, (0, 75))
    iar1 = np.array(im1)
    splitImage = []
    for a in range(10):
        for b in range(10):
            pre_val_a = a * 10
            pre_val_b = b * 10
            val_a = (a + 1) * 10
            val_b = (b + 1) * 10
            splitImage.append(iar1[pre_val_a:val_a, pre_val_b:val_b, :3].tolist())
    meanArray = []
    for i in range(len(splitImage)):
        arr = np.mean(splitImage[i], axis=1)
        meanArray.append(np.mean(arr, axis=0).tolist())
    return (meanArray)

if __name__ == '__main__':
    mobsFolder = [f.path for f in os.scandir('./monsters') if f.is_dir()]
    jsonFile = {}
    for mobsPath in mobsFolder:
        mobsMeanArray = []
        for p in pathlib.Path(mobsPath).iterdir():
            if p.is_file():
                print(p)
                lastSlashIndex = str(p).rfind('/')
                secondLastSlashIndex = str(p)[:lastSlashIndex - 1].rfind('/')
                fileName = str(p)[lastSlashIndex + 1:]
                mobsName = str(p)[secondLastSlashIndex + 1:lastSlashIndex]
                print(fileName)
                print(mobsName)
                if fileName != '.DS_Store':
                    mobsMeanArray.append(getTestData(str(p)))
                    jsonFile[mobsName] = mobsMeanArray
    with open('data.json', 'w') as outfile:
        json.dump(jsonFile, outfile)
