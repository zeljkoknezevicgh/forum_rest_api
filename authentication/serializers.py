from rest_framework import serializers
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ("username", "password", "email")
        extra_kwargs = {
            "password": {"write_only": True},
            
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


    

   