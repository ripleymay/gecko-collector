from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('geckos/', views.geckos_index, name='index'),
    path('geckos/<int:gecko_id>/', views.geckos_detail, name='detail'),
    path('geckos/create/', views.GeckoCreate.as_view(), name='geckos_create'),
    path('geckos/<int:pk>/update', views.GeckoUpdate.as_view(), name='geckos_update'),
    path('geckos/<int:pk>/delete', views.GeckoDelete.as_view(), name='geckos_delete')
]