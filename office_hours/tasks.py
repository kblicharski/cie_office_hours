from django.utils import timezone

from cie_office_hours.celery import app
from .models import OfficeHour, OfficeHourSession, StudentQueue


@app.task
def create_daily_office_hour_sessions():
    office_hours = OfficeHour.objects.filter(teaching_assistant__active=True)
    for time in office_hours:
        now = timezone.localtime(timezone.now())
        does_not_exist = OfficeHourSession.objects.filter(date=now).exists()
        current_day_of_the_week = now.strftime('%A')
        if time.get_day_of_the_week_display() == current_day_of_the_week:
            session = OfficeHourSession.objects.create(office_hour=time)
            queue = StudentQueue.objects.create(office_hour_session=session)
            print(f'Created new session {session}')
