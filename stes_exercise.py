friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
print('Eric' in friends and 'John' in friends)
combined_set = friends | my_friends
print(combined_set)
print(friends.intersection(my_friends))
print(friends.difference(my_friends))
#diff
print(friends - my_friends)
#remove duplicates
cars_no_duplicates = set(cars)
print(cars_no_duplicates)
