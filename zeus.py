import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from geoip2 import database
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parser_resourse.settings")
django.setup()

from ip_parse.models import CompromizedIP


def zeus_lst():
    URL = 'https://zeustracker.abuse.ch/monitor.php?filter=all'
    row_lst = []
    f = urlopen(URL)
    soup = BeautifulSoup(f, 'lxml')
    tables = soup.find_all("table")
    prop_table= tables[1]
    table_rows = prop_table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        row_lst.append(row)
    return row_lst


def cycrime_lst():
    URL = 'http://cybercrime-tracker.net/index.php?s=0&m=1'
    row_lst = []
    f = urlopen(URL)
    soup = BeautifulSoup(f, 'lxml')
    tables = soup.find("tbody")
    table_rows = tables.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        row_lst.append(row)
    return row_lst

zeus_ip = [x[3] for x in zeus_lst()]
cycrime_ip = [x[2] for x in cycrime_lst()]


def geo_id(ip_lst):
    result ={}
    reader = database.Reader("/home/user/Desktop/db for parsing/GEodata/GeoLite2-City.mmdb")
    for uno_ip in ip_lst:
        try:
            geo_ip = reader.city(uno_ip)
            long = geo_ip.location.longitude
            lat = geo_ip.location.latitude
            if geo_ip.country.name == "Ukraine":
                result.update({uno_ip: ({'geom': {'type': 'Point', 'coordinates': [long, lat]}})})

        except:
            pass
    # повертає словник {'91.236.213.74': (37.7759, 47.9917), '193.201.227.142': (30.5233, 50.45)}
    return result


def compare(dict, list):
    for line in list:
        for key in dict.keys():
            if key in line[3]:
                dict[key].update({'date': line[0], 'ip': line[3], 'subnet':line[8], 'malware': line[1]})
            elif key in line[2]:
                dict[key].update({'date': line[0], 'ip': line[2], 'subnet':" ", 'malware': line[3]})
    return dict


"""  вписать значения словарь в словаре для полученной информации по парсингу ---
d = {'46.28.65.62': ('22-02-2015', '', 'Keitaro'), '176.107.193.191': ('12-02-2014', '', 'Citadel')}
d['46.28.65.62']
('22-02-2015', '', 'Keitaro')
d = {'46.28.65.62': { 'data' : '22-02-2015',  'virus' :'Keitaro'}}
d['46.28.65.62'].get('data')
'22-02-2015'
"""

def djangoDBbridge(parseddict):
        for key in parseddict.keys():
            db,status = CompromizedIP.objects.get_or_create(title=' || '.join([parseddict[key].get('date'), key]),
                                                             appear_date=parseddict[key].get('date'),
                                                             ip_adress=parseddict[key].get('ip'),
                                                             as_number=parseddict[key].get('subnet'),
                                                             malware_type=parseddict[key].get('malware'),
                                                             geom=parseddict[key].get('geom'))
            if status == True:
                db.appear_data = parseddict[key].get('date')
                db.save()
                print(db)


if __name__=="__main__":
    x ={}
    x.update(compare(geo_id(cycrime_ip), cycrime_lst()))
    x.update(compare(geo_id(zeus_ip), zeus_lst()))
    print(x)
    djangoDBbridge(x)