from urllib.request import urlopen
from bs4 import BeautifulSoup
from geoip2 import database

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
    URL = 'http://cybercrime-tracker.net/index.php?s=0&m=10000'
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
    result = []
    reader = database.Reader("/home/lap/Рабочий стол/GeoLite2-City.mmdb")
    for uno_ip in ip_lst:
        try:
            geo_ip = reader.city(uno_ip)
            if geo_ip.country.name == "Ukraine":
                result.append(uno_ip)
        except:
            pass

    return result


def compare_zeus(geo, parse):
    result = {}
    for line in parse:
        for uno_geo in geo:
            if uno_geo in line[3]:
                line_red =  line[0], line[8], line[1]
                result.update({line[3] :line_red})

    return result


def compare_cycrime(geo, parse):
    result = {}
    for line in parse:
        for uno_geo in geo:
            if uno_geo in line[2]:
                line_red = line[0],'',line[3]
                result.update({line[2]:line_red})
    return (result)



if __name__=="__main__":
    x = {}
    x.update(compare_cycrime(geo_id(cycrime_ip), cycrime_lst()))
    x.update(compare_zeus(geo_id(zeus_ip), zeus_lst()))
    print(x.keys())