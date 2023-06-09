import requests
import pygame
import time
import webbrowser

url = input("send url : ")

while(True):

    try:
        response = requests.get(f'https://{url}', timeout=5)
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
    except requests.exceptions.RequestException as error:
        print(f"Unable to connect to {url}: {error}")

    time.sleep(5) # 1500 = 5min

