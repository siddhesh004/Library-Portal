"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books.views import home_view, about_view, borrow_view, issue_request_view, return_request_view
from books import views as core_views
from books import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('books/', home_view, name='index'),
    path('books/about/', about_view, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('books/my_books/', borrow_view, name='return'),
    path('books/signup', core_views.signup, name='signup'),
    path('books/books/', views.BookListView.as_view(), name='issue'),
    path('books/book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<uuid:pk>', issue_request_view, name='change_status'),
    path('book/return/<uuid:pk>', return_request_view, name='new_status'),

]
