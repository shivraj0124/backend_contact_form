from django.urls import path
from .views import send_contact_email

urlpatterns = [
    path('send-email/', send_contact_email, name='send_contact_email'),
]
