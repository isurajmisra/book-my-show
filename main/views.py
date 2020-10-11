from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login
from .forms import UserRegistrationForm, UserLoginForm
from .models import *
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        # user = request.user
        movies = Movie.objects.all()
        context = {
            'movies': movies
        }
        return render(request, 'home.html', context)
    else:
        return redirect("login")

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!!")
            return redirect('login')

    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST.get('email', ''))
        if user.exists():
            if user.first().check_password(request.POST.get('password', '')):
                user_login(request, user.first())
                messages.success(request, "Login successful!!")
                return redirect('home')
            else:
                messages.error(request, "Credentials not valid!")
                return redirect('login')
        else:
            messages.error(request, "Email is not registered!")
            return redirect('register')
    form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def profile(request):
    orders = Order.objects.filter(user=request.user)
    context={
        "orders": orders
    }
    return render(request, 'profile.html', context)

def movie(request, pk=None):
    movie = get_object_or_404(Movie, pk=pk)
    theaters = Theater.objects.filter(movie=movie)
    timings = MovieTimeing.objects.filter(movie=movie)
    orders = Order.objects.all()
    available_seats = {}
    for theater in theaters:
        seats = [i for i in range(1, theater.total_seats+1)]
        for order in orders:
            if order.theater == theater and order.movie == movie:
                if order.seat_number in seats:
                    seats.remove(order.seat_number)
        available_seats[theater.name] = seats

    context = {
        'movie': movie,
        'theaters': theaters,
        'timings': timings,
        'available_seats': available_seats
    }

    return render(request, 'movie.html', context)


def order(request):
    if request.method == "POST":
        timing = get_object_or_404(MovieTimeing, pk=request.POST['select-timing'])
        seat = request.POST['select-seat']
        movie = get_object_or_404(Movie, pk=request.POST['movie'])
        theater = get_object_or_404(Theater, pk=request.POST['theater'])
        unique_id = get_random_string(length=32)
        Order.objects.create(user=request.user, movie=movie, timing=timing, theater=theater, seat_number=seat, code=unique_id)
    messages.success(request, "Show Booked Successfully.")
    messages.info(request, f"Please  copy your unique booking code : {unique_id}")
    return redirect('home')