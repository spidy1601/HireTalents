from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    company_name = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=50)
    phone = models.BigIntegerField()

    def __str__(self):
        return self.company_name[:30]

class Question(models.Model):
    TYPES=[('radio','radio'),('choice','choice'),('text','text')]
    type=models.CharField(max_length=6,choices=TYPES)
    question_text=models.CharField(max_length=500)

    def __str__(self):
        return self.question_text[:30]

class Option(models.Model):
    option_text = models.CharField(max_length=500)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.option_text[:30]
    
class UserRequirement(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    


