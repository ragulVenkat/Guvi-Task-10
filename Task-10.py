# Track Class
class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_info(self):
        return f"Title: {self.title}, Artist: {self.artist}, Duration: {self.duration}"


# Playlist Class
class Playlist:
    def __init__(self):
        self.tracks = []
        self.current_index = 0

    def add_track(self, track):
        self.tracks.append(track)

    def remove_track(self, track):
        self.tracks.remove(track)

    def next_track(self):
        if self.current_index < len(self.tracks) - 1:
            self.current_index += 1
        return self.tracks[self.current_index]

    def previous_track(self):
        if self.current_index > 0:
            self.current_index -= 1
        return self.tracks[self.current_index]


# MusicPlayer Class
class MusicPlayer:
    def __init__(self):
        self.playlist = Playlist()
        self.current_track = None

    def play(self):
        if self.current_track is None and self.playlist.tracks:
            self.current_track = self.playlist.tracks[self.playlist.current_index]
        print(f"Playing: {self.current_track.get_info()}")

    def stop(self):
        print(f"Stopping: {self.current_track.get_info()}")
        self.current_track = None

    def add_to_playlist(self, track):
        self.playlist.add_track(track)
        print(f"Added: {track.get_info()} to playlist")

    def remove_from_playlist(self, track):
        self.playlist.remove_track(track)
        print(f"Removed: {track.get_info()} from playlist")

# Example usage
track1 = Track("Song A", "Artist A", "3:30")
track2 = Track("Song B", "Artist B", "4:00")

player = MusicPlayer()
player.add_to_playlist(track1)
player.add_to_playlist(track2)
player.play()
player.stop()
