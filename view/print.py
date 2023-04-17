import requests
from time import sleep


# URL to access model component
model_url = "http://localhost:1110/view/should_learn"


# Print response every second
def main():
    while True:
        print(requests.get(model_url).text)
        sleep(1)


if __name__ == '__main__':
    main()