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


def get_genres_hiphop(json_data):
    hiphop_packs = []

    for pack in json_data["packs"]:
        if "hip-hop" in pack["genres"]:
            hiphop_packs.append(pack)

    return hiphop_packs


def main():
    json_data = retrieve_packs()
    genre_names = get_sort_genres(json_data)
    hiphop_packs = get_genres_hiphop(json_data)
    print("\nFound %s different genres in packs:\n" % len(genre_names))

    for genre in genre_names:
        print("%s" % genre)

    print("\nFound %s packs under the genre Hip-Hop:\n" % len(hiphop_packs))

    for pack in hiphop_packs:
        print("%s" % pack["name"])


if __name__ == "__main__":
    main() 