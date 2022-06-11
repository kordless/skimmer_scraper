import random
import unittest
import os
import pprint
from serpapi import NaverSearch

class TestNaverSearchApi(unittest.TestCase):

		def setUp(self):
				NaverSearch.SERP_API_KEY = os.getenv("API_KEY", "demo")

		@unittest.skipIf((os.getenv("API_KEY") == None), "no api_key provided")
		def test_get_json(self):
				search = NaverSearch({"query": "Coffee"})
				data = search.get_json()
				self.assertIsNone(data.get("error"))
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["naver_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])
				if "ads_results" in data:
					self.assertIsNotNone(data["ads_results"][1]["title"])
				pp = pprint.PrettyPrinter(indent=2)
				pp.pprint(data)
				print(data.keys())

if __name__ == '__main__':
		unittest.main()
