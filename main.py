import json
import requests
from random import randint
key = '447c1dcc-434e-461b-84de-98802b2df128'
response = requests.get(f'https://api.thedogapi.com/v1/breeds')
data = json.loads(response.text)
rand_num = randint(0, len(data))

print(data[rand_num]['name'])
dog = data[rand_num]
list1 = []
for data in dog.items():
    str1 = f'{data[0]} : {data[1]}'.replace('}', '').replace("'", '')
    list1.append(str1)

print(list1)


