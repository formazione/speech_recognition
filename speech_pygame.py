import pygame
import os
from glob import glob
import time
import speech_recognition as sr


gameDisplay = pygame.display.set_mode((400, 400))

pngs = [x for x in glob("animals\\*.PNG")]
names = [x.split(".")[0] for x in glob("animals\\*.PNG")]
print(pngs)
print(names)
for n, animals in enumerate(pngs):
    guess_counter = 0
    carImg = pygame.image.load(os.path.join('', animals))
    gameDisplay.blit(carImg,(130,0))
    pygame.display.update()
    # pygame.mixer.Sound.play(Tiger)
    # pygame.mixer.music.stop()
    # time.sleep(1)
    for j in range(1,4):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print ('Say Something!')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print(text)
                except:
                    print('Did not get that try Again')
                    text=''
                if text == names[n].split("\\")[1]:
                    print('good job\n=========\n\n') 
                    #pygame.mixer.Sound.play(right)
                    # pygame.mixer.music.stop()
                    break
                else:
                    if guess_counter < 3:
                        print('wrong try again')
                        # pygame.mixer.Sound.play(wrong)
                        # pygame.mixer.music.stop()
                        # time.sleep(1)
                        guess_counter += 1
    time.sleep(1)

pygame.quit()

