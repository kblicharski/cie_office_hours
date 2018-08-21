from django.shortcuts import render
from django.utils import timezone

from .models import OfficeHourSession


# Create your views here.
def index(request):
    todays_sessions = OfficeHourSession.objects.filter(date=timezone.localdate())

    ongoing = False
    for session in todays_sessions:
        if session.ongoing:
            ongoing = True

    context = {
        'ongoing_office_hours': ongoing
    }

    return render(request, 'index.html', context=context)
