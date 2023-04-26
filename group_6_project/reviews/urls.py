from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('createRevier/', views.CreateReview, name='CreateReview')
]         