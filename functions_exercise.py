def greeting(name, age=28,color="red"):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    #print('Hello '  +  name + ', you will be ' + str(age)+1 + 'next birthday')
    print(f'Hello {name}, you will be {age + 1} years old next birthday!')
    print(f"We hear you like the color {color}!")
color = input('Enter your favourite color: ').lower()
name = input('Enter your name: ').capitalize()
age = int(input('Enter your age: '))
greeting(name, age, color)