from django.db import models
from line_app.models import User,Campaign

# Create your models here.


class Receipt(models.Model):
    id = models.AutoField('receipt_id', primary_key=True)
    
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_receipt'
    )
    
    campaign_id = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        related_name='campaign_receipt'
    )
    
    image_path = models.ImageField(upload_to='raw_image/')
    
    detection = models.JSONField(blank=True, null=True)
    
    parsed_data = models.JSONField(blank=True, null=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
