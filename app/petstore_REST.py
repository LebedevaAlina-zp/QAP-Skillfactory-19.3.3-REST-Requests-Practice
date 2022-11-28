""" The task is to make each of the REST-requests from https://petstore.swagger.io/ and print responses"""

import requests
import json

base_url = 'https://petstore.swagger.io/v2'

def print_response(response: requests.models.Response):
    """Prints REST API responses of json or text type"""
    print('Status code: ', response.status_code)
    print('Response:')
    if 'application/json' in response.headers['Content-Type']:
        print(response.json())
    else:
        print(response.text)


# PET  Everything about your Pets
THE_PET_API_SCENARIO = (
    "Here's a scenario with REST API requests concerning actions with pets on the Petstore",
    "Add a new pet with a POST /pet request, and save it's pet_id",
    "Add a pet's image with POST /pet/{pet_id}/uploadImage",
    "Update existing pet's info with PUT /pet request",
    "Update existing pet's info with POST /pet/{pet_id} request",
    "Check created pet with a GET /pet/{pet_id} request",
    "Delete the pet with DELETE pet/{pet_id} request",
    "Find all pets with status 'available', print first 5 of them, check there's no pet with pet_id"
    )

j = 0 # The scenario list index, we'll add it by 1 when going to the next request
print(THE_PET_API_SCENARIO[j])


# POST /pet Add a new pet to the store
j += 1
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}') # Add a new pet with a POST /pet request, and save it's pet_id

body = {
  "id": 0, # new id number will be assigned automatically
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
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}') # Add a pet's image with POST /pet/{pet_id}/uploadImage

picture = open('Grusha.jpg', 'rb')

res = requests.post(f'{base_url}/pet/{PET_id}/uploadImage',
                    headers={'accept': 'application/json'},
                    files={'file': picture, 'type': 'image/jpeg'})

print_response(res)


# PUT /pet Update an existing pet
j += 1
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}') # Update pet's with pet_id info with PUT /pet request

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
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}') # Update existing pet's info with POST /pet/{pet_id} request

name_upd = 'Sara'
status_upd = 'available'
formdata = f'name={name_upd}&status={status_upd}' # That's a form specified in swagger documentation

res = requests.post(f'{base_url}/pet/{PET_id}',
                    headers={'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'},
                    data=formdata)
print_response(res)

# GET /pet/{pet_id} Find pet by ID
j += 1
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}') # Check created pet with a GET /pet/{pet_id} request

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
print(f'\n{j}). {THE_PET_API_SCENARIO[j]}') # Find all pets with status 'available', print first 5 of them

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

