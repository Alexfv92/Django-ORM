""" modulo de URL"""
from django.contrib import admin
from django.urls import path
from proyecto import views as local_views
from posts import views as posts_views




urlpatterns = [
    path('admin/',admin.site.urls),
    path('hello-world/', local_views.hello_word),
    path('hi/', local_views.hi),
    path('say_hi/<str:name>/<int:age>/', local_views.say_hi),
    path('posts/',posts_views.list_post),

]
