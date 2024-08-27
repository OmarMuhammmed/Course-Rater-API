from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MaxValueValidator,MinValueValidator

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

    def __str__(self):
        return self.title

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    stars = models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])


    class Meta:
        unique_together = ['user', 'course']
        