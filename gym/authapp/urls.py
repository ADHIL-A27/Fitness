from django.urls import path
from authapp import views

urlpatterns = [
   path('',views.home,name="home"),
   path('signup',views.signup,name="signup"),
   path('login',views.handlelogin,name="handlelogin"),
   path('logout',views.handlelogout,name="handlelogout"),
   path('contact',views.contact,name="contact"),
   path('profile',views.profile,name="profile"),
   path('gallery',views.gallery,name="gallery"),
   path('attendence',views.attendence,name="attendence"),
   path('join',views.enroll,name="enroll"),
]

