# importing requests library
import requests 

# using requests to recieve data about Nirvana from MusicBrainz
response = requests.get('http://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?inc=aliases',

  # setting headers to accept JSON rather than XML
  headers={'Accept' : 'application/json'}
)

# printing the JSON response
print(response.json())
