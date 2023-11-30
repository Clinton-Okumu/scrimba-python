msg = ('abcdefghijklmnopqrstuvwxyz')
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(len(msg))
print(msg.count('p'))

#slicing strings
print(msg[5])
print(msg[5:9])
print(msg[:15])

#printing string in reverse
msg = 'welcome to python 101 strings'
print(msg)
reverse_string = msg[::-1]
print(reverse_string)