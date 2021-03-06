import mutagen
import os
class LengthParsed:
    def __init__(self,length="0:0:0"):
        self._hours, self._minutes, self._seconds = __parse_from_string(length)

    def __parse_from_string(self,string):
        if ':' not in string:
            return (0,0, int(string))
        temp = string.split(':')
        if len(temp) == 2:
            return (0, int(temp[0]), int(temp[1]) )
        else:
            return ( int(temp[0]), int(temp[1]) )
    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._minutes + self._hours * 60

    @property
    def seconds(self):
        return self._seconds + self.minutes * 60

    def __add__(self,other):
        self._hours += other.hours
        self._minutes += other.minutes
        self._seconds += other.seconds
        if _seconds >= 60:
            _minutes += _seconds // 60
            _seconds = _seconds % 60
        if _minutes >=60:
            _hours += _minutes // 60
            _minutes = _minutes % 60
        return self

    def __str__(self):
        if hours==0:
            return "{minutes} : {seconds}".format(self.minutes, self.seconds)
        return "{hours} : {minutes} : {seconds}".format(self.hours, self.minutes, self.seconds)
#expected format [hours:minutes:seconds]
#[seconds]
#[minutes:seconds]

class Song:
    def __init__(self, title, artist, album, length):
        self._title = title
        self._artist = artist
        self._album = album
        self._length = LengthParsed(length)

    def __str__(self):
        return "{artist} - {title} from {album} - {length}".format(self._artist, self._title, self._album, self._length)

    def __eq__(self,other):
        return self._title == other.title and self._artist == other.artist

    def __hash__(self):
        return self._title.__hash__

    @property
    def artist(self):
        return self._artist
    

    @property
    def length(hours=False,minutes=False,seconds=False):
        if seconds == True:
            return self._length.seconds

        if minutes == True:
            return self._length.minutes

        if hours == True:
            return self._length.hours

        return str(self._length)

class Playlist:
    def __init__(self, name, repeat=False, shuffle=True):
        self._name = name
        self._repeat = repeat
        self._shuffle = shuffle
        self._songs = []
        self._current_song_idx=0

    def total_length(self):
        sum_length = LengthParsed()
        for song in self._songs:
            sum_length += LengthParsed(song.length)
        return str(sum_length)

    def add_song(self, song):
        self._songs.append(song)

    def remove_song(self, song):
        for idx, entry in enumerate(self._songs):
            if song == entry:
                del self._songs[idx]
                return True
        return False

    def add_songs(self,songs):
        for song in songs:
            self.add_song(song)
        return True

    def next_song(self):
            self._current_song_idx = (self._current_song_idx +1) % len(self._songs)
        if self._repeat == False and _current_song_idx == 0:
                return "end of playlist"

        return self._songs[current_song_idx]

    def pprint_playlist(self):
        for song in sorted(self.songs, key=artist):
            print(str(song))
            
    def save(self):
        filename=''
        for char in self.name:
            if char==' ':
                filename += '_'
            else:
                filename += char
        with open(filename) as f:
            json.dumps(self,f)

    @staticmethod
    def load(path):
        with open(path) as json_file:
            data=json.loads(json_file)

            instance_of_playlist = Playlist(path.split('/')[-1])
            #todo
            instance_of_playlist.__dict__ = data
        return instance_of_playlist

class MusicCrawler:
    #fix music crawler
    def __init__(self,fold_path):
        self.playlists={}
        for root, dirnames, filenames in os.walk(dirpath):
            #for every Folder create a PLaylist
            if filenames==[]:
                continue
            cur_playlist = Playlist(root.split('/')[-1])
            for file in filenames:
                filepath = root + "/" + file
                filetype = mutagen.File(filepath) 
                if filetype == None:
                    continue
                else:
                    cur_playlist.add_song(Song.parse_song_from_mutagen_dict(filepath, filetype))
            if not cur_playlist.empty():
                self.playlists[cur_playlist.name] = (cur_playlist, root)#playlist and path
class MusicPlayer
    def __init__(self):
        self.myMusic = MusicCrawler('/home/mitakaxd/code/python101/Python101/Python101/week05/music/')
    def playPlaylist(self,playlistName):
        self.playSong(playlistName)

    def playSong(self,playlistName,songName=None):
        if songName == None:
            currentSong = self.myMusic.playlists[playlistName][0].cur_playlist_song
        else:
            currentSong = self.myMusic.playlists[playlistName][0].get_song(songName)
        self.instance = vlc.Instance()
        self.vlc_player = self.instance.media_player_new()
        self.vlc_player.set_mrl("file:///" + self.myMusic.playlists[playlistName][1]+ '/' + currentSong.name)
        self.vlc_player.play()

    def listPlaylists(self):
        for playlistName in self.myMusic.playlists[0]:
            print(playlistName)

    def listAllSongs(self):
        for playlistName, playlist in self.myMusic.playlists[0].items():
            print(playlistName)
            playlist.list_playlist_songs()
            print("--------------")
    def stop(self):
        self.vlc_player.stop()