from django.urls import path
from . import views

urlpatterns = [
    path("buku", views.daftar_buku, name="daftar_buku"),
    path("buku/<int:id>", views.detail_buku, name="detail_buku"),
]
