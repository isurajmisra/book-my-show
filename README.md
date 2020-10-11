# BookMyShow

Steps to run the API
## Install dependencies
```
pip install -r requirements.txt
```


##Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

## Create SuperUser 
```
python manage.py createsuperuser
admin
admin@gmail.com
123
123
yes

```

## Create Sample Data

```
python manage.py shell
from main.sample_data import *
create_users()
add_movies()
add_theater()
add_movie_timing()
make_orders()
```

## Runserver
```
python3 manage.py runserver
```

## Test the API

```
Route: http://localhost:8000/login/
Request Type: POST
Data: 

    {
        "email":"suraj@gmail.com",
        "password":"test"
    }
```

## Admin Panel


```
You can add movies, Theaters  and Timing from admin panel.
```


