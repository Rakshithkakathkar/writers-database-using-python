from django import forms
from django.contrib.auth.models import User  #gives the generic user class which we can use, that can be tweaked
from .models import Movie, Writer, TvShow


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['Title','Year','Studio','Movie_writer']


class WriterForm(forms.ModelForm):

    class Meta:
        model = Writer
        fields = ['Writer', 'Bday', 'Literacy_agency', 'Writer_pic']


class TvShowForm(forms.ModelForm):

	class Meta:
		model = TvShow
		fields = ['Name', 'Total_seasons', 'Series_Writer']        

		
			

		
