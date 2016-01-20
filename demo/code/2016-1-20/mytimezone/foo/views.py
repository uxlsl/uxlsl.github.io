import pytz
from django.shortcuts import redirect, render
from django.utils import timezone


class TimezoneMiddleware(object):

    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/set_timezone')
    else:
        return render(request, 'template.html',
                      {'timezones': pytz.common_timezones,
                       'value': timezone.now(),
                       })
