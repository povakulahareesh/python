# page check is a decorator  and takes one function as a argument  it modify existing function and return the  modified function 
#  whenever  we want we can  add decorator 
def page_check(func):
    def inner(name,login):
        if login == False:
            print("please try to login first")
        else:
            return func(name,login) 
        return inner
    def  home_page(name,login):
        print("home page",name)
    def order_page(name,login):
        print("order page",name)    
        
           
         