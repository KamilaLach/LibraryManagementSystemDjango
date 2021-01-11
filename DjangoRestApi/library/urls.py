from django.conf.urls import url

from library import views
from django.urls import path

from library.models import Book
from library.models import Category

urlpatterns = [
    url(r'^api/books$', views.book_list),
    url(r'^api/books/(?P<pk>[0-9]+)$', views.book_detail),
    url(r'^api/books/available$', views.book_list_available),
    url(r'^api/books/not-available$', views.book_list_not_available),
    url(r'^api/categories$', views.category_list),
    url(r'^api/categories/(?P<pk>[0-9]+)$', views.category_detail),
    path('hello/', views.HelloView.as_view(), name='hello'),
]

