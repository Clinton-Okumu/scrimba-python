def greeting(name,age='34'):
    print("Hello " + name +  "youre age is: " + str(age))
    print(f"hello {name}, youre age is: {age}")

name = input("Enter youre name: ")
greeting(name,"21")
greeting("judith")