#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
import os
import sys
import json
import matplotlib.pyplot as plt
import cv2 as cv
import math
import source.config as config

row = 0
result = []

def foundMob(mobMeanArray):
    global row
    global result
    probs = [(math.inf, 'empty'), (math.inf, 'empty'), (math.inf, 'empty')]
    with open('data.json') as json_file:
        jsonData = json.load(json_file)
        for key in jsonData:
            for j in range(len(jsonData[key])):
                total = 0
                comparator = []
                for i in range(30, len(mobMeanArray)):
                    for k in range(len(mobMeanArray[i])):
                        comparator.append(
                            abs(mobMeanArray[i][k] - jsonData[key][j][i][k]))
                for i in range(len(comparator)):
                    total += comparator[i]
                total = total / len(mobMeanArray)
                if total < probs[0][0]:
                    probs[2] = probs[1]
                    probs[1] = probs[0]
                    probs[0] = (total, key)
                elif total < probs[1][0]:
                    probs[2] = probs[1]
                    probs[1] = (total, key)
                elif total < probs[2][0]:
                    probs[2] = (total, key)
        print(
            f'|{row}|Higher probability are: \n\
            #1 - {config.WARNING}{probs[0][1]}{config.ENDC} with {config.WARNING}{probs[0][0]}{config.ENDC}\n\
            #2 - {config.OKBLUE}{probs[1][1]}{config.ENDC} with {config.OKBLUE}{probs[1][0]}{config.ENDC}\n\
            #3 - {config.OKBLUE}{probs[2][1]}{config.ENDC} with {config.OKBLUE}{probs[2][0]}{config.ENDC}')
        row += 1
        result.append(probs[0][1])



def splitImage(imageArray):
    newArray = []
    global row
    for a in range (10):
        for b in range (10):
            pre_val_a = a * 10
            pre_val_b = b * 10
            val_a = (a + 1) * 10 
            val_b = (b + 1) * 10
            newArray.append(imageArray[pre_val_a:val_a, pre_val_b:val_b, 0:3])
    meanArray = []
    for i in range(len(newArray)):
        arr = np.mean(newArray[i], axis=1)
        meanArray.append(np.around(np.mean(arr, axis=0)))
    return (meanArray)

def threshold(imageArray):

    balanceAr = []
    newAr = imageArray

    from statistics import mean
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)

    balance = 125 #mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance * 2:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
            elif mean(eachPix[:3]) > balance * 1.5:
                eachPix[0] = 200
                eachPix[1] = 200
                eachPix[2] = 200
            elif mean(eachPix[:3]) > balance:
                eachPix[0] = 150
                eachPix[1] = 150
                eachPix[2] = 150
            elif mean(eachPix[:3]) > balance / 1.5:
                eachPix[0] = 100
                eachPix[1] = 100
                eachPix[2] = 100
            elif mean(eachPix[:3]) > balance / 2:
                eachPix[0] = 50
                eachPix[1] = 50
                eachPix[2] = 50
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
    return newAr


def analyseImage(mobsArray):
    blackSquare = Image.new('RGB', (100, 30), (0, 0, 0))
    secondBlackSquare = Image.new('RGB', (25, 25), (0, 0, 0))
    for mob in mobsArray:
        mob.thumbnail((100, 100), Image.ANTIALIAS)
        mob.paste(blackSquare)
        mob.paste(secondBlackSquare, (75, 75))
        mob.paste(secondBlackSquare, (0, 75))
        iar = np.array(mob)
        meanArray = splitImage(iar)
        foundMob(meanArray)
        print("_________________________________________________________________________________________________________")
