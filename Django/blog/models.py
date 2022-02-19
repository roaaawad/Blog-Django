from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# each class has one table in database and each attribute of class will be field in table in db
# the post model and the user model going to have relationship since users we going to author post
class Post(models.Model):
   title = models.CharField(max_length= 100)
   content = models.TextField()
   date_posted = models.DateTimeField(default=timezone.now)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   def __str__(self):
      return self.title
   def get_absolute_url(self):
      return reverse('post-detail',kwargs={'pk':self.pk})
