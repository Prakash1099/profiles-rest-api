from rest_framework import serializers
from .models import UserProfile

class HelloSerializer(serializers.Serializer):
    """Serialize a name field for test out APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializez a user profile object"""

    class Meta:
        """To point to a specific model in our project"""

        model = UserProfile

        fields=('id', 'email', 'name', 'password') #must be a tuple
        extra_kwargs = {
            'password': {
                'write_only': True, # To onelly use when create / Update
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],

        )

        return user

    def update(self, instance, validated_data):
        """Update an existing user"""


        """
        While Updating a password DRF default update function will update the password as plain string.
        So to save the password as hasded value we are overriding teh existing update funciton 
        """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)  ## To pass the values to existing DRF update function

