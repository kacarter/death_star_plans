#!/usr/bin/env python

# Adapted from fadecandy's chase.py and https://stackoverflow.com/questions/36634807/how-do-i-open-an-mp4-video-file-with-python

import opc, time, serial, cv2

numLEDs = 512
laser_length = 90
spoke_length = 30
num_spokes = 5
strip_length = 64
client = opc.Client('127.0.0.1:22368')
#client = opc.Client('127.0.0.1:7890')
serial_port = serial.Serial('/dev/ttyUSB0', 9600)
video_file = cv2.VideoCapture('sintel_trailer-480p.mp4')
ret, frame = video_file.read()

while True:
    serial_port.reset_input_buffer()
    button_status = serial_port.readline().decode().strip('\r\n')
    #print(button_status)
    if (button_status == '1'):
        pixels = [(0,0,0)] * numLEDs
        for i in range(spoke_length):
            for j in range(num_spokes):
                for k in range(i):
                    pixels[(j*64) + k] = (0, 150, 0)
                    if (k % 4 == i % 4):
                        pixels[(j*64) + k] = (0, 0, 0)
            client.put_pixels(pixels)
            time.sleep(0.15)

        for i in range(spoke_length):
            for j in range(num_spokes):
                for k in range(spoke_length):
                    if (i >= 10 and k >= 10):
                        extra_brightness = (((i - 10) % 20) * ((k - 10) % 20)) / 4
                        pixels[(j*64) + k] = (extra_brightness * 1.5, 164 + extra_brightness, extra_brightness * 1.5)
                    else:
                        pixels[(j*64) + k] = (0, 150, 0)
                    if (k % 4 == i % 4):
                        pixels[(j*64) + k] = (0, 0, 0)
            client.put_pixels(pixels)
            time.sleep(0.15)


        for i in range(210):
            pixels[i + 286] = (0, 255, 0)
            if (i <= laser_length + spoke_length):
              for j in range(num_spokes):
                for k in range(spoke_length):
                  if (k >= 10):
                    extra_brightness = (19 * ((k - 10) % 20)) / 4
                    pixels[(j*64) + k] = (extra_brightness * 1.5, 164 + extra_brightness, extra_brightness * 1.5)
                  else:
                    pixels[(j*64) + k] = (0, 150, 0)
                  if (k % 4 == i % 4):
                    pixels[(j*64) + k] = (0, 0, 0)
                if (i > laser_length - spoke_length):
                  for k in range(i - laser_length + spoke_length):
                    pixels[(j*64) + k] = (0, 0, 0)
            if (i >= laser_length):
              pixels[i - laser_length + 286] = (0, 0, 0)
            client.put_pixels(pixels)
            time.sleep(0.15)

        for i in range(laser_length):
            pixels[i + 495 - laser_length + 1] = (0, 0, 0)
            client.put_pixels(pixels)
            time.sleep(0.15)

        while True:
            ret, frame = video_file.read()
            cv2.imshow('frame', frame)
            if (cv2.waitKey(1) & 0xFF == ord('q') or ret == False):
                video_file.release()
                cv2.destroyAllWindows()
                break
            cv2.imshow('frame', frame)
