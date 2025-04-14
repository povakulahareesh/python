import json
emp_data='''
         {
         "eid":101,
         "ename":"Rahul",
         "loc":true
         }
         '''
emp_dict=json.loads(emp_data)
print(type(emp_dict))
print(emp_dict)

# # loads()--> json to python obj 
# # dumps ()-->python obj to json obj 


# read employee.json file
# and write eid  ,ename  in emp .csv file/
# and write into ms (exe.vlxl)
# ==========================================



