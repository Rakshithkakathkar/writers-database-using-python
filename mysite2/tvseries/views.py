from django.contrib.auth import authenticate, login #authenticate is used to check if credentials are correct,login attaches a session id so that they dont have to login at each page
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Writer, Movie, TvShow
from .forms import UserForm, MovieForm, WriterForm, TvShowForm #inherits UserForm and movieform class created in forms.py


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_writer(request):
    if not request.user.is_authenticated():
        return render(request, 'tvseries/login.html')
    else:
        form = WriterForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            writer = form.save(commit=False)
            writer.user = request.user
            writer.Writer_pic = request.FILES['Writer_pic']
            file_type = writer.Writer_pic.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'writer': writer,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'tvseries/writer_form.html', context)
            writer.save()
            return render(request, 'tvseries/detail.html', {'writer': writer})
        context = {
            "form": form,
        }
        return render(request, 'tvseries/writer_form.html', context)



def create_movie(request, writer_id):
    form = MovieForm(request.POST or None, request.FILES or None)
    writer = get_object_or_404(Writer, pk=writer_id)
    if form.is_valid():
        writers_movies = writer.movie_set.all()
        for m in writers_movies:
            if m.Title == form.cleaned_data.get("Title"):
                context = {
                    'writer': writer,
                    'form': form,
                    'error_message': 'You already added that writer',
                }
                return render(request, 'tvseries/create_movie.html', context)
        movie = form.save(commit=False)
        movie.writer = writer

        movie.save()
        return render(request, 'tvseries/detail.html', {'writer': writer})
    context = {
        'writer': writer,
        'form': form,
    }
    return render(request, 'tvseries/create_movie.html', context)



def delete_writer(request, writer_id):
    writer = Writer.objects.get(pk=writer_id)
    writer.delete()
    writers = Writer.objects.filter(user=request.user)
    return render(request, 'tvseries/index.html', {'writers': writers})



def delete_movie(request, writer_id, movie_id):
    writer = get_object_or_404(Writer, pk=writer_id)
    movie = Movie.objects.get(pk=movie_id)
    movie.delete()
    return render(request, 'tvseries/detail.html', {'writer': writer})


def detail(request, writer_id):
    if not request.user.is_authenticated():
        return render(request, 'tvseries/login.html')
    else:
        user = request.user
        writer = get_object_or_404(Writer, pk=writer_id)
        return render(request, 'tvseries/detail.html', {'writer': writer, 'user': user})  


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'tvseries/login.html')
    else:
        writers = Writer.objects.filter(user=request.user)
        movie_results = Movie.objects.all()
        query = request.GET.get("q")
        if query:
            writers = writers.filter(
                Q(Writer__icontains=query) |
                Q(Literacy_agency__icontains=query)
            ).distinct()
            movie_results = movie_results.filter(
                Q(Title__icontains=query)
            ).distinct()
            return render(request, 'tvseries/index.html', {
                'writers': writers,
                'movies': movie_results,
            })
        else:
            return render(request, 'tvseries/index.html', {'writers': writers})






def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'tvseries/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                writers = Writer.objects.filter(user=request.user)                
                return render(request, 'tvseries/index.html', { 'writers': writers })
            else:
                return render(request, 'tvseries/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'tvseries/login.html', {'error_message': 'Invalid login'})
    return render(request, 'tvseries/login.html')



def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                writers = Writer.objects.filter(user=request.user)
                return render(request, 'tvseries/index.html', {"writers" : writers})
    context = {
        "form": form,
    }
    return render(request, 'tvseries/register.html', context)





def movies(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'tvseries/login.html')
    else:
        try:
            movie_ids = []
            for writer in Writer.objects.filter(user=request.user):
                for movie in writer.movie_set.all():
                    movie_ids.append(movie.pk)
            users_movies = Movie.objects.filter(pk__in=movie_ids)
            if filter_by == 'favorites':
                users_movies = users_movies.filter(is_favorite=True)
        except Writer.DoesNotExist:
            users_movies = []
        return render(request, 'tvseries/movies.html', {
            'movie_list': users_movies,
            'filter_by': filter_by,
        })


def create_tvshow(request, writer_id):
    form = TvShowForm(request.POST or None, request.FILES or None)
    writer = get_object_or_404(Writer, pk=writer_id)
    if form.is_valid():
        writers_tvshows = writer.tvshow_set.all()
        for t in writers_tvshows:
            if t.Name == form.cleaned_data.get("Name"):
                context = {
                    'writer': writer,
                    'form': form,
                    'error_message': 'You already added that tvshow',
                }
                return render(request, 'tvseries/create_tvshow.html', context)
        tvshow = form.save(commit=False)
        tvshow.writer = writer

        tvshow.save()
        return render(request, 'tvseries/detail.html', {'writer': writer})
    context = {
        'writer': writer,
        'form': form,
    }
    return render(request, 'tvseries/create_tvshow.html', context)




def delete_tvshow(request, writer_id, tvshow_id):
    writer = get_object_or_404(Writer, pk=writer_id)
    tvshow = TvShow.objects.get(pk=tvshow_id)
    tvshow.delete()
    return render(request, 'tvseries/detail.html', {'writer': writer})






















		

	    
		



	

