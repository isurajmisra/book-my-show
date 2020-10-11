from django.contrib.auth.hashers import make_password
from .models import *
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

def create_users():
    sample_data = [
        {
            'username': 'suraj',
            'email': 'isurajmisra@gmail.com',
        },
        {
            'username': 'sachin',
            'email': 'sachin@gmail.com',
        },
        {
            'username': 'manish',
            'email': 'manish@gmail.com',
        },
        {
            'username': 'aditya',
            'email': 'aditya@gmail.com',
        },
        {
            'username': 'sagar',
            'email': 'sagar@gmail.com',
        },
    ]
    User.objects.bulk_create([
        User(
            username=data['username'],
            email=data['email'],
            password=make_password('123')
        ) for data in sample_data
    ])
    print("created Sample User")

def add_movies():
    names = [
        "Joker",
        "Avenger End Game",
        "Avenger Infinity War",
        "Thor",
        "Hulk",
        "Madras Cafe",
        "Mission Impossible"
    ]

    Movie.objects.bulk_create([
        Movie(
            name = name
        )for name in names
    ]
    )
    print("Movies Added.")

