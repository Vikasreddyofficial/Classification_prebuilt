# classify_cat_dog/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from .model import classify_image

class UploadedImageViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    @action(detail=False, methods=['post'])
    def upload_and_classify(self, request, *args, **kwargs):
        file_serializer = UploadedImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            image_path = file_serializer.instance.image.path
            predictions = classify_image(image_path)
            top_prediction = predictions[0]  # Get the top prediction
            return Response({
                "top_prediction": top_prediction,
                "image_url": file_serializer.instance.image.url
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
