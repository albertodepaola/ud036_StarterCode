import webbrowser


class Video:
    """Video super class used to group common attributes.

    Attributes:
        title: Video title
        duration: duration in minutes
        rating: video rating
    """
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, duration, rating):
        """Inits Video with title, duration in minutes and rating."""
        self.title = title
        self.duration = duration
        self.rating = rating


class Movie(Video):
    """Movie specific class to store custom attributes.

    The image must be publicly available, and only youtube URLS are accepted.

    Attributes:
         movie_name: movie title
         duration: duration in minutes
         movie_storyline: movie summary
         image_url: publicly available image URL
         trailer_url: embeddable youtube URL
         rating: movie rating
    """

    def __init__(self, movie_name, duration, movie_storyline,
                 image_url, trailer_url, rating):
        """Inits class movie with all its attributes."""
        Video.__init__(self, movie_name, duration, rating)
        self.storyline = movie_storyline
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        """Opens the browser using the youtube trailer URL."""
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """TV Show specific class, adds season and episode numbers.

    Attributes:
        title: episode name
        duration: duration in minutes
        season: season number
        episode: episode number
        rating: episode rating
    """
    def __init__(self, title, duration, season, episode, rating):
        """Inits class TvShow with all its attributes."""
        Video.__init__(self, title, duration, rating)
        self.season = season
        self.episode = episode
