from django.urls import path
from slack.views import slack

urlpatterns = [
    path('', view=slack, name='slack')
]