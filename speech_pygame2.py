import pygame
import os
from glob import glob
import time
import speech_recognition as sr
from random import shuffle

gameDisplay = pygame.display.set_mode((400, 400))

pngs = [x for x in glob("animals\\*.PNG")]
names = [x.split(".")[0] for x in glob("animals\\*.PNG")]

animals = {k:v for k, v in zip(pngs, names)}
print(animals)


print(pngs)
print(names)
keys = list(animals.keys())
shuffle(keys)

score = 0
for animal in keys:
    guess_counter = 0
    carImg = pygame.image.load(os.path.join('', animal))
    gameDisplay.blit(carImg,(130,0))
    pygame.display.update()
    # pygame.mixer.Sound.play(Tiger)
    # pygame.mixer.music.stop()
    # time.sleep(1)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('What\'s his name!')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print('Did not get that try Again')
            text=''
        if text == animals[animal].split("\\")[1]:
            print('good job\n=========\n\n') 
            #pygame.mixer.Sound.play(right)
            # pygame.mixer.music.stop()
            score += 1
            # break
        else:
            if guess_counter < 3:
                print('wrong try again\n')
                # pygame.mixer.Sound.play(wrong)
                # pygame.mixer.music.stop()
                # time.sleep(1)
                guess_counter += 1
            else:
                pygame.quit()

                  
    gameDisplay.fill((0,0,0))
    print(f"{score}")

pygame.quit()

