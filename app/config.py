from datetime import datetime

base_url = 'https://petstore.swagger.io/v2'

def print_response(response):
  """Prints the REST API response no matter it's json or text type"""
  print('Status code: ', response.status_code)
  print('Response:')
  if 'application/json' in response.headers['Content-Type']:
    print(response.json())
  else:
    print(response.text)


# PET Data for actions with pets
# info for a new pet to use in: POST /pet Add a new pet to the store
new_pet = {
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

# *jpg Image file name to use in: POST /pet/{pet_id}/uploadImage Uploads an image
image_file_name = 'Grusha.jpg'

# info to update a pet to use in: PUT /pet Update an existing pet
update_pet = {
  "id": 0,
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
  "status": "pending"
}

# pet's characteristics to update to use in: POST /pet/{pet_id} Updates a pet in the store with form data
upd_characteristics = {
  'name': 'Clair',
  'status': 'available'
}

# STORE  Access to Petstore orders
# New order detail to use in: POST /store/order Place an order for a pet
new_order = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"), # Make data and time format meet the swagger documentation
  "status": "placed",
  "complete": True
}

# USER  Operations about user

N = 2 # Number of Users to create using POST /user/createWithArray
M = 3 # Number of Users to create using POST /user/createWithList