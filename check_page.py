import requests
import pygame
import time
import webbrowser
import re

def get_url():
    global min
    global url

    print("")
    message = "send url >> https//:www."
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.06) 

    url = input()
    min=float(input("chek time? (min) : "))


get_url()

while(True):
    global url
    global min


    try:
        response = requests.get(f'https://{url}', timeout=6)
        response.raise_for_status()
        print("Website is accessible and opened correctly")

        webbrowser.open(f'https://{url}')




        pygame.mixer.init()
        sound = pygame.mixer.Sound('mu.mp3')
        try:
            sound.play()
        except:
            print('no play')
        time.sleep(sound.get_length())
        pygame.mixer.quit()


    except requests.exceptions.Timeout as error:
        print(f"Request to {url} timed out: {error}")
    except requests.exceptions.HTTPError as error:
        print(f"Unable to access {url}: {error}")
        get_url()

        
    except requests.exceptions.RequestException as error:
        print(f"Unable to connect to {url}: {error}")
        get_url()

        

    time.sleep(min*60) 

