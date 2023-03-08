#! python3

import requests

def retrieve_packs():
    packs = requests.get('https://api.ampifymusic.com/packs')
    return packs.json()

def main():
    json_data = retrieve_packs()
    print(json_data)

if __name__ == "__main__":
    main()