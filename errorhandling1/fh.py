import requests
import json 

#extract data from source
resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp_data.json()

#transform
new_users=[]
for user in users:
    new_users.append({"user_id":user['id'],
                      "user_name":user['name'],
                      "city":user['address']['city'],
                      "mobile":user['phone']
                      })

print(new_users)

#load data into new json file