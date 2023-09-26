from django.urls import path

from . import views

app_name='store'

urlpatterns = [
    path('', views.home,name="home"),
    path('allbooks/<slug:e>', views.allbooks, name="allbooks"),
    path('viewbook/<slug:e>', views.viewbook, name="viewbook"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),

]