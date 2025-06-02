#  map exepcting function and iterator 
#  map (1,2)
#  map(1 is function and  2 is sequernce)
#  sequence:
# In Python, a sequence is an ordered collection of elements that can be indexed and iterated over

marks=[1,2,3,33,44,55]  # sequence 
def add (mark):  # function 
    return mark+1
# print(add(2))
# map(function,sequence)
#  map excepting one function reference  and  sequence  --> what is sequence may be here    marks only

# a=map(add,marks)
# print(a)
#  map excepting  function and sequence 
#  map execute function for every element  in the sequence     
#  map function execute  provided function for   every element present in the  sequence  and apply some functionality  return  new element  
#  am getting map object  convert into list type then am printing 
# map excepting one function and  sequence  
map_obj=map(add,marks)
new_marks=list(map_obj)

print(marks)
print(new_marks)


