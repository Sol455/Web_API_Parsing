#! python3

import requests

def retrieve_packs():
    packs = requests.get('https://api.ampifymusic.com/packs')
    return packs.json()

def get_sort_genres(json_data):
    genre_names = set()

    for pack in json_data["packs"]:
        for genre in pack["genres"]:
            genre_names.add(genre)
    sort_genre_names = sorted(genre_names)
    return sort_genre_names

def main():
    json_data = retrieve_packs()
    genre_names = get_sort_genres(json_data)\
    #print(json_data)
    print("\n%s genres found in packs:\n" % len(genre_names))

    for genre in genre_names:
        print("%s" % genre)

if __name__ == "__main__":
    main()