from django.shortcuts import render
from django.http import HttpResponse
from .models import Country, Temperature
from .forms import DataForm
from .utils import data_entry
from . import fusioncharts

# Create your views here.


def create_reports(request):
    form = DataForm()
    base_url = request.META['HTTP_HOST']
    country_list = Country.objects.values_list('title', flat=True)
    year_list = Temperature.objects.values_list('year', flat=True).distinct().order_by('-year')
    create_data_url = str(base_url) + '/save-data'
    return render(request, 'w_reports/weather_reports.html', {'country_list': country_list, 'year_list': year_list,
                                                              'create_data_url': create_data_url, 'DataForm': form})


def create_data(request):
    """ Scrap data from url and store in database """
    country = request.POST.get('country')
    data_url = request.POST.get('data_url')
    data_type = request.POST.get('data_type')
    data_entry(country, data_url, data_type)
    return HttpResponse({"success": True})



# Include the `fusioncharts.py` file that contains functions to embed the charts.
# The `chart` function is defined to generate Column 2D chart from database.
def view_chart(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    data = []
    column2D = {}
    form = DataForm(data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            country = form.cleaned_data['country']
            year = form.cleaned_data['year']
            type = form.cleaned_data['type']
            t_data = Temperature.objects.filter(country__title=country, year=year, type=type)
            dataSource = {}
            dataSource['chart'] = {
                "caption": "Monthly " + type + " In " + country+ " For Year " + str(year),
                "subCaption": "",
                "xAxisName": "Season-Month",
                "yAxisName": "Temperature",
                "numberPrefix": "",
                "theme": "zune"
            }

            # The data for the chart should be in an array where each element of the array is a JSON object
            # having the `label` and `value` as key value pair.

            dataSource['data'] = []
            # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
            for key in t_data:
                data={}
                data['label'] = key.month if key.month else key.season
                data['value'] = key.temperature
                dataSource['data'].append(data)
            # Create an object for the Column 2D chart using the FusionCharts class constructor
            column2D = fusioncharts.FusionCharts("column2D", "ex1", "600", "350", "chart-1", "json", dataSource)
        if data:
            return render(request, 'w_reports/statastic.html', {'DataForm': form, 'output': column2D.render()})
        else:
            return render(request, 'w_reports/statastic.html', {'DataForm': form, 'error_desc': 'Data Not Found! Try Other Filter'})
    else:
        return render(request, 'w_reports/statastic.html', {'DataForm': DataForm})


