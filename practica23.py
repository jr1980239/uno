import requests
import json

url= "http://things.ubidots.com/api/v1.6/variables/5852054076254275dcc8ff5c/values"
parametros = {"format":"json","token":"jVYIpUpCxX12EVkSqDFAxWcAopdBf1"}
response = requests.get(url=url,params=parametros)

#print(response.text)

datos = json.loads(response.text)
#print(datos)
#print(response.text)

for resultado in datos["results"]:
    print("valor", resultado["value"])
    print("Creado en", resultado["created_at"])
    for k,v in resultado["context"].items():
        print(k,v)
    print("##############################")
