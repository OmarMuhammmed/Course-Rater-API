from django.urls import path,include
from rest_framework import routers
from .views import CourseViewSet,RatingViewSet,UserViewSet  


router = routers.DefaultRouter()
router.register('courses', CourseViewSet)
router.register('ratings', RatingViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('/', include(router.urls))
]
