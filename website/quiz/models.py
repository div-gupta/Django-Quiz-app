from django.db import models


# Create your models here.


class Java(models.Model):
    Question = models.CharField(max_length=4000,null = True)
    incorrect_option1 = models.CharField(max_length=100,null = True)
    
    incorrect_option2= models.CharField(max_length=100,null = True)
    incorrect_option3 = models.CharField(max_length=100,null = True)
    correct = models.CharField(max_length=100,null = True)
    

    




