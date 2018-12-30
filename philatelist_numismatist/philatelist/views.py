from django.shortcuts import render, get_object_or_404
from .models import StampsGroup, Stamp

def index(request):
    all_stamp_groups = StampsGroup.objects.all()
    return render(request, 'philatelist/index.html', {'all_stamp_groups': all_stamp_groups})

def detail(request, stamps_group_id):
    all_stamp_groups = get_object_or_404(StampsGroup, pk=stamps_group_id)
    return render(request, 'philatelist/detail.html', {'all_stamp_groups': all_stamp_groups})
