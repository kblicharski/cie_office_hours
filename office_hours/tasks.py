from django.utils import timezone

from cie_office_hours.celery import app
from .models import OfficeHour, OfficeHourSession, StudentQueue


@app.task
def create_daily_office_hour_sessions():
    office_hours = OfficeHour.objects.filter(teaching_assistant__active=True)
    for time in office_hours:
        now = timezone.localtime(timezone.now())
        exists = False
        for session in OfficeHourSession.objects.all():
                exists = True
        current_day_of_the_week = now.strftime('%A')
        if not exists and time.get_day_of_the_week_display() == current_day_of_the_week:
            session = OfficeHourSession.objects.create(office_hour=time)
            StudentQueue.objects.create(office_hour_session=session)
            print(f'Created new session {session}')
