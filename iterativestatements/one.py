# Print all employee names - using for,while loop
# Print all male employee names using for loop
# Print all female employee names using while loop
# print how many male employees?
# print how many female employees?





employees=[{'eid':1,'ename':'Izak','gender':'Male'},
{'eid':2,'ename':'Louella','gender':'Female'},
{'eid':3,'ename':'Carol','gender':'Bigender'},
{'eid':4,'ename':'Eustacia','gender':'Female'},
{'eid':5,'ename':'Francisco','gender':'Male'},
{'eid':6,'ename':'Wenda','gender':'Female'},
{'eid':7,'ename':'Griffin','gender':'Male'},
{'eid':8,'ename':'Diarmid','gender':'Genderqueer'},
{'eid':9,'ename':'Twila','gender':'Female'},
{'eid':10,'ename':'Torrin','gender':'Bigender'},
{'eid':11,'ename':'Odie','gender':'Male'},
{'eid':12,'ename':'Dulcie','gender':'Female'},
{'eid':13,'ename':'Elfie','gender':'Female'},
{'eid':14,'ename':'Arv','gender':'Male'},
{'eid':15,'ename':'Terence','gender':'Male'},
{'eid':16,'ename':'Dix','gender':'Female'},
{'eid':17,'ename':'Rubia','gender':'Female'},
{'eid':18,'ename':'Brent','gender':'Male'},
{'eid':19,'ename':'Rozanne','gender':'Female'},
{'eid':20,'ename':'Kain','gender':'Male'},
{'eid':21,'ename':'Curtice','gender':'Male'},
{'eid':22,'ename':'Woodie','gender':'Male'},
{'eid':23,'ename':'Eal','gender':'Male'},
{'eid':24,'ename':'Eugenie','gender':'Female'},
{'eid':25,'ename':'Marsh','gender':'Male'},
{'eid':26,'ename':'Kaitlin','gender':'Female'},
{'eid':27,'ename':'Mortimer','gender':'Male'},
{'eid':28,'ename':'Ranice','gender':'Female'},
{'eid':29,'ename':'Fairlie','gender':'Male'},
{'eid':30,'ename':'Nell','gender':'Female'},
{'eid':31,'ename':'Chick','gender':'Male'},
{'eid':32,'ename':'Gradey','gender':'Male'},
{'eid':33,'ename':'Cory','gender':'Male'},
{'eid':34,'ename':'Isabelle','gender':'Genderqueer'},
{'eid':35,'ename':'Daron','gender':'Male'},
{'eid':36,'ename':'Electra','gender':'Female'},
{'eid':37,'ename':'Janina','gender':'Female'},
{'eid':38,'ename':'Kerstin','gender':'Female'},
{'eid':39,'ename':'Winston','gender':'Male'},
{'eid':40,'ename':'Kyla','gender':'Female'},
{'eid':41,'ename':'Caryl','gender':'Female'},
{'eid':42,'ename':'Arney','gender':'Male'},
{'eid':43,'ename':'Portia','gender':'Female'},
{'eid':44,'ename':'Cherice','gender':'Female'},
{'eid':45,'ename':'Killian','gender':'Male'},
{'eid':46,'ename':'Reynolds','gender':'Agender'},
{'eid':47,'ename':'Lulu','gender':'Female'},
{'eid':48,'ename':'Mable','gender':'Female'},
{'eid':49,'ename':'Ashlen','gender':'Female'},
{'eid':50,'ename':'Gilli','gender':'Female'},
{'eid':51,'ename':'Tess','gender':'Non-binary'},
{'eid':52,'ename':'Linc','gender':'Male'},
{'eid':53,'ename':'Corabella','gender':'Female'},
{'eid':54,'ename':'Julina','gender':'Female'},
{'eid':55,'ename':'Betteann','gender':'Female'},
{'eid':56,'ename':'Edith','gender':'Female'},
{'eid':57,'ename':'Alexei','gender':'Genderfluid'},
{'eid':58,'ename':'Massimiliano','gender':'Male'},
{'eid':59,'ename':'Barnie','gender':'Male'},
{'eid':60,'ename':'Alvan','gender':'Male'},
{'eid':61,'ename':'Damaris','gender':'Female'},
{'eid':62,'ename':'Conant','gender':'Male'},
{'eid':63,'ename':'Teressa','gender':'Female'},
{'eid':64,'ename':'Virge','gender':'Male'},
{'eid':65,'ename':'Davita','gender':'Female'},
{'eid':66,'ename':'Marris','gender':'Female'},
{'eid':67,'ename':'Eldon','gender':'Male'},
{'eid':68,'ename':'Elliott','gender':'Male'},
{'eid':69,'ename':'Afton','gender':'Female'},
{'eid':70,'ename':'Roma','gender':'Male'},
{'eid':71,'ename':'Debera','gender':'Female'},
{'eid':72,'ename':'Roy','gender':'Male'},
{'eid':73,'ename':'Marj','gender':'Female'},
{'eid':74,'ename':'Jacklyn','gender':'Female'},
{'eid':75,'ename':'Farand','gender':'Non-binary'},
{'eid':76,'ename':'Duffy','gender':'Male'},
{'eid':77,'ename':'Bernadette','gender':'Female'},
{'eid':78,'ename':'Rochell','gender':'Female'},
{'eid':79,'ename':'Abel','gender':'Male'},
{'eid':80,'ename':'Filia','gender':'Female'},
{'eid':81,'ename':'Tadd','gender':'Male'},
{'eid':82,'ename':'Worthington','gender':'Male'},
{'eid':83,'ename':'Perceval','gender':'Male'},
{'eid':84,'ename':'Heddi','gender':'Female'},
{'eid':85,'ename':'Padraic','gender':'Male'},
{'eid':86,'ename':'Mick','gender':'Male'},
{'eid':87,'ename':'Sandy','gender':'Female'},
{'eid':88,'ename':'Teodora','gender':'Female'},
{'eid':89,'ename':'Marcella','gender':'Female'},
{'eid':90,'ename':'Malia','gender':'Female'},
{'eid':91,'ename':'Tate','gender':'Male'},
{'eid':92,'ename':'Neala','gender':'Female'},
{'eid':93,'ename':'Trescha','gender':'Female'},
{'eid':94,'ename':'Clare','gender':'Male'},
{'eid':95,'ename':'Teodor','gender':'Male'},
{'eid':96,'ename':'Stanislas','gender':'Male'},
{'eid':97,'ename':'Aviva','gender':'Female'},
{'eid':98,'ename':'Freeman','gender':'Male'},
{'eid':99,'ename':'Betta','gender':'Female'},
{'eid':100,'ename':'Cordula','gender':'Female'}]




