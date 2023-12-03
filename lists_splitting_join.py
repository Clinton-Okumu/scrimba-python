msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print('Welcome to Python 101: Split and Join')
print(msg.split())
print(msg.split(' '))
print(csv.split(','))
print(''.join(friends_list))#joining a string

print(''.join(msg.split()))
print(msg.replace(' ', ''))