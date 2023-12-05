names = ['john clEEse','Eric IDLE','micheal']
names1 = ['graHam chapman','clint','clint okumu']
msg = 'you are invited to the party on saturday.'

names += names1
for index in range(2):
    names.append(input('Enter a new name: '))

for name in names:
    msg1 = name.title() + '!' + msg
    print(msg1)