#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time

numLEDs = 390
client = opc.Client('127.0.0.1:22368')

while True:
	for i in range(numLEDs):
		pixels = [ (0,0,0) ] * numLEDs
		pixels[i] = (255, 255, 255)
		client.put_pixels(pixels)
		time.sleep(0.05)
