from django.urls import path

from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/',AddPost.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view() ,name='contact' ),

    path('login/', LoginUser.as_view(),name='login'),
    path('register/', RegisterUser.as_view(),name='register'),
    path('logout/', logout_user,name='logout'),
   
    path('post/<slug:post_slug>', ShowPost.as_view(),name='post'),
    path('category/<slug:cat_slug>', ShowCategory.as_view(),name='category')
     
]