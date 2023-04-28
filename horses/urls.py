from django.urls import path
from .views import HorseDetail


urlpatterns = [
    path('<int:pk>/', HorseDetail.as_view(), name='horse_detail'),
]
