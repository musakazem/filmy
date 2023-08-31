from configuration import Configs


class LinkGenerator:
    @staticmethod
    def get_imdb(movie_id, data=None):
        from versions.v2.services import get_data
        from versions.v2.utils import get_uri
        if not data:
            uri = get_uri(movie_id)
            data = get_data(uri=uri)
        imdb_id = data.get("imdb_id")
        return f"{Configs.imdb_base_url}{imdb_id}"

    @staticmethod
    def get_youtube(movie_id, data=None):
        from versions.v2.services import get_data
        from versions.v2.utils import get_uri
        if not data:
            uri = get_uri(movie_id, True)
            data = get_data(uri=uri)
        video = data["videos"]["results"][0] if data["videos"] else ""
        if video:
            video_id = video["key"]
            return f"{Configs.youtube_base_url}{video_id}"
        return None
