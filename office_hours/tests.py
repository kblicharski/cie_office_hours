import freezegun
import pytest
from django.utils import timezone

from .factories import OfficeHourFactory
from .models import OfficeHour, OfficeHourSession
from .tasks import create_daily_office_hour_sessions


@pytest.mark.django_db
def test_create_daily_office_hour_sessions():
    # Freeze on a Tuesday
    with freezegun.freeze_time('2018-08-21 00:00:00-05:00'):
        OfficeHourFactory(day_of_the_week=OfficeHour.TUESDAY)
        OfficeHourFactory(day_of_the_week=OfficeHour.WEDNESDAY)
        OfficeHourFactory(day_of_the_week=OfficeHour.THURSDAY)
        create_daily_office_hour_sessions()
        assert OfficeHourSession.objects.exists()

        # Go to Thursday
        with freezegun.freeze_time(timezone.localtime(timezone.now()) + timezone.timedelta(days=2)):
            create_daily_office_hour_sessions()
            assert OfficeHourSession.objects.count() == 2
