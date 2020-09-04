
from django.contrib import admin
from django.urls import path
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name="home"),
    path('aboutus/', views.about_us, name='aboutus'),
    path('suggessions/',views.suggessions , name='suggest'),
    
]
