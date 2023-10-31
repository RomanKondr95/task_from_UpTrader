from django.urls import path
from . import views

urlpatterns = [
    path('my_page/', views.my_page_view, name='my_page'),
]
