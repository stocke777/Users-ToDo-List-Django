
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('front.urls')),
    path('register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = "users/login.html"), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = "users/logout.html"), name = 'logout'),
    path('profile/', user_views.profile, name = 'profile'),
    path('todo/', user_views.todo, name = 'todo'),
    path('delete/<int:tid>', user_views.delete, name = 'delete'),
    path('create/', user_views.create, name = 'create'),
]
