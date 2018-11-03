from django.db import models
from django.utils import timezone


class TeachingAssistant(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class OfficeHour(models.Model):
    SUNDAY = 'SU'
    MONDAY = 'M'
    TUESDAY = 'T'
    WEDNESDAY = 'W'
    THURSDAY = 'TH'
    FRIDAY = 'F'
    SATURDAY = 'SA'
    DAYS = (
        (SUNDAY, 'Sunday'),
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday')
    )

    teaching_assistant = models.ForeignKey(TeachingAssistant, on_delete=models.PROTECT)
    room = models.CharField(max_length=10)
    start = models.TimeField()
    end = models.TimeField()
    day_of_the_week = models.CharField(max_length=2, choices=DAYS)

    def __str__(self):
        day = self.get_day_of_the_week_display()
        return f"{self.teaching_assistant.name}'s office hours for {day}"


class OfficeHourSession(models.Model):
    office_hour = models.ForeignKey(OfficeHour, on_delete=models.CASCADE)
    # We can't use autoaddnow because Celery refuses to use the right timezone
    # Instead we have to overrride save() and add it manually
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.office_hour.teaching_assistant.name}'s office hours held on {self.date}"

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.localtime(timezone.now())
        super().save(*args, **kwargs)

    @property
    def ongoing(self):
        now = timezone.localtime()
        return self.office_hour.start <= now < self.office_hour.end


class StudentQueue(models.Model):
    locked = models.BooleanField(default=False)
    office_hour_session = models.ForeignKey(OfficeHourSession, on_delete=models.CASCADE)

    @property
    def size(self):
        return self.student_set.filter(addressed=False).count()

    def __str__(self):
        return f"Queue of students for {str(self.office_hour_session)}"


class Student(models.Model):
    queue = models.ForeignKey(StudentQueue, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    addressed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
