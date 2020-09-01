from django.urls import path
from shoppies.api.views import awards_api, award_api, awards_all_api

app_name = 'murder_in_color'
urlpatterns = [
    path(f'awards/', awards_api, name='awards'),
    path(f'awards/<str:pk>/', award_api, name='award'),
    path(f'allawards/', awards_all_api, name='allawards'),
]