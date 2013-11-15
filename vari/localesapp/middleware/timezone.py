# -*- encoding: utf-8 -*-
from django.utils import timezone
from django.http import HttpRequest

class TimezoneMiddleware(object):
    
    def process_request(self, request):
        tz = request.session.get('django_timezone')
        if tz is not None:
            timezone.activate(tz)

    def process_response(self, request, response):
        timezone.deactivate()
        return response