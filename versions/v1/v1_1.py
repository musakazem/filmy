import requests
import json

from configuration import Configs

root = Configs.api_base_url
api_key = Configs.api_key

def query(st):
	cleaned = st.split()

	string = str()

	for clean in cleaned:
		string += clean
		if clean == cleaned[-1]:
			break
		else:
			string += "+"

	return string

def find_movie(mes):
	root = Configs.api_base_url
	api_key = Configs.api_key
	param = "search/movie?"
	q = "&query=" + query(mes)
	addr = root + param + api_key + q
	response = requests.get(addr)

	text = json.dumps(response.json(), sort_keys=True, indent=3)
	obj = json.loads(text)

	results = obj["results"]
	output = str()
	n = 7
	if(len(results) >= n):
		i = 1
		for result in results:
			if(i <= n):
				output += result["title"] + " " + "(" + str(result["id"]) + ")"
				output += "\n"
			else:
				break
			i+=1
	else:
		for result in results:
			output += result["title"] + " " + "(" + str(result["id"]) + ")"
			output += "\n"

	return output

def movie_details(mes):

  param = "movie/"
  movie_id = mes + "?"
  and_video = "&append_to_response=videos"
  addr = root + param + movie_id + api_key + and_video
  response = requests.get(addr)

  text = json.dumps(response.json(), sort_keys = True, indent = 3)
  obj = json.loads(text)

  videos = obj["videos"]
  video_results = videos["results"]
  video_key = str()

  for result in video_results:
    video_key = result["key"]
    break
  
  video_link = Configs.youtube_base_url + video_key 

  title = obj["title"]
  rating = "Rating: " + str(obj["vote_average"])
  status = "Status: " + obj["status"]
  overview = obj["overview"]
  imdb_id = obj["imdb_id"]

  imdb_link = Configs.imdb_base_url + imdb_id 

  genre_obj = obj["genres"]

  genre = str()

  for index,elem in enumerate(genre_obj):
    genre += elem["name"]

    try:
      genre_obj[index+1]
      genre += ","
    except:
      break

  l = "\n"
  output = title + l + genre + l + overview + l + rating + l + status + l + imdb_link + l + video_link

  return output
