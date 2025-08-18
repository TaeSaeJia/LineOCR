from django.urls import path
from .views import OCRView, HomeView,THOCRView

urlpatterns = [
    path('',  OCRView.as_view(), name='ocr'),
    path('th', THOCRView.as_view(), name='TH_OCR')
]