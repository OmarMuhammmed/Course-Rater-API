from django.urls import path,include
from rest_framework import routers
from .views import CourseViewSet,RatingViewSet


router = routers.DefaultRouter()
router.register('courses', CourseViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('/', include(router.urls))
]
