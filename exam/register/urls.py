from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name="all_product"),
    path('create_product/', views.create_view),
    path("main/<int:id>/", views.detail_view, name="detail_view"),
    path("main/<int:id>/delete/", views.delete_view, name="delete_view"),
    path("main/<int:id>/update/", views.update_view, name="update_view"),
]