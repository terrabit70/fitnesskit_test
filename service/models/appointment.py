import uuid
from django.db import models
from .service import Service


class Appointment(models.Model):
    class WeekDays(models.IntegerChoices):
        MONDAY = 1, 'MONDAY'
        TUESDAY = 2, 'TUESDAY'
        WEDNESDAY = 3, 'WEDNESDAY'
        THURSDAY = 4, 'THURSDAY'
        FRIDAY = 5, 'FRIDAY'
        SATURDAY = 6, 'SATURDAY'
        SUNDAY = 7, 'SUNDAY'

    appointment_id = models.UUIDField(blank=False, null=False, primary_key=True, default=uuid.uuid4)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    weekday = models.IntegerField(blank=False, null=False, choices=WeekDays.choices, default=WeekDays.MONDAY)
    pay = models.BooleanField(blank=False, null=False, default=False)
    appointment = models.BooleanField(blank=False, null=False, default=False)
    color = models.CharField(blank=False, null=False, max_length=7)
    availability = models.IntegerField(blank=False, null=False, default=-1)

    place = models.ForeignKey('Place', on_delete=models.SET_NULL,  blank=False, null=True)
    service = models.ForeignKey('Service', on_delete=models.SET_NULL,  blank=False, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL,  blank=False, null=True)

    def __str__(self):
        return f'{Service.name} : {self.weekday.choices}'
