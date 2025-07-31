from django.urls import path
from .views import OCRView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('ocr/', OCRView.as_view(), name='ocr'),
]