from rest_framework import serializers
from .models import Rating , Course 
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
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


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','date_joined']
        extra_kwargs  = {'passowrd':{'write_only':True, 'required':True}}

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user  
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        return super().update(instance, validated_data)
    