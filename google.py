from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = ''

google_places = GooglePlaces(YOUR_API_KEY)

query_result = google_places.nearby_search(
        location='Austin, Texas', keyword='pool services',
        radius=20000, types=[types.TYPE_FOOD])

for result in query_result.places:
	print(result.place_id)
