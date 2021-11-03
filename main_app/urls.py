from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('geckos/', views.geckos_index, name='index'),
    path('geckos/<int:gecko_id>/', views.geckos_detail, name='detail'),
    path('geckos/create/', views.GeckoCreate.as_view(), name='geckos_create')
]