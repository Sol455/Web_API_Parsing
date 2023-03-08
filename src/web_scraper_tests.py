import os
import json
import unittest
from web_scraper import retrieve_packs, get_sort_genres, get_genres_hiphop

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
print(DATA_DIR)


class ParseTests(unittest.TestCase):

    def test_fetch_data(self):
        fetched_data = retrieve_packs()
        file_path = os.path.join(DATA_DIR, "data.json")
        print (file_path)
        f = open(file_path, "w")
        f.write(json.dumps(fetched_data, indent=4))
        f.close()
        self.assertIsNotNone(fetched_data)

    def test_get_sorted_genres(self):
        file_path = os.path.join(DATA_DIR, "data.json")

        with open(file_path, "r") as f:
            data = json.loads(f.read())

        genre_names = get_sort_genres(data)
        self.assertTrue(len(genre_names) > 0)

        for i in range(len(genre_names) - 2):
            self.assertTrue(genre_names[i] < genre_names[i + 1])

    def test_get_hiphop_pack_name(self):
        file_path = os.path.join(DATA_DIR, "data.json")

        with open(file_path, "r") as f:
            data = json.loads(f.read())

        hiphop_packs = get_genres_hiphop(data)
        self.assertTrue(len(hiphop_packs) > 0)

        for pack in hiphop_packs:
            self.assertTrue("hip-hop" in pack["genres"])