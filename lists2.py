friends = ['john','clare','terry','eric','clint']
cars = ['911','130','340','740','308']
print(friends)
friends.sort()#sorting the list
print(friends)
friends.sort(reverse=True)#sorting the list in reverse-descending order
print(friends)
friends.reverse()
print(friends)


print(min(cars))
print(max(cars))

friends[2] = 'Prudence'#changing a particular value in lists
print(friends)
friends.extend(cars)#combining cars and friends 
print(friends)
friends.remove('clint')
print(friends)
friends.pop()
print(friends)