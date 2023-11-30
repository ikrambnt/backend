from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Group

def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    return render(request, 'group_detail.html', {'group': group})

