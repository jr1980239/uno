import threading
import requests
import time
def obtener_sismos():
    response = requests.get(
        'http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-16&endtime=2016-06-05')
    data = response.text
   # api = ApiClient(token='jVYIpUpCxX12EVkSqDFAxWcAopdBf1')
    #my_variable = api.get_variable('5852054076254275dcc8ff5c')
    ## new_value = my_variable.save_value({'value': 50})

    eventos = data.split("\n")
    for indice in range(len(eventos)):
        if indice > 0:
            evento = eventos[indice]
            datos = evento.split("|")
            if len(datos) == 13 and datos[12].lower().find("ecuador"):
                if datos[10] is not "":
                    magnitud = float(datos[10])
                    print({'value': magnitud})
                    #new_value = my_variable.save_value({'value': magnitud})
                    time.sleep(0.5)

#obtener_sismos()
t = threading.Thread(target=obtener_sismos)
t.start()
print("test")
i = 0
while True:
    print(i)
    i+=1
    time.sleep(0.5)
