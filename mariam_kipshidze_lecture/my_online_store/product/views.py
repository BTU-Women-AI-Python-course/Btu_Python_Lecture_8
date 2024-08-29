from django.http import HttpResponse, JsonResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html, status=200)


def my_personal_data(request, birth_date: int):
    name = 'Mariami'
    last_name = "Kipshidze"
    birth_date = int(birth_date)
    return JsonResponse(
        {
            "birth_date": birth_date
        },
        status=200
    )


class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value
