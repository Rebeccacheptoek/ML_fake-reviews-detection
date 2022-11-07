from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reviews.app.reviewsapp.views import EndpointViewSet
from reviews.app.reviewsapp.views import MLAlgorithmViewSet
from reviews.app.reviewsapp.views import MLAlgorithmStatusViewSet
from reviews.app.reviewsapp.views import MLRequestViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    path(r"^api/v1/", include(router.urls)),
]