from serpapi import GoogleSearch
import os
import time

import json 
with open("data2.json", "r") as f:
  data = json.load(f)


f = open('pool_names.txt', 'a',encoding="utf-8")

x = 0
for item in data:
  city = item['name']
  state = item['usps']
  if state=="TX" or state=="AZ" or state=="CA" or state=="FL" or state=="NM" or state=="NV":

    for start in range(0, 20):
      params = {
        "api_key": "",
        "engine": "google",
        "q": "pool cleaning %s, %s" % (city, state),
        #"q": "%s, %s" % (city, state),
        #"location": "%s, United States" % city,
        "google_domain": "google.com",
        "gl": "us",
        "hl": "en",
        "tbm": "lcl",
        "num": "250",
        "start": "%s" % start
      }

      search = GoogleSearch(params)
      results = search.get_dict()

      _results = results.get('local_results', [])

      for result in _results:
        title = result.get('title', 'None') 
        the_type = result.get('type', 'None')
        phone = result.get('phone', 'None')
        address = result.get('address', 'None')
        city = city
        state = state
        rating = result.get('rating', 0)
        reviews = result.get('reviews', 0)
        review = result.get('review', 'None')
        years = result.get('years_in_business', 'None')
        gps = result.get('gps_coordinates', 'None')
        if gps != "None":
          lat = gps.get('latitude', 0)
          lon = gps.get('longitude', 0)
        else:
          lat = 0
          lon = 0
        links = result.get('links', 'None')
        if links != "None":
          website = links.get('website')
        else:
          website = "None"
        if the_type == "Pool cleaning service":
	        output = str("%s" % title)
	        print(output)
	        print(output, file=f)

      time.sleep(0.20)
