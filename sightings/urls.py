from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_squirrels),
    path('add/',views.add_squirrel),
    path('stats/',views.stats),
    path('<squirrel_id>/', views.edit_squirrel),
        ]
