from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from . views import (
    UserViewSet, GasStationViewSet, FuelViewSet,
    ManagerViewSet, StaffViewSet, PriceManagementViewSet,
    TransactionSalesViewSet, TypeOfFuelViewSet
    )


router = DefaultRouter()
router.register(r'user', UserViewSet, basename='users')
router.register(r'manager', ManagerViewSet, basename='managers')
router.register(r'staff', StaffViewSet, basename='staffs')
router.register(r'gas-station', GasStationViewSet, basename='gas')
router.register(r'fuel-pricing', FuelViewSet)
router.register(r'price-management', PriceManagementViewSet)
router.register(r'sales', TransactionSalesViewSet)
router.register(r'type-of-fuel', TypeOfFuelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]