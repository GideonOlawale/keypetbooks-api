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
        query_asia=  CsvModel.objects.filter(continent='Asia')
        query_south =  CsvModel.objects.filter(continent='South America')
        query_europe =  CsvModel.objects.filter(continent='Europe')
        query_north =  CsvModel.objects.filter(continent='North America')
        query_oceania =  CsvModel.objects.filter(continent='Oceania')
        africa_dataset = csv_data.export(query_africa)
        asia_dataset = csv_data.export(query_asia)
        south_dataset = csv_data.export(query_south)
        europe_dataset = csv_data.export(query_europe)
        north_dataset = csv_data.export(query_north)
        oceania_dataset = csv_data.export(query_oceania)
        response = Response({
        	'africa':africa_dataset.json,
        	# 'oceania':oceania_dataset.json,
        	# 'north':north_dataset.json,
        	# 'asia':asia_dataset.json,
        	# 'europe' : europe_dataset.json,
        	# 'south': south_dataset.json
        	})
        return response