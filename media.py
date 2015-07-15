class Movie():
    """ This class provides a way to store movie related information """
    # Create Movie Attributes
    def __init__(self, movie_title, movie_storyline, movie_cast,
                 poster_image_url, trailer_youtube_url):

        self.title = movie_title
        self.storyline = movie_storyline
        self.cast = movie_cast
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
