from rest_framework import serializers
from django.conf import settings
from core.models import Logo, Contact, SocialMedia, FAQ, About


class LogoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Logo
        fields = ('id', "image")

    def get_image_url(self, obj):
        img = obj.image.url
        if settings.DEBUG:
            request = self.context.get('request')
            img = request.build_absolute_uri(obj.image.url)
        return img


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', "phone", "email", "location")


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('id', "media", "url")


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'content')
