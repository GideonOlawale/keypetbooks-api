from django.db import models
from import_export import resources


class CsvModel(models.Model):
	iso_code = models.CharField(max_length=50, blank=True, null=True)
	continent = models.CharField(max_length=50, blank=True, null=True)
	location = models.CharField(max_length=50, blank=True, null=True)
	date = models.DateField(blank=True, null=True)
	total_cases = models.IntegerField(blank=True, null=True)
	new_cases =  models.IntegerField(blank=True, null=True)
	total_deaths =  models.IntegerField(blank=True, null=True)
	new_deaths =  models.IntegerField(blank=True, null=True)
	new_deaths_smoothed =  models.IntegerField(blank=True, null=True)
	total_cases_per_million = models.FloatField(blank=True, null=True)
	new_cases_per_million = models.FloatField(blank=True, null=True)
	new_cases_smoothed_per_million = models.FloatField(blank=True, null=True)
	total_deaths_per_million = models.FloatField(blank=True, null=True)
	new_deaths_per_million = models.FloatField(blank=True, null=True)
	new_deaths_smoothed_per_million = models.FloatField(blank=True, null=True)
	new_cases_smoothed = models.FloatField(blank=True, null=True)

	def __str__(self):
		return self.continent


class CsvModelResouces(resources.ModelResource):
	
	class Meta:
		import_id_fields = ('iso_code',)
		model = CsvModel