from django.forms import ValidationError
from rest_framework import viewsets, status
from .models import Rating, Course
from .serializers import RatingSerializer, CourseSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny ,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrAdmin
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset  = Course.objects.all()
    serializer_class = CourseSerializer
    course1 = Course()
    print(course1.id)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Extra actions ViewSets
    @action(detail=True, methods=['POST','GET'])
    def rate_course(self, request,pk=None):
        data = request.data

        if 'stars' in data :
            course = Course.objects.get(id=pk)
            user = request.user
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def update(self, request, *args, **kwargs):
        return Response({
            'message': 'this is not allowed to Update'
        },
        status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        return Response({
            'message': 'this is not allowed to Create'
        },
        status=status.HTTP_400_BAD_REQUEST)
    


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'destroy']:  # GET, DELETE
            permission_classes = [IsAdminUser]
        elif self.action == 'create':  # POST
            permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update']: # PUT, PATCH
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]