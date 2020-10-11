from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('api/v1/users/', views.UserView.as_view()),
    # path('api/v1/users/search', views.SearchUserView.as_view()),
    path('', views.home_view, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('movie/<int:pk>/', views.movie, name='movie'),
    path('profile/', views.profile, name='profile'),
    path('order/', views.order, name='order'),
    # path('api/v1/users/<int:id>/', views.UserDetailView.as_view()),
    # path('api/v1/users/<int:user_id>/contacts/', views.ContactListView.as_view()),
    # path('api/v1/users/<int:user_id>/contacts/<int:contact_id>/', views.UserDetailView.as_view()),
    # path('api/v1/users/<int:user_id>/spam_contacts/', views.SpamView.as_view()),
    # path('api/v1/users/<int:user_id>/spam_contacts/<int:spam_id>/', views.UserDetailView.as_view()),
]