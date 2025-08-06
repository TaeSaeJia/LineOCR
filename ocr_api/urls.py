from django.urls import path
from .views import OCRView, HomeView

urlpatterns = [
    path('',  OCRView.as_view(), name='ocr'),
]