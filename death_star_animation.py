#!/usr/bin/env python

# Adapted from fadecandy's chase.py

import opc, time

numLEDs = 512
#client = opc.Client('127.0.0.1:22368')
client = opc.Client('127.0.0.1:7890')

while True:
    pixels = [(0,0,0)] * numLEDs
    for i in range(30):
        for j in range(5):
            for k in range(i):
                pixels[(j*64) + k] = (0, 150, 0)
                if (k % 4 == i % 4):
                    pixels[(j*64) + k] = (0, 0, 0)
        client.put_pixels(pixels)
        time.sleep(0.15)

    for i in range(30):
        for j in range(5):
            for k in range(30):
                if (i >= 10 and k >= 10):
                    extra_brightness = (((i - 10) % 20) * ((k - 10) % 20)) / 4
                    pixels[(j*64) + k] = (extra_brightness * 2.5, 150 + extra_brightness, extra_brightness * 2.5)
                else:
                    pixels[(j*64) + k] = (0, 150, 0)
                if (k % 4 == i % 4):
                    pixels[(j*64) + k] = (0, 0, 0)
        client.put_pixels(pixels)
        time.sleep(0.15)


    for i in range(210):
        pixels[i + 286] = (0, 255, 0)
        client.put_pixels(pixels)
        time.sleep(0.02)
