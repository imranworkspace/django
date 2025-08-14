from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=25)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=25)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.email = validated_data.get('email')
        instance.password = validated_data.get('password')
        instance.save()
        return instance