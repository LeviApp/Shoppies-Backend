from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.

class Awards(models.Model):
    userID = models.CharField(max_length=20)
    Title = models.CharField(max_length=200, null=True)
    Year = models.CharField(max_length=10, null=True)
    Rated = models.CharField(max_length=10, null=True)
    Released = models.CharField(max_length=20, null=True)
    Runtime = models.CharField(max_length=20, null=True)
    Genre = models.CharField(max_length=200, null=True)
    Director = models.CharField(max_length=50, null=True)
    Writer = models.TextField(null=True)
    Actors = models.TextField(null=True)
    Plot = models.TextField(null=True)
    Language = models.CharField(max_length=200, null=True)
    Country = models.CharField(max_length=200, null=True)
    Awards = models.CharField(max_length=200, null=True)
    Poster = models.TextField(null=True)
    Ratings = models.TextField(null=True)
    Metascore = models.CharField(max_length=10, null=True)
    imdbID = models.CharField(max_length=20, null=True)
    Type = models.CharField(max_length=20, null=True)
    DVD = models.CharField(max_length=20, null=True)
    BoxOffice = models.CharField(max_length=20, null=True)
    Production = models.CharField(max_length=20, null=True)
    Website = models.TextField(null=True)
    Response = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.Title

    # {
    #   "Title": "Night at the Museum",
    #   "Year": "2006",
    #   "imdbID": "tt0477347",
    #   "Type": "movie",
    #   "Poster": "https://m.media-amazon.com/images/M/MV5BMTQyOTM4MDMxN15BMl5BanBnXkFtZTcwODg5NTQzMw@@._V1_SX300.jpg"
    # },

    # userID = models.CharField(max_length=20)
    # Title = models.CharField(max_length=200, default="N/A")
    # Year = models.CharField(max_length=10, default="N/A")
    # Rated = models.CharField(max_length=10, default="N/A")
    # Released = models.CharField(max_length=20, default="N/A")
    # Runtime = models.CharField(max_length=20, default="N/A")
    # Genre = ArrayField(models.CharField(max_length=20), default = list)
    # Director = models.CharField(max_length=50, default="N/A")
    # Writers = ArrayField(models.CharField(max_length=50), default = list)
    # Actors = ArrayField(models.CharField(max_length=50), default = list)
    # Plot = models.TextField(default="N/A")
    # Language = ArrayField(models.CharField(max_length=20), default = list)
    # Country = ArrayField(models.CharField(max_length=20), default = list)
    # Awards = ArrayField(models.CharField(max_length=20), default = list)
    # Poster = models.URLField(null=True)
    # Ratings = ArrayField(JSONField(), default = list)
    # Metascore = models.IntegerField(null=True)
    # imdbRating: models.FloatField(null=True)
    # imdbVotes: models.IntegerField(null=True)
    # imdbID = models.CharField(max_length=20)
    # Type = models.CharField(max_length=20, default="N/A")
    # DVD = models.CharField(max_length=20, default="N/A")
    # BoxOffice = models.CharField(max_length=20, default="N/A")
    # Production = models.CharField(max_length=20, default="N/A")
    # Website = models.URLField(null=True)
    # Response = models.BooleanField(default=True)