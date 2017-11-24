class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating):
        '''This sets out the necessary information that is needed for an object to be created in the class Movie'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating

    def add_ratings(self):
        '''This function adds the rating to the end of the title of the film if it's one of the valid ratings so that people can see if its appropriate before clicking on it'''
        VALID_RATINGS = ["U", "PG", "12a", "12", "15", "18"]
        if self.rating in VALID_RATINGS:
            title = self.title + ' (' + self.rating +')'
            return title
        else:
            return self.title
