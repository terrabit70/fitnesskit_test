from rest_framework import serializers
from service.models import Appointment
from service.serializers.teacher import TeacherSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='service.name')
    description = serializers.CharField(source='service.description')
    place = serializers.CharField(source='place.name')
    teacher = serializers.CharField(source='teacher.name')
    startTime = serializers.TimeField(format='%H.%M', source='start_time')
    endTime = serializers.TimeField(format='%H.%M', source='end_time')
    weekDay = serializers.IntegerField(source='weekday')
    service_id = serializers.CharField(source='service.service_id')
    teacher_v2 = TeacherSerializer(source='teacher')

    class Meta:
        model = Appointment  #TODO wtf
        fields = [
            'name',
            'description',
            'place',
            'teacher',
            'startTime',
            'endTime',
            'weekDay',
            'appointment_id',
            'service_id',
            'pay',
            'appointment',
            'teacher_v2',
            'color',
            'availability'
        ]
