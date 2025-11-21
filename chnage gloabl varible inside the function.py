#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x="wow"
def myfunc():
      global x
      x= "Aura "

myfunc()
print("python is "+x)
