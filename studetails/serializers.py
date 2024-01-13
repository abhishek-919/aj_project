from rest_framework import serializers
from .models import studentsdetails


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = studentsdetails
        fields = '__all__'
