from django.conf import settings
from rest_framework import serializers

# Register serializer
from apps.base_user.models import MyUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = MyUser.objects.create(email=validated_data['email'], password=validated_data['password'])
        user.save()
        return user


# User serializer
class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


# User serializer
class UserProfileSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = MyUser
        fields = ('avatar', 'avatar_url', 'first_name', 'last_name', 'email', 'address', 'city',)

    def get_image_url(self, obj):
        img = obj.avatar.url
        if settings.DEBUG:
            request = self.context.get('request')
            img = request.build_absolute_uri(obj.avatar.url)
        return img


# Security
from rest_framework import serializers
from django.contrib.auth.models import User


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
