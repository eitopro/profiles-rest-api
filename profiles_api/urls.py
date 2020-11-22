from django.urls import path, include
from profiles_api import views

"""For ViewsetAPI"""
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
"""End For ViewsetAPI"""

"""for Profiles ViewSet """
router.register('profile', views.UserProfileViewSet)
"""end"""

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]