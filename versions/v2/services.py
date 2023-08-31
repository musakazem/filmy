import requests

from configuration import Configs
from versions.v2.external_link import LinkGenerator


def get_query(message):
    query_message = message.replace(" ", "+")
    return "&query=" + query_message


def get_data(message=None, uri=None):
    if not uri:
        query = get_query(message)
        uri = Configs.api_base_url + Configs.api_search_movie + Configs.api_key + query
    response = requests.get(uri)

    return response.json()


def get_movie_obj_list(message):
    data = get_data(message=message)
    if not data["results"]:
        return

    movie_list = list()
    for index, movie in enumerate(data["results"]):
        if index + 1 == Configs.query_limitation:
            break
        movie_id = movie.get("id")
        data_map = {
            "index": index,
            "id": movie_id,
            "title": movie.get("title"),
            "imdb_link": LinkGenerator.get_imdb(movie_id),
        }
        movie_list.append(data_map)
    return movie_list


def get_movie_detail_obj(movie_id):
    from versions.v2.utils import get_uri

    uri = get_uri(movie_id, True)
    data = get_data(uri=uri)
    rating = data["vote_average"]
    status = data["status"]
    data_map = {
        "title": data["title"],
        "rating": f"Rating: {rating}",
        "status": f"Status: {status}",
        "overview": data["overview"],
        "imdb": LinkGenerator.get_imdb(movie_id, data),
        "youtube": LinkGenerator.get_youtube(movie_id, data),
    }
    return data_map
