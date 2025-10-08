#Defining function with def keyword
def hello():
    print("Hello")


name=input("What's your name? ")
hello()
print(name)



#Defining functions with arguments
def hello(to="world"):
    print("Hello ",to)

name=input("What's your name? ")
hello(name)