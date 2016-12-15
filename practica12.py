
from ubidots import ApiClient
import random
import time

api = ApiClient(token='jVYIpUpCxX12EVkSqDFAxWcAopdBf1')
my_variable = api.get_variable('5848c8d87625422d640ad3e2')
#new_value = my_variable.save_value({'value': 50})

dato = 100

while dato > 50:
    dato = random.randrange(48, 80)
    print(dato)
    new_value = my_variable.save_value({'value': dato})
    time.sleep(2)


