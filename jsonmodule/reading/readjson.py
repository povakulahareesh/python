import json
emp='''{"name":"sai","id":101,"sal":true}'''
print(type(emp))
f=json.loads(emp)
print(type(f))
print(f)