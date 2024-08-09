from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Movie_review(models.Model):

    movie_detail = [('Published','Published'),('NotPublished','NotPublished')]
    
    CONTENT= [('Horror','Horror'),('Comedy','comedy'),('Action','Action'),('Sci-Fi','Sci-Fi'),('Triller','Triller')]
    
    id = models.IntegerField(primary_key=True)
    movieTitle = models.CharField(null=False ,max_length=100)
    director = models.CharField(null=False, max_length=100)
    reviewContent = models.TextField()
    rating = models.IntegerField(choices=[(i,str(i)) for i in range(1,6)])
    created_At = models.DateField(auto_now_add=True)
    rewiever_emil_Id = models.EmailField()
    status = models.CharField(max_length=100, choices=movie_detail)
    genres = models.ManyToManyField(Genre, related_name='movies')
    