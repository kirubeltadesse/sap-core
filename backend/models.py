from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# create a mode with multiple user types
# class User(AbstractUser):
#     userTypeChoices = (
#         ('student', 'Student'),
#         ('mentor', 'Mentor'),
#         ('staff', 'Staff'),
#         ('admin', 'Admin'),
#     )

#     role = models.CharField(max_length=10, choices=userTypeChoices, default='student')
#     email = models.EmailField(max_length=254, unique=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     name = models.CharField(max_length=100, blank=False, null=True)
#     phone = models.CharField(max_length=20, blank=True, null=True)


class Rootuser(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# # create a model with two different user
# class Mentor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='mentor')
#     category = models.ManyToManyField(Category)
#     def __str__(self):
#         return self.user.username

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='student')
#     category = models.ManyToManyField(Category)
#     def __str__(self):
#         return self.user.username

# Create Event model with title, content, date_posted, student, mentor, start_date, end_date, category, status
class Event(models.Model):

    class EventObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)

    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor')
    date_posted = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager()  # The default manager.
    eventobjects = EventObjects() # custom manager for published posts 
    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return self.title
