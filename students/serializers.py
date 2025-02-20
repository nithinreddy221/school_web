from rest_framework import serializers  # Import DRF's serializers
from .models import Student  # Import the Student model

class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Student model.
    This converts model instances into JSON format and vice versa.
    """
    class Meta:
        model = Student  # Specify the model to serialize
        fields = '__all__'  # Serialize all fields from the Student model
