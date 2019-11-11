# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:45:12 2019

@author: user
"""

from pygame import mixer

mixer.init()
mixer.music.load("elevator.mp3")
mixer.music.play()

mixer.music.load("nope.mp3")
mixer.music.play()