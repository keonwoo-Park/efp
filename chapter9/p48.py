#usr/bin/env python

import sys
import urllib
import json

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def get_site_info(info):
    city = "%s, %s" %(info[0], info[1])
    appid = "455cefd1dc8a3f62d3892a4ec0b0cac3"
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (city, appid)
    
    f = urllib.urlopen(url)
    json_data = json.loads(f.read())
    return json_data 


if __name__ == "__main__":
    city = version_input("Where are you?(city, nation) ")
    info = city.split()
    
    json_data = get_site_info(info)
    main_info = json_data['main']

    print("%s weather: " %info[0])
    print("%d degrees Fahrenheit" % main_info['temp'])
