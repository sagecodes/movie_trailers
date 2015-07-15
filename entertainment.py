import media
import them_apples

# Movie Attributes order: title, storyline, cast, image URL, trailer URL.
kung_fury = media.Movie(
          "Kung Fury",
          "Kung fu guy becomes time traveling nazi killer",
          "That kung fu guy",
          "https://upload.wikimedia.org/wikipedia/en/thumb/0/0d/Kung_Fury_Poster.png/220px-Kung_Fury_Poster.png",  # NOQA
          "https://www.youtube.com/watch?v=72RqpItxd8M")

batman_begins = media.Movie(
              "Batman Begins",
              "Rich guy becomes coolest ninja ever",
              "That rich guy",
              "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/Batman_Begins_Poster.jpg/220px-Batman_Begins_Poster.jpg",  # NOQA
              "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

iron_man = media.Movie(
          "Iron Man",
          "Rich guy becomes coolest metal man ever",
          "That rich guy, no the OTHER rich guy",
          "https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Ironmanposter.JPG/220px-Ironmanposter.JPG",  # NOQA
          "https://www.youtube.com/watch?v=8hYlB38asDY")

starwars = media.Movie(
          "Starwars Return of the Jedi",
          "whiny guy becomes powerful jedi",
          "That whiny guy",
          "https://upload.wikimedia.org/wikipedia/en/thumb/b/b2/ReturnOfTheJediPoster1983.jpg/220px-ReturnOfTheJediPoster1983.jpg",  # NOQA
          "https://www.youtube.com/watch?v=7L8p7_SLzvU")

star_trek = media.Movie(
          "Star Trek",
          "Cocky guy becomes captain of a starship",
          "That cocky guy",
          "https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Startrekposter.jpg/220px-Startrekposter.jpg",  # NOQA
          "https://www.youtube.com/watch?v=SyJszxnJydA")


movies = [kung_fury, batman_begins, iron_man, starwars, star_trek]
them_apples.open_movies_page(movies)
