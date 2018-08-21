from django.contrib import admin

from .models import OfficeHour, OfficeHourSession, Student, StudentQueue, TeachingAssistant

# Register your models here.
admin.site.register(OfficeHour)
admin.site.register(OfficeHourSession)
admin.site.register(StudentQueue)
admin.site.register(Student)
admin.site.register(TeachingAssistant)
