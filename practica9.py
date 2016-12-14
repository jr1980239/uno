from ubidots import ApiClient

api = ApiClient(token='jVYIpUpCxX12EVkSqDFAxWcAopdBf1')
my_variable = api.get_variable('5848c8d87625422d640ad3e2')
new_value = my_variable.save_value({'value': 30})
