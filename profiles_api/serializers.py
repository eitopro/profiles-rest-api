from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name input field for testing posting to the APIView"""
    name = serializers.CharField(max_length=10)