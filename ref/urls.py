from django.urls import path

from . import views

urlpatterns = [
    path('subscriber/', views.subscriber),
    path('invite/send', views.invite)
]