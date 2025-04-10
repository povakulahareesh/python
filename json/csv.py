# import csv
# fp=open('emp.csv','r')
# csvreader=csv.reader(fp)
# print (csvreader)

# print(type(csvreader))

# for user in csvreader:
#     print(user)


# ===================================

# import csv

# fp = open('emp.csv','r')
# csvreader=csv.reader(fp)

# print(csvreader)
# print(type(csvreader))

# for user in csvreader:
#     print(user)

# ===================================
# import csv

# fp = open('emp.csv','r')
# csvreader=csv.reader(fp)
# users=list(csvreader)
# for user in users[1:]:
#     print(user[1])


# ================================

# e=["qq","ee","rr","ooo"]
# print(e[2])
# t=e[2:4]
# print(t)

# ======================================

# import requests,csv,json 
# resp=requests.get('https://dummyjson.com/products')
# product_data=resp.json()

# print(type(product_data))     #  <class,dict>
# products=product_data['products']

# print(type(products))         #<class,list>

# # ==========================================
# import requests,csv,json 
# # extract data from source - rest api/cloud apis/database
# resp=requests.get('https://dummyjson.com/products')
# product_data=resp.json()
# products=product_data['products']

# #load into beauty.csv and beauty.json

# fp1 = open('beauty.csv','w',newline="")
# csvwriter=csv.writer(fp1)
# csvwriter.writerow(['PID','Name','Price','Category'])

# for product in products:
#     csvwriter.writerow([product['id'],product['title'],product['price'],product['category']])

# print('New CSV File created successfully')

# fp1.close()


# =========================================

# fp=open("emp.txt","r")
# data=fp.read()
# print(data)
# fp.close()




a=int(input(" enter no:"))
b=int(input(" enter no:"))
print(a/b)
