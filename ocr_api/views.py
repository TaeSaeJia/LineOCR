from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
import cv2
import numpy as np
from paddleocr import PaddleOCR
import tempfile
from .extraction import extrac_total_prize, extrac_date_branch
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"


ocr_model = PaddleOCR(use_angle_cls=True, lang='en')  # หรือ 'th' สำหรับภาษาไทย

class OCRView(APIView):
    parser_classes = [MultiPartParser]
    
    def get(self, request):
        # render หน้า form HTML
        return render(request, 'ocr_form.html')
    
    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image')
        if not image_file:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_img:
            for chunk in image_file.chunks():
                temp_img.write(chunk)
            temp_img.flush()
            print(temp_img.name)
            result = ocr_model.predict(temp_img.name)

        # แปลงผลลัพธ์เป็น JSON-friendly format
        output = []
        for picture in result:
            output.append({
                'total' : extrac_total_prize(picture['rec_texts']),
                "date" : extrac_date_branch(picture['rec_texts']),
                'texts': picture['rec_texts'],
                'confidence': picture['rec_scores'],
                'box': picture['rec_polys']
            })

        return Response(output, status=status.HTTP_200_OK)