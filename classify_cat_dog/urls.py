# classify_cat_dog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UploadedImageViewSet

router = DefaultRouter()
router.register(r'images', UploadedImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-and-classify/', UploadedImageViewSet.as_view({'post': 'upload_and_classify'})),
]
