from django.contrib import admin
from django.urls import path
from bookapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book', views.book),
    path('pencil', views.pencil),
]