import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_crud.settings')
django.setup()
from django.contrib.auth.models import User
from django.utils import timezone
from movies.models import Movie

Movie.objects.all().delete()

admin = User.objects.get(username='admin')

movies = [
    {
        'title': 'Venom',
        'genre': 'Science Fiction',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vel ullamcorper orci. Proin fringilla velit at condimentum scelerisque. Proin vel pellentesque orci. Mauris viverra sem sed magna dignissim, id tempor libero congue. Integer eget maximus arcu. Quisque fringilla orci non tempor ullamcorper. Vivamus congue tempor tellus id mattis. Nulla maximus libero sed enim ornare, et bibendum dui placerat.',
        'imageUrl': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQL-C2COfSsCkq3_x3dKXWmYyMJWhgRx0icOg&usqp=CAU',
        'year': 2018,
    },
    {
        'title': 'Halloween',
        'genre': 'Horror',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vel ullamcorper orci. Proin fringilla velit at condimentum scelerisque. Proin vel pellentesque orci. Mauris viverra sem sed magna dignissim, id tempor libero congue. Integer eget maximus arcu. Quisque fringilla orci non tempor ullamcorper. Vivamus congue tempor tellus id mattis. Nulla maximus libero sed enim ornare, et bibendum dui placerat.',
        'imageUrl': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVjx5DR1OF6veOuLZWsi181OV4445Lx7Vq4g&usqp=CAU',
        'year': 2018,
    },
    {
        'title': 'Logan',
        'genre': 'Comics',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vel ullamcorper orci. Proin fringilla velit at condimentum scelerisque. Proin vel pellentesque orci. Mauris viverra sem sed magna dignissim, id tempor libero congue. Integer eget maximus arcu. Quisque fringilla orci non tempor ullamcorper. Vivamus congue tempor tellus id mattis. Nulla maximus libero sed enim ornare, et bibendum dui placerat.',
        'imageUrl': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSD1D320iQ764Hwcz5F-Txi-WLeqHj6JYUiUg&usqp=CAU',
        'year': 2017,
    },
    {
        'title': 'Joker',
        'genre': 'Comics',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vel ullamcorper orci. Proin fringilla velit at condimentum scelerisque. Proin vel pellentesque orci. Mauris viverra sem sed magna dignissim, id tempor libero congue. Integer eget maximus arcu. Quisque fringilla orci non tempor ullamcorper. Vivamus congue tempor tellus id mattis. Nulla maximus libero sed enim ornare, et bibendum dui placerat.',
        'imageUrl': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDJtSHfYpMEgchl0uQwRv7oQtH4SBg7LbT5A&usqp=CAU',
        'year': 2019,
    },
    {
        'title': 'The Dark Knight',
        'genre': 'Action',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vel ullamcorper orci. Proin fringilla velit at condimentum scelerisque. Proin vel pellentesque orci. Mauris viverra sem sed magna dignissim, id tempor libero congue. Integer eget maximus arcu. Quisque fringilla orci non tempor ullamcorper. Vivamus congue tempor tellus id mattis. Nulla maximus libero sed enim ornare, et bibendum dui placerat.',
        'imageUrl': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdMxPKaZr38NM9FqwDtF2Y6TeeXUCeU-7c7A&usqp=CAU',
        'year': 2008,
    },{
        'title': 'Mortal Kombat',
        'genre': 'Action',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vel ullamcorper orci. Proin fringilla velit at condimentum scelerisque. Proin vel pellentesque orci. Mauris viverra sem sed magna dignissim, id tempor libero congue. Integer eget maximus arcu. Quisque fringilla orci non tempor ullamcorper. Vivamus congue tempor tellus id mattis. Nulla maximus libero sed enim ornare, et bibendum dui placerat.',
        'imageUrl': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRl-oLtvtfmJN_eS8xPmQ6e15ZpBZ2o-Fpt0w&usqp=CAU',
        'year': 2019
    }
]

for movie_data in movies:
    movie = Movie()
    movie.title = movie_data['title']
    movie.genre = movie_data['genre']
    movie.description = movie_data['description']
    movie.imageUrl = movie_data['imageUrl']
    movie.year = movie_data['year']
    movie.creator = admin
    movie.save()
