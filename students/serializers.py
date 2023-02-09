from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Student
        fields = [
            'full_name',
            'age',
            'student_id'
        ]

    def get_full_name(self, obj):
        return obj.get_full_name()