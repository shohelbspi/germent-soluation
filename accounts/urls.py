from django.urls import path
from accounts import views,authViews


urlpatterns = [
    path('',authViews.singin,name='admin_singin'),
    path('user-create/',authViews.singup,name='singup'),
    path('user-list/',authViews.user_list.as_view(),name='user_list'),
    path('singout/', authViews.singout, name='singout'),
    path('dashboard/',authViews.dashboard,name='dashboard'),
]
