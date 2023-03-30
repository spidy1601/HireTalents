from django.db import models
from django.db.models import Max
from djf_surveys.models import UserAnswer
# Create your models here.
class DeveloperImage(models.Model):
    # answer_id = models.ForeignKey(UserAnswer,on_delete=models.CASCADE)
    answer_id = models.IntegerField(unique=True)
    developer_image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        # Get the maximum ID of ModelB
        max_id = UserAnswer.objects.aggregate(max_id=Max('id'))['max_id']
        
        # Set the value of field_a in ModelA to max_id
        self.answer_id = max_id
        
        super(DeveloperImage, self).save(*args, **kwargs)



