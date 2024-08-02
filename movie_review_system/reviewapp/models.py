from django.db import models



class Movie_review(models.Model):
    
    movie_detail = [('Published','Published'),('NotPublished','NotPublished')]
    
    content = [('Horror','Horror'),('Comedy','comedy'),('Action','Action'),('Sci-Fi','Sci-Fi'),('Triller','Triller')]
    
    id = models.IntegerField(primary_key=True)
    movieTitle = models.CharField(null=False ,max_length=100)
    director = models.CharField(null=False, max_length=100)
    reviewContent = models.TextField()
    rating = models.IntegerField(null=False)
    created_At = models.DateField()
    rewiever_emil_Id = models.EmailField()
    status = models.CharField(max_length=100, choices=movie_detail)
    genres = models.CharField(max_length=100,choices=content)
    