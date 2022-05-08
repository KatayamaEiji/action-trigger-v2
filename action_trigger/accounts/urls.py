from django.urls import path
from django.views.generic import RedirectView

from .views import hellow
from .views import home
from .views import postlist
from django.contrib.auth import views

urlpatterns = [
    path('', home.Home.as_view(),name="home"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('hello/', hellow.helloworldfunction),
    path('post_list/', postlist.PostListView.as_view(), name='post_list'), # ここを追加
]