from django.urls import path
from .views import List,Signup,Create,Profile,chat,loginfunc
from django.conf.urls import url
from . import views

urlpatterns = [
    path("chat/",chat,name="chat"),
    path("chat/<str:room_name>/",views.room, name='room'),
    path("",Signup.as_view(),name="signup"),
    path("login/",loginfunc,name="login"),
    path("list/",List.as_view(),name="list"),
    path("create/",Create.as_view(),name="create"),
    path("<username>/",Profile.as_view(),name="profile"),




]
