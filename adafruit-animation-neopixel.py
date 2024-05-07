import pygame
import time
import threading

# MUSIC PLAYING

def play_music(mp3File):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3File)
    pygame.mixer.music.play()
    
def wait_for_input():
    input()
    pygame.mixer.music.stop()

music_thread = threading.Thread(target=play_music, args=('Organic (2).mp3',))
input_thread = threading.Thread(target=wait_for_input)

music_thread.start()
input_thread.start()

#=============================================================================================

#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

from rpi_ws281x import *
import argparse

# LED strip configuration:
LED_COUNT      = 256      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 20     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


from PIL import Image

import numpy as np

def flip_even_rows(a):
    for i, row in enumerate(a):
        if i % 2 == 1:
            a[i] = row[::-1]
    return a




def animation(strip, pixel_sequence):
    num=0
    for row in pixel_sequence:
        for pixel in row:

    #            print ("\tPIXEL",pixel)
            red = pixel[0]
            blue = pixel[1]
            green = pixel [2]
            alpha = pixel [3]
    #            print("NUM",num,"\tred=",red, "\tblue", blue, "\tgreen", green)

            strip.setPixelColor(num,  Color(red, blue, green))
    #        pixels_out[num]= (red, blue, green)
            num = num+1

    strip.show()


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            
            
            

            art = ["Fish0.png", "Fish1.png", "Fish2.png", "Fish3.png", "Fish4.png", "Fish5.png", "Fish6.png", "Fish7.png", "Fish8.png", "Fish9.png", "Fish10.png", "Fish11.png", "Fish12.png", "Fish13.png", "Fish14.png", "Fish0.png"]


            #FOR LOOP
            #==============================================================
            for i in range(0, 15):            
            
                #im = Image.open("rainbow-slash.png")
                im = Image.open(art[i])
                im = im.transpose(Image.TRANSPOSE)

                rotateim = im.rotate(0) 
                width, height = im.size

                matrix = np.asarray(rotateim)

            #    print(matrix[1])
                matrix2 = flip_even_rows(matrix.copy())
            #    print(matrix2[1])


                #pixel_sequence = list(rotateim.getdata())

                pixel_sequence = list(matrix2)


                animation(strip, pixel_sequence)  # Red theater chase
                time.sleep(0.15)  


    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
