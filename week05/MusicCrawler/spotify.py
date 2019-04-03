import mutagen
import os
import vlc
from collections import OrderedDict
class Song:
    def __init__(self,path,tags,name):
        self.tags=tags
        self.path=path
        self.name=name
    @classmethod
    def parse_song_from_mutagen_dict(cls,path,filetype):
        name=path.split('/')[-1]
        return cls(path,filetype.tags,name)
    def __str__(self):
        return "{} properties: {}".format(self.name,self.tags)

class Playlist:
    def __init__(self,name):
        self._songs=OrderedDict()#name:
        self.cur_playlist_song=None
        self.name=name

    def list_playlist_songs(self):
        for songName,song in self._songs.items():
            print(song)
    def add_song(self,song):
        self._songs[song.name]=song
        self.cur_playlist_song=song
    def empty(self):
        return self._songs=={}
    def get_song(self,songname):
        return self._songs[songname]
    def next(self):
        _songs.move_to_end(cur_playlist_song.name)


class Spotify:
    def __init__(self, dirpath):
        #parsing folder  -> creating a playlist for every song
        self.playlists={}
        self.currentSong=None
        self.vlc_player=None
        for root, dirnames, filenames in os.walk(dirpath):
            #for every Folder create a PLaylist
            # print(root,dirnames,filenames)
            if filenames==[]:
                continue
            cur_playlist = Playlist(root.split('/')[-1])
            for file in filenames:
                filepath=root + "/" + file
                filetype=mutagen.File(filepath) 
                if filetype==None:
                    continue
                else:
                    cur_playlist.add_song(Song.parse_song_from_mutagen_dict(filepath, filetype))
            if not cur_playlist.empty():
                self.playlists[cur_playlist.name] = cur_playlist

    def playPlaylist(self,playlistName):
        self.playSong(playlistName)

    def playSong(self,playlistName,songName=None):
        if songName==None:
            currentSong=self.playlists[playlistName].cur_playlist_song
        else:
            currentSong=self.playlists[playlistName].get_song(songName)
        self.instance=vlc.Instance()
        self.vlc_player=self.instance.media_player_new()
        self.vlc_player.set_mrl("file:///" + currentSong.path)
        self.vlc_player.play()

    def listPlaylists(self):
        for playlistName in self.playlists:
            print(playlistName)

    def listAllSongs(self):
        for playlistName, playlist in self.playlists.items():
            print(playlistName)
            playlist.list_playlist_songs()
            print("--------------")
    def stop(self):
        self.vlc_player.stop()




























