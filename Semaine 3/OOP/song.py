import os

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

class Album:
    """ Class to represent an album
    Attributes:
        album_name (str): The name of the album
        year (int): The year of the album release
        artist (Artist): The artist of the album. If not specified, the artist will default 
        to an artist with the name "Various Artists"
        tracks (List[Song]): A list of the songs in the album. 
    
    Methods:
        add_song(song): Adds a song to the album's track list. 
    """
    
    def __init__(self, album_name, year, artist=None):

        """Album init method
        Args:
            album_name (str): Initializes the name of the album
            artist (Artist): Initializes the artist of the album
            year (int): Initializes the year of the album release
        """
        self.album_name = album_name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []
        
    def add_song(self, song, position=None):
        """Adds a song to the album's track list. 
        Args:
            song (Song): The song to be added to the album's track list
            position (Optional[int]): If specified, the song will be added to that position in the track list. 
            Otherwise, the song will be added to the end of the track list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)
            
class Artist:
    """ Class to represent an artist
    Attributes:
        name (str): The name of the artist
        albums (List[Album]): A list of the albums by the artist.
                The List includes only those albums in this collection, it is
                not an exhaustive list of the artist's published albums.
    Methods:
        add_album(album): Adds an album to the artist's album list.
    """
    
    def __init__(self, name):
        """Artist init method
        Args:
            name (str): Initializes the name of the artist
        """
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Adds an album to the artist's album list.
        Args:
            album (Album): The album to be added to the artist's album list.
                if the album is already present, it will not be added again.
        """
        if album not in self.albums:
            self.albums.append(album)
            
def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    
    with open(os.path.join(os.path.dirname(__file__), "albums.txt"), "r", encoding="utf-8") as albums:
        for line in albums:
            # Artist name, Album name, Year, Song title
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))
            
            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # We've just read details for a new artist
                # store the current album in the currents artists collection then create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.album_name != album_field:
                # We've just read details for a new album
                # store the current album in the currents artists collection then create a new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)
                
            # Create a new song object and add it to the current album's track list
            new_song = Song(song_field, new_artist.name)
            new_album.add_song(new_song)
        # After reading the last line of the text file, we will have an album and artist that haven't been stored
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)
    return artist_list

def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file"""
    with open(os.path.join(os.path.dirname(__file__), "checkfile.txt"), "w", encoding="utf-8") as checkfile:
        for artist in artist_list:
            for album in artist.albums:
                for song in album.tracks:
                    print("{}\t{}\t{}\t{}".format(artist.name, album.album_name, album.year, song.title), file=checkfile)


                

if __name__ == "__main__":
    #help(Song.__init__)
    artists = load_data()
    print("There are {} artists".format(len(artists)))
    create_checkfile(artists)