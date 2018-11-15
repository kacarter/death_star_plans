#!/usr/bin/env python

# Adapted from fadecandy's chase.py

import threading, time, opc, serial, cv2
from playsound import playsound

client = opc.Client('127.0.0.1:7890')
# client = opc.Client('127.0.0.1:22368')
numLEDs = 512
pixels = [(0, 0, 0)] * numLEDs
background_pixels = 192
background_counter = 0
num_spokes = 5
strip_length = 64
spoke_length = 30
pixel_off = (0, 0, 0)
animation_speed = 0.15


def background_animation():
    global background_pixels
    global background_counter
    global pixels
    global pixel_off
    for b in range(background_pixels):
        if b % 6 in [background_counter, (background_counter + 1) % 6, (background_counter + 2) % 6]:
            pixels[b + (num_spokes * strip_length)] = (255, 0, 0)
        if b % 6 in [(background_counter + 3) % 6, (background_counter + 4) % 6, (background_counter + 5) % 6]:
            pixels[b + (num_spokes * strip_length)] = pixel_off
    background_counter = (background_counter + 1) % 6


def play_animation():
    global pixels
    global client
    global numLEDs
    global num_spokes
    global strip_length
    global pixel_off
    global animation_speed
    global spoke_length
    laser_length = 30

    pixels = [pixel_off] * numLEDs
    for i in range(spoke_length):
        for j in range(num_spokes):
            for k in range(i):
                pixels[(j * strip_length) + k] = (0, 0, 150)
                if k % 4 == i % 4:
                    pixels[(j * strip_length) + k] = pixel_off
        background_animation()
        client.put_pixels(pixels)
        time.sleep(animation_speed)

    for i in range(spoke_length):
        for j in range(num_spokes):
            for k in range(spoke_length):
                if i >= 10 and k >= 10:
                    extra_brightness = (((i - 10) % 20) * ((k - 10) % 20)) / 4
                    pixels[(j * strip_length) + k] = (extra_brightness * 1.5, extra_brightness * 1.5, 164 + extra_brightness)
                else:
                    pixels[(j * strip_length) + k] = (0, 0, 150)
                if k % 4 == i % 4:
                    pixels[(j * strip_length) + k] = pixel_off
        background_animation()
        client.put_pixels(pixels)
        time.sleep(animation_speed)

    for i in range(strip_length - spoke_length):
        pixels[i + ((num_spokes - 1) * strip_length) + spoke_length] = (255, 0, 0)
        if i <= laser_length + spoke_length:
            for j in range(num_spokes):
                for k in range(spoke_length):
                    if (k >= 10):
                        extra_brightness = (19 * ((k - 10) % 20)) / 4
                        pixels[(j * strip_length) + k] = (extra_brightness * 1.5, extra_brightness * 1.5, 164 + extra_brightness)
                    else:
                        pixels[(j * strip_length) + k] = (0, 0, 150)
                    if (k % 4 == i % 4):
                        pixels[(j * strip_length) + k] = pixel_off
                if (i > laser_length - spoke_length):
                    for k in range(i - laser_length + spoke_length):
                        pixels[(j * strip_length) + k] = pixel_off
        if i >= laser_length:
            pixels[i - laser_length + ((num_spokes - 1) * strip_length) + spoke_length] = pixel_off
        background_animation()
        client.put_pixels(pixels)
        time.sleep(animation_speed)

    for i in range(laser_length):
        pixels[i + (num_spokes * strip_length) - laser_length] = pixel_off
        background_animation()

        client.put_pixels(pixels)
        time.sleep(animation_speed)

    pixels = [pixel_off] * numLEDs
    client.put_pixels(pixels)


try:
    serial_port = serial.Serial('/dev/ttyUSB1', 9600)
except:
    serial_port = serial.Serial('/dev/ttyUSB0', 9600)
sound = "happy_birthday.mp3"
button_error = False

while True:
    try:
        if button_error == True:
            try:
                serial_port = serial.Serial('/dev/ttyUSB1', 9600)
                button_error = False
            except:
                try:
                    serial_port = serial.Serial('/dev/ttyUSB0', 9600)
                    button_error = False
                except:
                    button_error = True
        button_status = serial_port.readline().decode().strip('\r\n')
    except:
        print("button error")
        button_error = True
        time.sleep(10)
        pass
    # print(button_status)
    if (button_status == '1'):
        t = threading.Thread(target=play_animation)
        t.daemon = True
        t.start()
        try:
            playsound(sound)
        except:
            print("Can't play audio")
        try:
            serial_port.reset_input_buffer()
        except:
            pass

