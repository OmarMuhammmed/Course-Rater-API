from django.forms import ValidationError
from rest_framework import viewsets, status
from .models import Rating, Course
from .serializers import RatingSerializer, CourseSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset  = Course.objects.all()
    serializer_class = CourseSerializer

    # Extra actions ViewSets
    @action(detail=True, methods=['POST','GET'])
    def rate_course(self, request,pk=None):
        data = request.data

        if 'stars' in data :
            course = Course.objects.get(id=pk)
            username = data['username']
            user = User.objects.get(username = username)
            stars = data['stars']

            # if user has a rating 
            try:
                # get the rating from data
                rateing = Rating.objects.get(
                                        user = user,
                                        course = course,
                                        )
                
                rateing.stars =  stars  # update
                rateing.save()
                serializer = RatingSerializer(rateing, many=False)                     
                                                    
                return Response({
                                'message':'Rating Updated Succufully..',
                                 'res':serializer.data
                                 }
                                 ,status=status.HTTP_201_CREATED)
            # else 
            except:
                create_rate = Rating.objects.create(
                    user = user,
                    course = course ,
                    stars = stars
                )
                serializer = RatingSerializer(create_rate, many=False)
                create_rate.save()

                return Response({
                                'message':'Rating Created Succufully..',
                                'res': serializer.data
                                 }
                                 ,status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'stars not provided'},status=status.HTTP_400_BAD_REQUEST)
        

class RatingViewSet(viewsets.ModelViewSet):
    queryset  = Rating.objects.all()
    serializer_class = RatingSerializer
