from django.urls import path
from . import views

urlpatterns = [
    path('', views.icecream_list, name='icecream_list'),
    path('icecream/<int:pk>', views.icecream_detail, name='icecream_detail'),
    path('icecream/new', views.icecream_create, name='icecream_create'),
    path('icecream/<int:pk>/edit', views.icecream_edit, name='icecream_edit'),
    path('icecream/<int:pk>/delete', views.icecream_delete, name='icecream_delete'),
]