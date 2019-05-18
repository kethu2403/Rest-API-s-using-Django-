from rest_framework import serializers

class HelloSerialzer(serializers.Serializer):
    """Serailizes a name filed for testing an APIView"""

    name = serializers.CharField(max_length=10)
        
