""" The task is to make each of the REST-requests from https://petstore.swagger.io/ and print responses"""

import requests
import json
from datetime import datetime


base_url = 'https://petstore.swagger.io/v2'

def print_response(response: requests.models.Response):
    """Prints the REST API response no matter it's json or text type"""
    print('Status code: ', response.status_code)
    print('Response:')
    if 'application/json' in response.headers['Content-Type']:
        print(response.json())
    else:
        print(response.text)


# PET  Everything about your Pets
THE_PET_API_SCENARIO = (
    "\nI. PET. \nHere are main REST API requests covering actions with pets on the Petstore according to https://petstore.swagger.io/",
    "POST /pet - Add a new pet and save it's pet_id",
    "POST /pet/{pet_id}/uploadImage - Add a pet's image",
    "PUT /pet - Update existing pet's info",
    "POST /pet/{pet_id} - Update existing pet's info",
    "GET /pet/{pet_id} - Check created pet finding it by pet_id",
    "DELETE pet/{pet_id} - Delete the pet",
    "GET /pet/findByStatus - Find all pets with a status 'available', print first 5 of them, check there's no pet with pet_id"
    )

j = 0
print(THE_PET_API_SCENARIO[j])


# POST /pet Add a new pet to the store
j += 1
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}')

body = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "bird"
  },
  "name": "Polly",
  "photoUrls": [
    "noPhoto"
  ],
  "tags": [
    {
      "id": 0,
      "name": "parrot"
    }
  ],
  "status": "available"
}

res = requests.post(f'{base_url}/pet',
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(body))
print_response(res)
PET_id = res.json()['id']


# POST /pet/{pet_id}/uploadImage Uploads an image
j += 1
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}')

picture = open('Grusha.jpg', 'rb')

res = requests.post(f'{base_url}/pet/{PET_id}/uploadImage',
                    headers={'accept': 'application/json'},
                    files={'file': picture, 'type': 'image/jpeg'})

print_response(res)


# PUT /pet Update an existing pet
j += 1
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}')
body = {
  "id": PET_id,
  "category": {
    "id": 0,
    "name": "cat"
  },
  "name": "Kitty",
  "photoUrls": [
    "noPhoto"
  ],
  "tags": [
    {
      "id": 0,
      "name": "boldcat"
    }
  ],
  "status": "available"
}

res = requests.put(f'{base_url}/pet',
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(body))
print_response(res)


# POST /pet/{pet_id} Updates a pet in the store with form data
j += 1
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}')

name_upd = 'Sara'
status_upd = 'available'
formdata = f'name={name_upd}&status={status_upd}' # That's a form specified in swagger documentation

res = requests.post(f'{base_url}/pet/{PET_id}',
                    headers={'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'},
                    data=formdata)
print_response(res)

# GET /pet/{pet_id} Find pet by ID
j += 1
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}')

res = requests.get(f'{base_url}/pet/{PET_id}',
                   headers={'accept': 'application/json', 'Content-Type': 'multipart/form-data'})
print_response(res)


# DELETE /pet/{pet_id} Deletes a pet
j += 1
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}') # Delete the pet with DELETE pet/{pet_id} request

res_del = requests.delete(f'{base_url}/pet/{PET_id}',
                          headers={'accept': 'application/json', 'api_key': 'special-key'})
print_response(res_del)


# GET /pet/findByStatus Finds all the pets with certain status among: 'available', 'pending', 'sold'
j += 1
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}')

res = requests.get(f'{base_url}/pet/findByStatus',
                   params={'status': 'available'},
                   headers={'accept': 'application/json'})

if len(res.json()) < 5:
    print_response(res)
else:
    print('Code: ', res.status_code)
    for i in range(5):
        print(res.json()[i])

for i in range(len(res.json())):
    if res.json()[i]['id'] == PET_id:
        print('The {0} item is:\n {1}'.format(i, res.json()[i]))
        break
    elif i == len(res.json()) - 1:
        print(f'No item was found with the ID {PET_id}')


########################################################################################################################

# STORE  Access to Petstore orders
THE_STORE_API_SCENARIO = (
    "\n\nII. STORE. \nHere are main REST API requests related to access to the Petstore orders according to https://petstore.swagger.io/",
    "POST /store/order - Place a new order, save its ID",
    "GET /store/order/{orderId} - Find the order just created",
    "DELETE /store/order/{orderId} - Delete the order by ID",
    "GET /store/inventory - Check pet inventories by status"
    )

j = 0
print(THE_STORE_API_SCENARIO[j])


# POST /store/order Place an order for a pet
j += 1
print(f'\n{j}). {THE_STORE_API_SCENARIO[j]}')

body = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"), # Make data and time format meet the swagger documentation
  "status": "placed",
  "complete": True
}

res = requests.post(f'{base_url}/store/order',
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(body))
print_response(res)
order_id = res.json()['id']


# GET /store/order/{orderId} Find purchase order by ID
j += 1
print(f'\n{j}). {THE_STORE_API_SCENARIO[j]}')

res = requests.get(f'{base_url}/store/order/{order_id}', headers={'accept': 'application/json'})
print_response(res)


#DELETE /store/order/{orderId} - Delete purchase order by ID
j += 1
print(f'\n{j}). {THE_STORE_API_SCENARIO[j]}')

res = requests.delete(f'{base_url}/store/order/{order_id}', headers={'accept': 'application/json'})
print_response(res)


# GET /store/inventory - Returns pet inventories by status
j += 1
print(f'\n{j}). {THE_STORE_API_SCENARIO[j]}')

res = requests.get(f'{base_url}/store/inventory', headers={'accept': 'application/json', 'api_key': 'special-key'})
print_response(res)