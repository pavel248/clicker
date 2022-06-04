from django.urls import path

from clicker import settings
from . import views
from django.contrib.auth.views import LogoutView

boosts = views.BoostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
lonely_boost = views.BoostViewSet.as_view({
    'put': 'partial_update', # редактировать буст
})


urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('call_click/', views.call_click),
    path('', views.index, name='index'),
    path('boosts/', boosts, name='boosts'),
    path('boost/<int:pk>/', lonely_boost, name='boost'),
    path('update_coins/', views.update_coins),
    path('core/', views.get_core)
]