__author__ = 'karishma'

from .constants import MONTHS, SEASONS
from urllib.request import Request, urlopen
from .models import Country, Temperature


def data_entry(country_name, url, type):
    data = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # it's a file like object and works just like a file
    lines = urlopen(data).readlines()
    country, created = Country.objects.get_or_create(title=country_name)
    for line in lines[8:]:
        try:
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.JAN, type=type, defaults={'temperature': line.split()[1].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.FEB, type=type, defaults={'temperature': line.split()[2].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.MAR, type=type, defaults={'temperature': line.split()[3].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.APR, type=type, defaults={'temperature': line.split()[4].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.MAY, type=type, defaults={'temperature': line.split()[5].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.JUN, type=type, defaults={'temperature': line.split()[6].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.JUL, type=type, defaults={'temperature': line.split()[7].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.AUG, type=type, defaults={'temperature': line.split()[8].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.SEP, type=type, defaults={'temperature': line.split()[9].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.AUG, type=type, defaults={'temperature': line.split()[10].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.SEP, type=type, defaults={'temperature': line.split()[11].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.OCT, type=type, defaults={'temperature': line.split()[12].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.NOV, type=type, defaults={'temperature': line.split()[13].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), month=MONTHS.DEC, type=type, defaults={'temperature': line.split()[14].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), season=SEASONS.WIN, type=type, defaults={'temperature': line.split()[15].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), season=SEASONS.SPR, type=type, defaults={'temperature': line.split()[16].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), season=SEASONS.SUM, type=type, defaults={'temperature': line.split()[17].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), season=SEASONS.AUT, type=type, defaults={'temperature': line.split()[18].decode()})
            Temperature.objects.update_or_create(country=country, year=line.split()[0].decode(), season=SEASONS.ANN, type=type, defaults={'temperature': line.split()[19].decode()})
        except IndexError:
            pass

