from django.db import models


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
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.office_hour.teaching_assistant.name}'s office hours held on {self.date}"


class StudentQueue(models.Model):
    locked = models.BooleanField(default=False)
    office_hour_session = models.ForeignKey(OfficeHourSession, on_delete=models.CASCADE)

    def __str__(self):
        return f"Queue of students for {str(self.office_hour_session)}"


class Student(models.Model):
    queue = models.ForeignKey(StudentQueue, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    addressed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
