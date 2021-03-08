from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r
from rest_framework import  permissions
from django.http import HttpResponse
from rest_framework.response import Response
from .models import CsvModel, CsvModelResouces


class CSVApi(APIView):

    permission_classes = [permissions.AllowAny]
    renderer_classes = (r.CSVRenderer, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    def get(self, request, format=None):
        csv_resource = CsvModelResouces()
        dataset = csv_resource.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="covid.csv"'
        return response