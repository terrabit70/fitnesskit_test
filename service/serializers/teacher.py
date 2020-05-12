from django.conf import settings
from rest_framework import serializers
from service.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    #imageUrl = serializers.SerializerMethodField()

 #   def get_imageUrl(self, instance):
 #       return f'http://{settings.TUNNEL_HOST}{settings.MEDIA_URL}{instance.image}'

    class Meta:
        model = Teacher
        fields = [
            'short_name',
            'name',
            'position',
 #           'imageUrl'
        ]
