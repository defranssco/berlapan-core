from django.urls import path

from .views import ListDonor, DetailDonor

urlpatterns = [
    path('', ListDonor.as_view()),
    path('<int:pk>/', DetailDonor.as_view()),
]