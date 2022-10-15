from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):

    STATUS_BACKLOG = 'B'
    STATUS_BLOCKED = 'l'
    STATUS_PROGRESS = 'P'
    STATUS_REVIEW = 'R'
    STATUS_CLOSED = 'C'

    STATUS_CHOICES = [
       (STATUS_BACKLOG, 'Backlog'),
       (STATUS_BLOCKED, 'Blocked'),
       (STATUS_PROGRESS, 'Progress'),
       (STATUS_REVIEW, 'Review'),
       (STATUS_CLOSED, 'Closed'),
   ]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    status = models.CharField(max_length=1,choices=STATUS_CHOICES, default=STATUS_PROGRESS)
    file = models.FileField(upload_to ='file/',blank=True, null=True,)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(null=True,blank=True)
    is_completd = models.BooleanField(default=False)
    draft = models.BooleanField(default=True)


    # project url
    def get_absolute_url(self):
        return f"/project/{self.slug}"

    def __str__(self):
        return self.name+ " -> Start Date: "+ str(self.start_date)+ " -> End Date: "+ str(self.end_date)





