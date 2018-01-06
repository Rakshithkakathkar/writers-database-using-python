from django.db import models
from django.contrib.auth.models import Permission, User

class Writer(models.Model):
	user = models.ForeignKey(User, default=1)
	Writer = models.CharField(max_length=25)
	Bday = models.DateField('D.O.B')
	Literacy_agency = models.CharField(max_length=25)
	Writer_pic = models.FileField()

	def __str__(self):
		return self.Writer+' - ' + self.Literacy_agency
	

class Movie(models.Model):
	Title = models.CharField(max_length=25)
	Year = models.IntegerField()
	Studio = models.CharField(max_length=20)
	Movie_writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
	
	
	

	def __str__(self):
		return self.Title


class TvShow(models.Model):
	Name = models.CharField(max_length=25)
	Total_seasons = models.IntegerField()
	Series_Writer = models.ForeignKey(Writer, on_delete=models.CASCADE)

	def __str__(self):
		return self.Name

		


# Create your models here.
