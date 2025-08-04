from django.shortcuts import render, redirect
from .models import Campaign, User
from .forms import CampaignForm, UserForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# --- หน้า HTML ---
def campaign_form(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('campaign_list')
    else:
        form = CampaignForm()
    return render(request, 'campaign_form.html', {'form': form})

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaign_list.html', {'campaigns': campaigns})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


# --- REST API ---
@api_view(['GET', 'POST'])
def api_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return Response({'id': instance.id}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        data = list(Campaign.objects.values())
        return Response(data)

@api_view(['GET', 'POST'])
def api_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return Response({'id': instance.id}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        data = list(User.objects.values())
        return Response(data)
