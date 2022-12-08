""" The task is to make each of the REST-requests from https://petstore.swagger.io/ and print responses"""

import requests
import json
import random_profile
import random
from config import base_url, print_response, N, M
import config


# PET  Everything about your Pets
print("\nI. PET. \nHere are main REST API requests covering actions with pets on the Petstore according to https://petstore.swagger.io/")

# POST /pet Add a new pet to the store
j = 1 # This is a counter just to numerize the requests when printing
print(f"\n{j}).", "POST /pet - Add a new pet and save it's pet_id")

body = config.new_pet
print(f"New pet's info: {body}")

res = requests.post(f'{base_url}/pet',
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(body))
print_response(res)

pet_id = res.json()['id']
print(f"Saved pet_id = {pet_id}")


# POST /pet/{pet_id}/uploadImage Uploads an image
j += 1
print(f"\n{j}).", "POST /pet/{pet_id}/uploadImage - Add a pet's image")
print(f"Upload an image file {config.image_file_name}")

picture = open(config.image_file_name, 'rb') # Open an image file

res = requests.post(f'{base_url}/pet/{pet_id}/uploadImage',
                    headers={'accept': 'application/json'},
                    files={'file': picture, 'type': 'image/jpeg'})
print_response(res)


# PUT /pet Update an existing pet
j += 1
print(f"\n{j}).", "PUT /pet - Update existing pet's info")

body = config.update_pet
body["id"] = pet_id # Put the right id into pet's info to update
print(f"New pet's info for update: {body}")

res = requests.put(f'{base_url}/pet',
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(body))
print_response(res)


# POST /pet/{pet_id} Updates a pet in the store with form data
j += 1
print(f"\n{j}).", "POST /pet/{pet_id} - Update the pet in the store with form data")

formdata = "" # Let's generate formdata from config.updcharacteristics to meet the format from swagger documentation
for key in config.upd_characteristics:
  formdata += f"{key}={config.upd_characteristics[key]}&"
formdata = formdata[:-1] # Delete the last "&" symbol

print(f"Formdata is: {formdata}")

res = requests.post(f'{base_url}/pet/{pet_id}',
                    headers={'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'},
                    data=formdata)
print_response(res)


# GET /pet/{pet_id} Find pet by ID
j += 1
print(f"\n{j}).", " GET /pet/{pet_id} - Check created pet finding it by pet_id")

res = requests.get(f'{base_url}/pet/{pet_id}',
                   headers={'accept': 'application/json', 'Content-Type': 'multipart/form-data'})
print_response(res)


# DELETE /pet/{pet_id} Deletes a pet
j += 1
print(f"\n{j}). ", "DELETE pet/{pet_id} - Delete the pet")

res_del = requests.delete(f'{base_url}/pet/{pet_id}',
                          headers={'accept': 'application/json', 'api_key': 'special-key'})
print_response(res_del)


# GET /pet/findByStatus Finds all the pets with certain status among: 'available', 'pending', 'sold'
j += 1
print(f"\n{j}).", "GET /pet/findByStatus - Find all pets with a status 'available', print first 5 of them")

res = requests.get(f'{base_url}/pet/findByStatus',
                   params={'status': 'available'},
                   headers={'accept': 'application/json'})

if len(res.json()) < 5:
    print_response(res)
else:
    print('Code: ', res.status_code)
    for i in range(5):
        print(res.json()[i])

print("\nNow let's check there's no pet with pet_id we deleted before.")
for i in range(len(res.json())):
    if res.json()[i]['id'] == pet_id:
        print('The {0} item is:\n {1}'.format(i, res.json()[i]))
        break
    elif i == len(res.json()) - 1:
        print(f'No item was found with the ID {pet_id}')


########################################################################################################################


# STORE  Access to Petstore orders
print("\n\nII. STORE. \nHere are main REST API requests related to access to the Petstore orders according to "
      "https://petstore.swagger.io/")


# POST /store/order Place an order for a pet
j = 1 # This is a counter just to numerize the requests when printing
print(f"\n{j}).", "POST /store/order - Place a new order")

body = config.new_order
print(f"New order details: {body}")

res = requests.post(f'{base_url}/store/order',
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(body))
print_response(res)
order_id = res.json()['id']
print(f"Saved order_id is {order_id}")


