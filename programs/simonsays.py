import pineworkslabs.RPi as GPIO
from time import sleep
import pygame
from random import *

pygame.init()
DEBUG = True
# Gpio pins From L to R
switches = [27,26,25,24]
# Led pins from L to R
leds = [4,5,6,12]
noteSpeed = 1.0
playSpeed = 0.5
if DEBUG:
    score = 9
else:
    score = -1

visuals = True
sounds = [ pygame.mixer.Sound("one.wav"),
pygame.mixer.Sound("two.wav"),
pygame.mixer.Sound("three.wav"),
pygame.mixer.Sound("four.wav") ]

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)
for i,pin in enumerate(switches):
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)
for _,pin in enumerate(leds):
    GPIO.setup(pin, GPIO.OUT)

def all_on():
    for _,pin in enumerate(leds):
        GPIO.output(pin, True)
        
def all_off():
    for _,pin in enumerate(leds):
        GPIO.output(pin, False)
        
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
        score += 1
        
        if score == 5: noteSpeed -= .1; playSpeed -= .1
        elif score == 7: noteSpeed -= .1; playSpeed -= .1
        elif score == 10: noteSpeed -= .1; playSpeed -= .05
        elif score == 13: noteSpeed -= .1; playSpeed -= .1
        elif score == 15: visuals = False
        
        seq.append(randint(0,3))
        
        if DEBUG:
            if len(seq) > 3:
                print()
            print(f"Seq={seq}")
            print(f"Your score is currently {score}")
            
        if visuals:
            if DEBUG:
                print("there are visuals")
            for s in seq:
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(noteSpeed)
                GPIO.output(leds[s],False)
                sleep(playSpeed)
        else:
            if DEBUG:
                print("no visuals")
            for s in seq:
                sounds[s].play()
                sleep(noteSpeed)
                sleep(playSpeed)
                
        
        switchCount = 0
        
        while switchCount < len(seq):
            
            pressed = False
            
            while not pressed:
                
                for i,pin in enumerate(switches):
                    while GPIO.input(pin):
                        val = i
                        pressed = True
            
            GPIO.output(leds[val], True)
            sounds[val].play()
            sleep(1)
            GPIO.output(leds[val], False)
            sleep(0.25)
            
            if val != seq[switchCount]:
                print(f"You made it to a sequence of {score}")
                lose()
                GPIO.cleanup()
                exit(0)

            switchCount += 1

    
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nSionara!")
