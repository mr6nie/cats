from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.CatsView.as_view(), name="cats_list"),
]
