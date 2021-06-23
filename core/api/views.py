from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.serializers import ContactSerializer, LogoSerializer, SocialMediaSerializer, FAQSerializer, \
    AboutSerializer
from core.models import Contact, Logo, SocialMedia, FAQ, About


class AboutView(APIView):
    def get(self, request):
        return Response(AboutSerializer(About.objects.last()).data)


class FAQView(APIView):
    def get(self, request):
        return Response(FAQSerializer(FAQ.objects.all(), many=True).data)
