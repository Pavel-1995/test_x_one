from django.urls import path

from .views import logout_user, redirect_url_view


urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
    path('all_urls/',  views.all_urls, name='all_urls'),
]
