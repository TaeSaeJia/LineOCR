from django.db import models
from line_app.models import User,Campaign

# Create your models here.

class Receipt(models.Model):
    id = models.AutoField('receipt_id', primary_key=True)
    
    user_id = models.IntegerField('user_id')
    
    campaign_id = models.IntegerField('campaign_id')
    
    image_path = models.ImageField(upload_to='raw_image/')
    
    detection = models.JSONField(blank=True, null=True)
    
    parsed_data = models.JSONField(blank=True, null=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
