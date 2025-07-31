from django.db import models

# Create your models here.
class Campaign(models.Model):
    id = models.AutoField('campaign_id', primary_key=True)
    


class User(models.Model) :
    id= models.AutoField('user_id', primary_key=True)