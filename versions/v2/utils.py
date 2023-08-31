from versions.v2.services import get_movie_obj_list, get_movie_detail_obj
from configuration import Configs


def get_query_list(message):
    movie_list = get_movie_obj_list(message)
    if not movie_list:
        return

    message = str()
    for movie in movie_list:
        title = movie["title"]
        movie_id = movie["id"]
        imdb = movie["imdb_link"]
        message += f"{title} ({movie_id}) ({imdb}) \n"

    return message


def get_movie_detail_query(movie_id):
    movie_detail = get_movie_detail_obj(movie_id)
    title = movie_detail["title"]
    rating = movie_detail["rating"]
    status = movie_detail["status"]
    overview = movie_detail["overview"]
    imdb = movie_detail["imdb"]
    youtube = movie_detail["youtube"]
    return f"{title}\n{rating}\n{status}\n{overview}\n{imdb}\n{youtube}\n"

def get_uri(movie_id, get_video=False):
    video_tag = ""
    if get_video:
        video_tag = "&append_to_response=videos"

    uri = f"{Configs.api_base_url}{Configs.api_get_movie}{movie_id}?{Configs.api_key}{video_tag}"
    return uri
