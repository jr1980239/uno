from ubidots import ApiClient
import requests
import time

api = ApiClient(token='jVYIpUpCxX12EVkSqDFAxWcAopdBf1')
my_variable = api.get_variable('5852054076254275dcc8ff5c')
#new_value = my_variable.save_value({'value': 50})

response = requests.get('http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-16&endtime=2016-04-20')
data = response.text
#print (data)

eventos = data.split("\n")
for indice in range(len(eventos)):
    if indice > 0:
        evento = eventos[indice]
        datos = evento.split("|")
        if len(datos) == 13 and  datos[12].lower().find("ecuador"):
            if datos[10] is not "":
                magnitud = float(datos[10])
                new_value = my_variable.save_value({'value': magnitud})
                time.sleep(2)
