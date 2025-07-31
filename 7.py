class Media:
    def play(self):
        pass

class Song(Media):
    def play(self):
        return f'Song is playing'

class Movie(Media):
    def play(self):
        return f'Movie is playing'

class Podcast(Media):
    def play(self):
        return f'Podcast is playing'                       

p = Podcast()
s = Song()
m = Movie()

print(f'{p.play()}\n{m.play()}\n{s.play()}')