from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('logout',views.LogOut,name='logout'),
    path('register', views.register_user, name='register_user'), 
    path('createReview/', views.CreateReview, name='CreateReview'),
    path('ShowReviews/', views.ShowReviews, name='ShowReviews'),
    path('delete/<review_id>',views.DeleteReview,name='delete'),
    path('inicio/',views.Inicio,name="inicio/"),
    path('myReviews/',views.ShowMyReviews,name='myReviews')
    
]         