from django.conf import settings
from rest_framework import serializers
from service.models import Teacher
import socket


class TeacherSerializer(serializers.ModelSerializer):
    imageUrl = serializers.SerializerMethodField()

    def get_imageUrl(self, instance):
        if not f'{instance.image}':
            return 'no image'
        else:
            return f'http://{socket.gethostbyname(socket.gethostname())}{settings.MEDIA_URL}{instance.image}'

    class Meta:
        model = Teacher
        fields = [
            'short_name',
            'name',
            'position',
            'imageUrl'
        ]
