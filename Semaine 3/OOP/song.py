class Song:
    """ Class to represent a song
    Attributes:
        title (str): The title of the song
        artist (str): The artist of the song
        duration (int): The duration of the song in seconds. Maybe 0 
    """
    
    def __init__(self, title, artist, duration = 0):
        """Song init method
        Args:
            title (str): Initializes the title of the song
            artist (str): Initializes the artist of the song
            duration (Optional[int]): Initializes the duration of the song in seconds. Maybe 0 
        """
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print(f"Playing '{self.title}' by {self.artist} for {self.duration} seconds.")