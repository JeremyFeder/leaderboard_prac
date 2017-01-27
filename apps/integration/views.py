from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib import messages
import random


# Create your views here.
def index(request):
    return render(request, 'integration/index.html')
