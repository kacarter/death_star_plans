#!/usr/bin/env python

# Adapted from fadecandy's chase.py

import opc, time

numLEDs = 390
client = opc.Client('127.0.0.1:22368')

while True:
    pixels = [(0,0,0)] * numLEDs
    for i in range(30):
        for j in range(6):
            for k in range(i):
                pixels[(j*30) + k] = (0, 150, 0)
                if (k % 4 == i % 4):
                    pixels[(j*30) + k] = (0, 0, 0)
        client.put_pixels(pixels)
        time.sleep(0.15)

    for i in range(30):
        for j in range(6):
            for k in range(30):
                pixels[(j*30) + k] = (0, 150, 0)
                if (k % 4 == i % 4):
                    pixels[(j*30) + k] = (0, 0, 0)
        client.put_pixels(pixels)
        time.sleep(0.15)


    for i in range(210):
        pixels = [ (0,0,0) ] * numLEDs
        pixels[i + 180] = (0, 255, 0)
        client.put_pixels(pixels)
        time.sleep(0.02)
