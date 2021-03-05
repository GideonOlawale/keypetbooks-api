from django.urls import path
from .views import CSVApi

urlpatterns = [
	path('covid/csv', CSVApi.as_view())
]