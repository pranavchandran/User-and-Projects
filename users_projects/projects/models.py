from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    project_name = models.CharField(max_length=200)
    project_desc = models.CharField(max_length=200)
    project_image = models.CharField(max_length=500,default="https://cdn.dribbble.com/users/1012566/screenshots/4187820/topic-2.jpg")

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse('projects:detail',kwargs={"pk": self.pk})
