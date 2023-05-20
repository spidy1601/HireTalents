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
        #reason for plus 1 is because we are adding it after form submits not during.
        self.answer_id = max_id + 1
        
        super().save(self,*args, **kwargs)

class ClientDetail(models.Model):
    selected_ids=models.CharField(max_length=300)
    detail_id = models.IntegerField(unique=True)
    meeting_done = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Get the maximum ID of ModelB
        max_id = UserAnswer.objects.aggregate(max_id=Max('id'))['max_id']
        
        if self.detail_id != max_id:
            # Set the value of field_a in ModelA to max_id
            self.detail_id = max_id
        
        super().save(*args, **kwargs)

