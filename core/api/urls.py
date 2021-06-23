from django.urls import path

from core.api.views import FAQView, AboutView

urlpatterns = [
    path('get_about/', AboutView.as_view(), name='get-about'),
    path('get_faq/', FAQView.as_view(), name='get-faq'),
]
