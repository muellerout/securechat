from django.contrib import admin
from slack.models import Regex, DataLeak

admin.site.register(Regex)
admin.site.register(DataLeak)