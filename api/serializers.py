from rest_framework import serializers
from .models import Rating , Course 

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", 
                  "title", 
                  "instructor",
                  "description",
                  "category",
                  "duration",
                  "num_of_rating",
                  "avg_rating",
                  )
