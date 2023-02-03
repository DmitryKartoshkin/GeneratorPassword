from rest_framework.serializers import ModelSerializer

from generator.models import Passwords


class PasswordsSerializer(ModelSerializer):
    class Meta:
        model = Passwords
        fields = ['id', 'service', 'password_for_the_service', 'created_at', 'updated_at', 'user']