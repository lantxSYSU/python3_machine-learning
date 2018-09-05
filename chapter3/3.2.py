#如何实现可迭代对象和迭代器对象
#coding:utf8
import requests

def getWeather(city):
    r = requests.get(u'http://wthrcdn.etouch.cn/weather_min?city=' + city)
    data = r.json()['data']['forecast'][0]
    return '%s: %s, %s' % (city, data['low'], data['high'])

print(getWeather(u'北京'))