# GET /store/order/{orderId} Find purchase order by ID
j += 1
print(f"\n{j}).", "GET /store/order/{orderId} - Find the order just created")

res = requests.get(f'{base_url}/store/order/{order_id}', headers={'accept': 'application/json'})
print_response(res)


#DELETE /store/order/{orderId} - Delete purchase order by ID
j += 1
print(f"\n{j}).", "DELETE /store/order/{orderId} - Delete the order by its ID", order_id)

res = requests.delete(f'{base_url}/store/order/{order_id}', headers={'accept': 'application/json'})
print_response(res)


# GET /store/inventory - Returns pet inventories by status
j += 1
print(f"\n{j}).", "GET /store/inventory - Check pet inventories by status")

res = requests.get(f'{base_url}/store/inventory', headers={'accept': 'application/json', 'api_key': 'special-key'})
print_response(res)


########################################################################################################################


# USER  Operations about user
print("\n\nIII. USER. \nHere are main REST API requests related to operations about user according to "
      "https://petstore.swagger.io/")


# POST /user - Create a user
j = 1 # This is a counter just to numerize the requests when printing
print(f'\n{j}).', "POST /user - Create a new user:")

profile = random_profile.RandomProfile(num=1).full_profiles() # Generate a random fake profile to get info from it
i = 0

username = profile[i]['first_name']+profile[i]['last_name'] # Create username by first and last names concatenation
password = random.randint(1000000000, 9999999999) # Generate a password as a random 10-digits number

body = {
        "id": 0,
        "username": f"{username}",
        "firstName": f"{profile[i]['first_name']}",
        "lastName": f"{profile[i]['last_name']}",
        "email": f"{profile[i]['email']}",
        "password": f"{password}",
        "phone": f"{profile[i]['phone_number']}",
        "userStatus": 0
    }

print(body)

res = requests.post(f'{base_url}/user', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(body))
print_response(res)


# GET /user/login - Logs user into the system
j += 1
print(f"\n{j}).", f"GET /user/login - Log in created user with username {username} and password {password}")

res = requests.get(f'{base_url}/user/login', params={'username': f'{username}', 'password': f'{password}'},
                   headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print_response(res)


# GET /user/logout - Logs out current logged in user session
j += 1
print(f"\n{j}).", "GET /user/logout - Log out current logged in user session")

res = requests.get(f'{base_url}/user/logout', headers={'accept': 'application/json'})
print_response(res)


# PUT /user/{username} - Updated user
j += 1
print(f"\n{j}).", "PUT /user/{username} - Update user's info with new:")

# Now let's generate random user info just like we did before in POST request. And leave the same username and password.
profile = random_profile.RandomProfile(num=1).full_profiles() # Generate a random fake profile to get info from it
i = 0

body = {
        "id": 0,
        "username": f"{username}",
        "firstName": f"{profile[i]['first_name']}",
        "lastName": f"{profile[i]['last_name']}",
        "email": f"{profile[i]['email']}",
        "password": f"{password}",
        "phone": f"{profile[i]['phone_number']}",
        "userStatus": 0
    }

print(body)

res = requests.put(f'{base_url}/user/{username}', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(body))
print_response(res)


# GET /user/{username} - Get user by user name
j += 1
print(f"\n{j}).", "GET /user/{username} - Get user by username", username)

res = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})
print_response(res)
text = "! Here we can see that the user's info is the same as it was before the update. So by the PUT request another user was " \
       "created with the same username."
print('\33[31m' + text + '\33[0m')


# GET /user/login - Logs user into the system
j += 1
print(f"\n{j}).", f"GET /user/login - Log into the system with username {username} and password {password}")

res = requests.get(f'{base_url}/user/login', params={'username': f'{username}', 'password': f'{password}'},
                   headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print_response(res)


# DELETE /user/{username} - Delete user
j += 1
print(f"\n{j}).", "DELETE /user/{username} - Delete created user by its username", username)

res = requests.delete(f'{base_url}/user/{username}', headers={'accept': 'application/json'})
print_response(res)


# GET /user/{username} - Get user by user name
j += 1
print(f"\n{j}).", "GET /user/{username} - Get user by username", username)

res = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})
print_response(res)
text = "Now after the user created in the first time has been deleted we can still find another user with the same username. " \
       "\nThat's the one created by the earlier PUT request. So it also needs to be deleted."
