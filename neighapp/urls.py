from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    re_path('hood/(?P<location>\w+)',views.single_hood, name="single_hood"),
    re_path('profile/(?P<username>\w+)',views.profile, name="profile"),
    path('search_business',views.search_business,name="search-business"),
]