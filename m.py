import webbrowser
class M():
    """this is M class which contain two def
which contain all data of the movie"""
    def __init__(self, t, story, pi, ty):
        self.title = t
        self.storyline = story
        self.poster_image_url = pi     
        self.trailer_youtube_url = ty      
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
""" webbrowser imported to open the web link"""
