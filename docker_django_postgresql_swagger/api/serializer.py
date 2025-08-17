from rest_framework import serializers
from .models import AuthorModel,PostModel

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=AuthorModel
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostModel
        fields='__all__'
    
    def update(self, instance, validated_data):
       #instance.author=validated_data.get('author')
       instance.post_title=validated_data.get('post_title')
       instance.post_description=validated_data.get('post_description')
       instance.save()
       return instance