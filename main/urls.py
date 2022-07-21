
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('new_todo', views.newtodo, name='new_todo'),
    path('detail/<int:id>/', views.delete, name='delete')
]
