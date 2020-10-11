from django.contrib import admin
from .models import *

# Register your models here.

admin.register(User)
admin.site.register(Theater)
admin.site.register(Movie)
admin.site.register(MovieTimeing)
admin.site.register(Order)