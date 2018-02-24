import webbrowser

class Movie():
    """ This class provide store to movies valid information """

    def __init__(self, title, storyline, image_trailer,youtube_trailer):
        self.title = title
        self.storyline = storyline;
        self.poster_image_url = image_trailer
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)
