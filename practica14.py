import requests

response = requests.get('http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-16&endtime=2016-04-20')
data = response.text
print (data)