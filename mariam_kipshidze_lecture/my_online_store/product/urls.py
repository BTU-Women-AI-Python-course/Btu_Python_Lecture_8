from django.urls import path, register_converter

from product.views import current_datetime, my_personal_data, FourDigitYearConverter

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [
    path('current_datetime/', current_datetime, name='current_datetime'),
    path('my_personal_data/<yyyy:birth_date>/', my_personal_data, name='my_personal_data'),
]
