from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import  permissions
from .models import CsvModel, CsvModelResouces


class CSVApi(APIView):

    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        csv_data = CsvModelResouces()
        query_africa =  CsvModel.objects.filter(continent='Africa')
        africa_dataset = csv_data.export(query_africa)
        response = Response({
        	'africa':africa_dataset.csv
        	})
        return response