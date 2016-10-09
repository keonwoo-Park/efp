#usr/bin/env python

import sys
import urllib
import json

def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def get_site_info():
    f = urllib.urlopen("http://api.open-notify.org/astros.json")
    json_data = json.loads(f.read())
    return json_data 


def extraction_data(json_data):
    message = json_data['message']
    number = int(json_data['number'])
    peoples_info = json_data['people']
    return number, peoples_info 


def max_len(result):
    str_len = {"name":0, "craft":0}
    for info in result[1]:
        if str_len.get("name") < len(info['name']):
            str_len["name"] = len(info['name'])
        if str_len.get("craft") < len(info['craft']):
            str_len["craft"] = len(info['craft'])
    return str_len


def result_print(result):
    str_len = max_len(result)
    bar = '-'
    space = ' '
    print("There are %d people in space rigth now:" % result[0])
    print("Name %s|Craft" % (space*str_len['name']))
    print("%s" % (bar*(str_len['name'] + str_len['craft'] + 9)))

    for people in result[1]:
        if len(people['name']) <= str_len['name']:
            gap = str_len.get('name') - len(people['name']) + 5
            message = (people['name'] + gap*space) 
        print("%s|%s" % (message, people['craft']))


if __name__ == "__main__":
    json_data = get_site_info()
    result = extraction_data(json_data)
    result_print(result)

