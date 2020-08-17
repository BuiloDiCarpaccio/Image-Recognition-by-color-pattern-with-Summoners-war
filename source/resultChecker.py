#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import source.config as config
import source.analyseImage as analyseImage
import emoji

def verifyResults():
    found = 0
    error = 0
    for mob in range(len(analyseImage.result)):
        if analyseImage.result[mob] == config.RESULT_EXPECTED[mob]:
            found += 1
        else:
            error += 1
    print(emoji.emojize(
        f'The total of mobs found is: {config.OKGREEN} {found} success :check_mark:  {config.ENDC} and {config.FAIL} {error} fail :cross_mark: {config.ENDC}'))
    total = found / len(analyseImage.result) * 100
    if total == 100:
        print(emoji.emojize(f"The success rate is :hundred_points:%"))
    else:
        print(f"The success rate is {found / len(analyseImage.result) * 100}%") 
    exit(config.EXIT_SUCCESS)