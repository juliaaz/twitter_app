import requests
import certifi

import ssl

import geopy.geocoders

from geopy.geocoders import Nominatim

ctx = ssl.create_default_context(cafile=certifi.where()) 
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent="twitter friends", scheme='http')
from geopy.exc import GeocoderUnavailable
from geopy.exc import GeocoderTimedOut
from flask import Flask, render_template, request 

import folium
app = Flask(__name__)

def get_info(bearer_token, screen_name):
  """
  Sends request to Twitter with the help of bearer token.
  Returns json with the information about first 50 friends of user with given username.
  """
  base_url = 'https://api.twitter.com/'
  search_headers = {
    'Authorization': 'Bearer {}'.format(bearer_token)
    }
  search_params = {
    'screen_name': '{}'.format(screen_name),
    'count': 50
  }
  search_url = '{}1.1/friends/list.json'.format(base_url)

  response = requests.get(search_url, headers=search_headers, params=search_params)
  json_response = response.json()
  return json_response
# print(get_info('AAAAAAAAAAAAAAAAAAAAAG6RMwEAAAAA280ZhavKwLDo0iERLhKFJN11htg%3Dd2g3YwRtkITfpQUlhnTuJZRsVsmrXRMQzh6sMVBjhCpJwDYHh1', '@elonmusk'))
def get_friends_coordinates(json_response):
  """
  Function gets a dictionary and returns a list
  of tuples with each friend's coordinates.
  """
  friends_list = []
  for user in json_response['users']:
    location = user['location']
    nickname = user['screen_name']
    friends_list.append([nickname, location])

  new_friends_list = []  
  for friend in friends_list:
    try:
      location = geolocator.geocode(friend[1])
      new_friends_list.append([friend[0], location.latitude, location.longitude])
    except AttributeError:
      continue
    except GeocoderTimedOut:
      continue
    except GeocoderUnavailable:
      continue
  return new_friends_list
# print(get_friends_coordinates(get_info('AAAAAAAAAAAAAAAAAAAAAG6RMwEAAAAA280ZhavKwLDo0iERLhKFJN11htg%3Dd2g3YwRtkITfpQUlhnTuJZRsVsmrXRMQzh6sMVBjhCpJwDYHh1', '@elonmusk')))
def create_map(new_friends_list):
  """
  Function creates an html map with markers as friends' locations.
  """
  mapp = folium.Map(tiles='CartoDB dark_matter')
  folium.TileLayer('OpenStreetMap').add_to(mapp)
  folium.TileLayer('CartoDB positron').add_to(mapp)
  folium.TileLayer('Stamen Terrain').add_to(mapp)
  fig = folium.FeatureGroup(name = 'Twitter Friends')
  for friend in new_friends_list:
    fig.add_child(folium.Marker(location=[friend[1], friend[2]],
                                popup=friend[0],
                                icon=folium.Icon(color='blue', icon='user', prefix='fa')))

  mapp.add_child(fig)
  mapp.add_child(folium.LayerControl())
  mapp.save('templates/Twitter_Friends.html')

@app.route("/")
def index():
  """
  Function creates the main page of the app.
  """
  return render_template("index.html")

@app.route("/map", methods=["POST"])
def final_map():
  """
  Function creates a final map about friends.
  """
  try:
    nickname = request.form.get("screen_name")
    request_token = request.form.get("bearer_token")
    if not nickname or not request_token:
      return render_template("failure.html")
    json_response = get_info(request_token, nickname)
    create_map(get_friends_coordinates(json_response))

    return render_template("Twitter_Friends.html")
  except KeyError:
    return render_template("failure.html")

if __name__ == "__main__":
  app.run(debug=False)

