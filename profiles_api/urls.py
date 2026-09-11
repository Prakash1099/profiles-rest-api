from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset'), # no need '/' here
router.register('profile', views.UserProfileViewSet) 
# Since we assigned a queryset in this view, we dont need to specify a basename
# names will be taken from the queryset by the Django

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
    
]
