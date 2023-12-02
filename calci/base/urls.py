from django.urls import path
from. import views

    




urlpatterns = [
    
    path("",views.home,name="main"),
    path("profile/",views.profile,name="profile page"),
     path("calculator/",views.calci,name="calculator"),
    
    
]