from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('geckos/', views.geckos_index, name='index'),
    path('geckos/<int:gecko_id>/', views.geckos_detail, name='detail'),
    path('geckos/create/', views.GeckoCreate.as_view(), name='geckos_create'),
    path('geckos/<int:pk>/update', views.GeckoUpdate.as_view(), name='geckos_update'),
    path('geckos/<int:pk>/delete', views.GeckoDelete.as_view(), name='geckos_delete'),
    path('geckos/<int:gecko_id>/add_snack/', views.add_snack, name='add_snack'),
    path('geckos/<int:gecko_id>/assoc_tankitem/<int:tankitem_id>/', views.assoc_tankitem, name='assoc_tankitem'),
    path('geckos/<int:gecko_id>/unassoc_tankitem/<int:tankitem_id>/', views.unassoc_tankitem, name='unassoc_tankitem'),
    path('tankitems/', views.TankItemList.as_view(), name='tankitems_index'),
    path('tankitems/<int:pk>/', views.TankItemDetail.as_view(), name='tankitems_detail'),
    path('tankitems/create/', views.TankItemCreate.as_view(), name='tankitems_create'),
    path('tankitems/<int:pk>/update/', views.TankItemUpdate.as_view(), name='tankitems_update'),
    path('tankitems/<int:pk>/delete/', views.TankItemDelete.as_view(), name='tankitems_delete'),
]