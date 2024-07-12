from django.urls import path

from .views import RegisterCreateAPIView

urlpatterns = [
    path("register/", RegisterCreateAPIView.as_view()),
]
