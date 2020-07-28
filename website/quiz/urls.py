from django.urls import path
from . import views

urlpatterns=[
    path('index',views.index,name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('contact',views.contact,name='contact'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('quiz',views.quiz,name='quiz'),
    path('score',views.score,name='score'),
    path('logout',views.logout,name='logout')
   

    
]