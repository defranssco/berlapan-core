# from django.urls import path

# from . import views

# app_name = 'main'

# urlpatterns = [
#     path('', views.home, name='home'),
# ]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name="singup"),
    path('signin/', views.signin, name="singin"),
    path('signout/', views.signout, name="singout"),
    # path('register/',views.userprofile, name='register')
    path('json', views.flutter, name= 'json'),
    
]