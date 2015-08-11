from django.shortcuts import render
# Create your views here.

from .models import Jobseeker
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def jobseeker_list(request):
    u = get_object_or_404(Jobseeker)
    marks = Jobseeker.objects.all()
    json = serializers.serialize("json", marks)
    return HttpResponse(json, mimetype="application/json")

