from rest_framework import serializers
from . import models


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'role', 'created_at', 'updated_at',)
        model = models.Member

