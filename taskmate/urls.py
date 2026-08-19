

from django.urls import path, include
from django.contrib import admin

from todolist_app import views as todolist_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist_app.urls',)),
    path('account/', include('users_app.urls',)),
    path('', todolist_views.index, name='index'),
    path('contact/', todolist_views.contactM, name='contact'),
    path('home/', todolist_views.homeM, name='home_url'),
]