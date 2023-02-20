from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginUser,name='loginUser'),
    path('signup/', views.signupUser,name='signupUser'),
    path('logout/', views.logoutUser,name='logoutUser'),
    path('delete_rooms/', views.delete_rooms,name='delete_rooms'),
    path('<str:room>/', views.room, name="room"),
    path('checkview', views.checkview, name="checkview"),
    path('send', views.send, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages")
]
