import requests


url = input("send url : ")


try:
    response = requests.get(f'https://{url}', timeout=5)
    response.raise_for_status()
    print("Website is accessible and opened correctly")
except requests.exceptions.Timeout as error:
    print(f"Request to {url} timed out: {error}")
except requests.exceptions.HTTPError as error:
    print(f"Unable to access {url}: {error}")
except requests.exceptions.RequestException as error:
    print(f"Unable to connect to {url}: {error}")