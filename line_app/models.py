from django.db import models

# Create your models here.
class Campaign(models.Model):
    id = models.AutoField('campaign_id', primary_key=True)
    
    name = models.CharField('campaign_name',max_length=255)
    
    benefit_type = models.CharField()
    
    benefit_value = models.ImageField()
    
    start_date = models.DateField()
    
    end_date = models.DateField()
    
    describtion = models.CharField()
    
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model) :
    id= models.AutoField('user_id', primary_key=True)
    
    line_user_id = models.CharField(max_length=255)
    
    display_name = models.CharField(max_length=255)
    
    campaign_id = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)  