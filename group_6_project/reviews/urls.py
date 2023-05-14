from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('logout',views.LogOut,name='logout'),
    path('register', views.register_user, name='register_user'), 
    path('createReview/', views.CreateReview, name='CreateReview'),
    path('ShowReviews/', views.ShowReviews, name='ShowReviews'),
    path('deleteSR/<review_id>',views.DeleteReviewSR,name='delete'),
    # path('deleteMR/<review_id>',views.DeleteReviewMR,name='deleteMR'),
    path('inicio/',views.Inicio,name="inicio/"),
    path('myReviews/',views.ShowMyReviews,name='myReviews'),
    path('modify/<review_id>',views.ModifyReview,name='modify'),
    path('modifiedReview/<review_id>',views.ModifiedReview,name='modifiedReview'),
]         