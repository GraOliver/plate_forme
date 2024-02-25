from django.urls import path,include
from . import views

app_name="app"
urlpatterns = [
    path('',views.page,name="accueil"),
    path('Platforme',views.Accueil,name="index")
]