# import requests
# data = requests.get('https://dummyjson.com/products')
# product_data=data.json()
# status_code = data.status_code
# print(product_data)
# print(status_code)



# import requests
# data = requests.get('https://dummyjson.com/products')
# product_data=data.json()
# status_code = data.status_code

# print(type(product_data))
# print(status_code)
# products=product_data['products']
# print(len(products))





import requests,mysql.connector

data = requests.get('https://dummyjson.com/products')
product_data=data.json()
products=product_data['products']

new_products=[]
for product in products:
    new_products.append((product['id'],product['title'],product['price'],product['category']))

print(new_products)




