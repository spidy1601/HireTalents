from django.db import models
from djf_surveys.models import UserAnswer
# Create your models here.
class DeveloperImage(models.Model):
    answer_id = models.ForeignKey(UserAnswer,on_delete=models.CASCADE)
    developer_image = models.ImageField(upload_to='images/')