print('\33[31m' + text + '\33[0m')


# GET /user/login - Logs user into the system
j += 1
print(f"\n{j}).", f"GET /user/login - Log into the system with username {username} and password {password}")

res = requests.get(f'{base_url}/user/login', params={'username': f'{username}', 'password': f'{password}'},
                   headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print_response(res)


# DELETE /user/{username} - Delete user
j += 1
print(f"\n{j}).", "DELETE /user/{username} - Delete created user by its username", username)

res = requests.delete(f'{base_url}/user/{username}', headers={'accept': 'application/json'})
print_response(res)


# POST /user/createWithArray - Creates list of users with given input array
j += 1
print(f"\n{j}).", "POST /user/createWithArray - Creates list of users with given input array:")

# Create empty lists body, username and password to save generated later random users info
username = []
password = []
body = []

# Now generate info: usernames, passwords, first and last names, emails and phone numbers using random-profile package
# and put info from that profiles into body in a form we can then dump to json data

profile = random_profile.RandomProfile(num=N).full_profiles() # Generate random profiles info

for i in range(N):

    username.append(profile[i]['first_name']+profile[i]['last_name']) # Add a username by first and last names concatenation
    password.append(random.randint(1000000000, 9999999999)) # Generate a password as a random 10-digits number

    body.append({
            "id": 0,
            "username": f"{username[i]}",
            "firstName": f"{profile[i]['first_name']}",
            "lastName": f"{profile[i]['last_name']}",
            "email": f"{profile[i]['email']}",
            "password": f"{password[i]}",
            "phone": f"{profile[i]['phone_number']}",
            "userStatus": 0
        })

print(body)

res = requests.post(f'{base_url}/user/createWithArray', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(body))
print_response(res)


#Now log in and delete each of created users
for i in range(N):
    # GET /user/login - Logs user into the system
    j += 1
    print(f"\n{j}).", f"GET /user/login - Log into the system with username {username[i]} and password {password[i]}")

    res = requests.get(f'{base_url}/user/login', params={'username': f'{username[i]}', 'password': f'{password[i]}'},
                       headers={'accept': 'application/json', 'Content-Type': 'application/json'})
    print_response(res)

    # DELETE /user/{username} - Delete user
    j += 1
    print(f"\n{j}).", "DELETE /user/{username} - Delete created user by its username", username[i])

    res = requests.delete(f'{base_url}/user/{username[i]}', headers={'accept': 'application/json'})
    print_response(res)


# POST /user/createWithList - Creates list of users with given input array
j += 1
print(f"\n{j}).", "POST /user/createWithList - Creates list of users with given input array:")

# Create empty lists body, username and password to save generated later random users info
username = []
password = []
body = []

# Now generate info: usernames, passwords, first and last names, emails and phone numbers using random-profile package
# and put info from that profiles into body in a form we can then dump to json data

profile = random_profile.RandomProfile(num=M).full_profiles() # Generate random profiles info

for i in range(M):

    username.append(profile[i]['first_name']+profile[i]['last_name']) # Add a username by first and last names concatenation
    password.append(random.randint(1000000000, 9999999999)) # Generate a password as a random 10-digits number

    body.append({
            "id": 0,
            "username": f"{username[i]}",
            "firstName": f"{profile[i]['first_name']}",
            "lastName": f"{profile[i]['last_name']}",
            "email": f"{profile[i]['email']}",
            "password": f"{password[i]}",
            "phone": f"{profile[i]['phone_number']}",
            "userStatus": 0
        })

print(body)

res = requests.post(f'{base_url}/user/createWithList', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(body))
print_response(res)


#Now log in and delete each of created users
for i in range(M):
    # GET /user/login - Logs user into the system
    j += 1
    print(f"\n{j}).", f"GET /user/login - Log into the system with username {username[i]} and password {password[i]}")

    res = requests.get(f'{base_url}/user/login', params={'username': f'{username[i]}', 'password': f'{password[i]}'},
                       headers={'accept': 'application/json', 'Content-Type': 'application/json'})
    print_response(res)

    # DELETE /user/{username} - Delete user
    j += 1
    print(f"\n{j}).", "DELETE /user/{username} - Delete created user by its username", username[i])

    res = requests.delete(f'{base_url}/user/{username[i]}', headers={'accept': 'application/json'})
    print_response(res)