# # print all employees names using ,  for loop ,while loop 


# i=0   # initialize the index
# # Using while loop to print employee names
# while i<len(employees):
#    print(employees[i]['ename'])
#    i=i+1


# for emp in employees:
#       print(emp['ename'])

# ===========================================================================
# Print all male employee names using for and while  loop


# for emp in employees:
#     if emp ['gender']== 'Male':
#         print ("id:",emp["eid"],"name:",emp['ename'])

# e=0
# for emp in employees:
#     if emp['gender']=='Male':
#         e+=1
# print("no of male employees:",e)





# using while loop 

# i=0
# while i<=len(employees)-1:
#     if True:
#         pass
#     i=i+1


# =================================================================================

# Print all female employee names using while loop


# i=0
# while i<=len(employees)-1:
#     if employees[i]['gender']=="Female":
#         print(employees[i]["ename"],"gender:",employees[i]["gender"])
#         i=i+1

i=0
while i<len(employees)-1:
    if employees[i]['gender']=="Female":
        print(employees[i]['ename'], employees[i]['gender'])
    i+=1

# print how many male employees using for loop 

# for i in employees:
#     if i ['gender']=='Male':
#         print(i['ename'])


# print how many male employees?

# emp_count=0
# for emp in employees:
#     if emp ['gender']=='Male': 
# #    if emp ['gender'] =='Female':
#      emp_count=emp_count+1
# print(emp_count)
# print("no of male users",emp_count)
# # print("no of  female users",emp_count)

# print how many Female employees?

# empcount=0
# for emp in employees:
#     if emp['gender']=='Male':
#         empcount=empcount+1
# print(empcount)

# e=0
# for emp in employees:
#     if emp ['gender']=='Male':
#         e=e+1
# print(e)
 

# e=0
# i=0
# while i<=len(employees)+1:
#     if employees[i]['gender']=='Male':
#       print(i)
# i=i+1
# #         e=e+1
#         print(e)



# i=0
# if i<10:
#    print("haresssh")
# print("satya") 
