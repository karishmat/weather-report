__author__ = 'karishma'
from django import forms
from .models import Country, Temperature

COUNTRIES = [(country, country) for country in Country.objects.values_list('title', flat=True)]
YEARS = [(year, year) for year in Temperature.objects.values_list('year', flat=True).distinct().order_by('-year')]
TYPES = [(type, type) for type in Temperature.objects.values_list('type', flat=True).distinct().order_by('-type')]


class DataForm(forms.Form):
    country = forms.ChoiceField(choices=COUNTRIES)
    year = forms.ChoiceField(choices=YEARS)
    type = forms.ChoiceField(choices=TYPES)

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        # Need to initialize so that we get the updated data in form
        self.fields['country'].choices = [(country, country) for country in Country.objects.values_list('title', flat=True)]
        self.fields['year'].choices = [(year, year) for year in Temperature.objects.values_list('year', flat=True).distinct().order_by('-year')]
        self.fields['type'].choices = [(type, type) for type in Temperature.objects.values_list('type', flat=True).distinct().order_by('-type')]
