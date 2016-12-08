from ubidots import ApiClient

api = ApiClient(token='e869813949f9a15587ce43e6ec75fd5887695e45')
my_variable = api.get_variable('5848c8d87625422d640ad3e2')
new_value = my_variable.save_value({'value': 10})
