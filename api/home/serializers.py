from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

class User1Serializer(serializers.ModelSerializer):

    class Meta:
        model = User1
        # exclude = ['id', 'password']
        fields = '__all__'
    
    def validate(self, data):
        if 'name' in data:
            for i in data['name']:
                if not i.isalpha() and not ' ':
                    raise serializers.ValidationError({
                        'error': 'Enter Valid Name'
                        })
        
        return data