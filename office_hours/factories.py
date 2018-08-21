import factory
from django.utils import timezone

from .models import OfficeHour, TeachingAssistant


class TeachingAssistantFactory(factory.DjangoModelFactory):
    class Meta:
        model = TeachingAssistant

    name = 'test'
    email = 'test@example.com'


class OfficeHourFactory(factory.DjangoModelFactory):
    class Meta:
        model = OfficeHour
        exclude = ('now',)

    now = timezone.localtime(timezone.now())
    teaching_assistant = factory.SubFactory(TeachingAssistantFactory)
    room = 'test'
    start = now.time()
    end = (now + timezone.timedelta(hours=1)).time()
    day_of_the_week = OfficeHour.MONDAY
