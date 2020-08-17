#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# EXIT
EXIT_FAILURE = 84
EXIT_SUCCESS = 0

if __name__ == '__main__':
    sys.exit(EXIT_FAILURE)


# ARGUMENT

# SHOW
SHOW_KO = '[\033[31mKO\033[0m] '
SHOW_OK = '[\033[32mOK\033[0m] '

# USAGE

# RESSOURCES FOLDER
RESSOURCES_FOLDER = './monster'

# TEST RESULT EXPECTED
RESULT_EXPECTED = ['sabrina', 'sigmarus', 'talia', 'raoq', 'shaina', 'rica', 'verdehile', 'mav', 'lushen',
                    'ethna', 'belladeon', 'loren', 'fran', 'kro', 'veromos', 'martina', 'ariel', 'baretta',
                    'abigail', 'vigor', 'spectra', 'galion', 'megan', 'khmun', 'velajuel', 'xiong_fei', 'baleygr',
                    'vanessa', 'hwa', 'garo', 'tesarion', 'naomi', 'bernard', 'shannon', 'iunu', 'chasun',
                    'katarina', 'taurus', 'copper', 'gemini', 'eigar', 'hrungnir', 'pang', 'mei_hou_wang',
                    'olivia', 'elucia', 'mihyang', 'lapis', 'bastet', 'woosa', 'kumar', 'rica', 'chiwu', 'raki',
                    'trinity', 'tetra', 'lapis', 'julie', 'mihyang', 'qebehsenuef', 'liesel', 'xiao_lin', 'izaria',
                    'sonnet', 'malaka', 'izaria', 'qebehsenuef', 'mikene', 'hwa', 'astar', 'hwahee', 'astar',
                    'draco', 'kunite', 'fria', 'harmonia', 'prilea', 'lushen', 'carbine', 'logan', 'hraesvelg',
                    'carbine', 'briand', 'kaito', 'briand', 'logan', 'skogul', 'arang', 'chasun', 'cichlid',
                    'tyron', 'kaz', 'emma', 'theomars', 'xiao_lin', 'taor', 'sigmarus', 'psamathe', 'homunculus_water',
                    'galion', 'perna', 'baretta', 'colleen', 'hwa', 'jojo', 'velajuel', 'bernard', 'orochi', 'ramagos',
                    'akhamamir', 'mav', 'teshar', 'belladeon', 'julianne', 'amarna', 'veromos', 'mantura', 'thrain', 'zeratu',
                    'lushen']

# COLORS
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
