from urllib.request import urlopen

# sample = open('/home/user/Desktop/db for parsing/ripe.db.route')
# one = sample.readlines()
# print(one)




def geo_id(ip_lst):
    result = {}
    for uno_ip in ip_lst:
        reader = "http://ip-api.com/json/"+uno_ip
        data = urlopen(reader)
        print(data)
        result.update({uno_ip: reader})
    return result

