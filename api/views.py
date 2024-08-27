from rest_framework import viewsets
from .models import Rating, Course
from .serializers import RatingSerializer, CourseSerializer 
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset  = Course.objects.all()
    serializer_class = CourseSerializer
    
class RatingViewSet(viewsets.ModelViewSet):
    queryset  = Rating.objects.all()
    serializer_class = RatingSerializer
