import pineworkslabs.RPi as GPIO
from time import sleep
import pygame
from random import *

pygame.init()
DEBUG = False
# Gpio pins From L to R
switches = [20,16,12,26]
# Led pins from L to R
leds = [9,13,19,21]
noteSpeed = 1.0
playSpeed = 0.5
visuals = True
sounds = [ pygame.mixer.Sound("one.wav"),
pygame.mixer.Sound("two.wav"),
pygame.mixer.Sound("three.wav"),
pygame.mixer.Sound("four.wav") ]

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

def all_on():
    for _ in leds:
        GPIO.output(leds, True)
        
def all_off():
    for _ in leds:
        GPIO.output(leds, False)
        
def lose():
    for _ in range(0,4):
        all_on()
        sleep(0.5)
        all_off()
        sleep(0.5)
        
seq = []

seq.append(randint(0,3))
seq.append(randint(0,3))

print("Welcome to Simon!")
print("Try to play the sequence back by pressing the switches.")
print("Press Ctrl+C to exit...")

try:
    while True:
        seq.append(randint(0,3))
        if DEBUG:
            if len(seq) > 3:
                print()
            print(f"Seq={seq}")
            
        if visuals:
            for s in seq:
                GPIO.output(leds[s], True)
                sounds[s].play
                sleep(noteSpeed)
                GPIO.output(leds[s],False)
                sleep(playSpeed)
        else:
            for s in seq:
                sounds[s].play
                sleep(noteSpeed)
                sleep(playSpeed)
                
        
        switchCount = 0
        
        while switchCount < len(seq):
            
            pressed = False
            
            while not pressed:
                
                for i in range(len(switches)):
                    while GPIO.input(switches[i]):
                        val = 1
                        pressed = True
            
            if DEBUG:
                print(val)
                
            GPIO.output(leds[val], True)
            sounds[val].play()
            sleep(1)
            GPIO.output(leds[val], False)
            sleep(0.25)
            
            if val != seq[switchCount]:
                print(f"You made it to a sequence of {switchCount}")
                lose()
                GPIO.cleanup()
                exit(0)
                
            switchCount += 1
            
            if switchCount == 5: noteSpeed -= .1; playSpeed -= .1
            elif switchCount == 7: noteSpeed -= .1; playSpeed -= .1
            elif switchCount == 10: noteSpeed -= .1; playSpeed -= .05
            elif switchCount == 13: noteSpeed -= .1; playSpeed -= .1
            elif switchCount == 15: visuals = False
    
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nSionara!")