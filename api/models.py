from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import Avg

CATEGORIES = [
    ('Frontend Development', 'Frontend Development'),
    ('Backend Development', 'Backend Development'),
    ('Mobile Development', 'Mobile Development'),
    ('AI Development', 'AI Development'),
    ('Embedded Systems Development', 'Embedded Systems Development'),
]

class Instructor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    # override django defualt id and use uuid
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=60)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=50, choices=CATEGORIES,default=None)
    duration = models.FloatField(help_text="Duration of the course in hours")

    _avg_rating = None
    def num_of_rating(self):
        return Rating.objects.filter(course=self).count()
        
    @property
    def avg_rating(self):
        if self._avg_rating is None:
            avg_ratings = Rating.objects.filter(course=self).aggregate(Avg('stars'))
            self._avg_rating = avg_ratings['stars__avg']
        return self._avg_rating if self._avg_rating is not None else 0
            
    
    def __str__(self):
        return self.title




class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    stars = models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])


    class Meta:
        unique_together = ['user', 'course']
        