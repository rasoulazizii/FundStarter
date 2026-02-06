from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, DonationViewSet


router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaigns')
router.register(r'donation', DonationViewSet, basename='donations')

urlpatterns = [

]

urlpatterns += router.urls