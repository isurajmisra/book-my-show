from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Movie(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)



    def __str__(self):
        return self.name

    class Meta:
        db_table = 'movie'

class Theater(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    total_seats = models.IntegerField(null=True, blank=True)
    movie = models.ManyToManyField(Movie, related_name='theater')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'theater'



class MovieTimeing(models.Model):
    movie = models.ManyToManyField(Movie, related_name='movie_timing')
    theater = models.ManyToManyField(Theater, related_name='theater_timing')
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    class Meta:
        db_table = 'movie_timing'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    timing = models.ForeignKey(MovieTimeing, on_delete=models.DO_NOTHING, null=True)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, null=True)
    seat_number = models.IntegerField(null=True)
    code = models.CharField(max_length=100, null=True)


    class Meta:
        db_table = 'order'