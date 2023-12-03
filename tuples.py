#tuples - faster lists you cant chnage
friends = ['clint','micheal','terry','eric','graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
print(friends[2:4])
print(friends_tuple[2:4])

#sets
my_friends_set = {'leon','clint','laurel','john'}
friends_set = {'john','luka','eric','dion','clint','clint'}
print(friends_set)
print(friends_set.difference(my_friends_set))
print(friends_set.intersection(my_friends_set))