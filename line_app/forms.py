from django import forms
from .models import Campaign, User

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
