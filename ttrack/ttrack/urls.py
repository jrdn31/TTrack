"""ttrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from tracker.views import KitListView, ReqListView
from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.items, name='items'),
    path('items/<int:pk>',views.ItemDetailView.as_view(), name= 'item-detail'),
    path('item/new', views.new_item, name = 'new_item'),
    path('item/edit/<int:pk>/', views.item_edit, name='item_edit'),
    path('kits',KitListView.as_view(), name='kit-list' ),
    path('kit/new', views.new_kit, name = 'new_kit'),
    path('kit/<int:pk>',views.KitDetailView.as_view(), name= 'kit-detail'),
    path('kit/edit/<int:pk>/', views.kit_edit, name='kit_edit'),
    path('reqs',ReqListView.as_view(), name='req-list' ),
    path('request/edit/<int:pk>/', views.req_edit, name='req_edit'),

]
