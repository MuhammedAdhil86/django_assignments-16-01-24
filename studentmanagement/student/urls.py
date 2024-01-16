from django.urls import path
from student import views


urlpatterns = [
  
   path('',views.home,name='home'),
   path('register/',views.reg,name='register'),
   path('login/',views.login,name='login')
]