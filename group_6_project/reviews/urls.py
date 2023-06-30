from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('logout',views.LogOut,name='logout'),
    path('register', views.register_user, name='register_user'), 
    path('createReview/', views.CreateReview, name='CreateReview'),
    path('ShowReviews/', views.ShowReviews, name='ShowReviews'),
    path('deleteSR/<review_id>',views.DeleteReviewSR,name='delete'),
    path('dislike/<review_id>',views.DislikeReview,name='dislike'),
    path('like/<review_id>',views.LikeReview,name='like'),
    path('commentSR/<review_id>',views.Comment,name='comment'),
    path('deleteComment/<com_id>',views.DeleteComment,name='deleteComment'),    
    # path('deleteMR/<review_id>',views.DeleteReviewMR,name='deleteMR'),
    path('inicio/',views.Inicio,name="inicio/"),
    path('myReviews/',views.ShowMyReviews,name='myReviews'),
    path('modify/<review_id>',views.ModifyReview,name='modify'),
    path('details/<review_id>',views.reviewDetails,name='details'),
    path('modifiedReview/<review_id>',views.ModifiedReview,name='modifiedReview'),
    path('myReviewsFilter/',views.filterMyReviews,name='filterMyReviews'),
    path('AllReviewsFilter/',views.filterAllReviews,name='filterAllReviews'),
]         