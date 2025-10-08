#ask user to enter their name
name=input("What's your name?").strip().title()#Strip method removes space and title gives first letter as capital

#Greet the user 
print("Hello,")
print(name)

#Different ways to use print function
#1. using + Symbol, which tells to concatenate
print("Hello "+name)

#2 using the comma(,)
print("Hello", name)

#3using end parameter
print("Hello ", end="")
print(name)




#4. using formated string or f string
print(f"Hello ,{name}")


#ways to print the given string in inverted commas
#1. To use the combination of sigle and double commas
print("Hello 'Friend'")

#2. usin black slash
print("Hello \"Friend\"")

