msg = """ dear clint,
how are you
hope this finds you well"""
print(msg)

#find/replace stings
msg = 'welcome to python'
print(msg.replace('python','C')) #replaces python with c
print('python' in msg) #checks if word python is in msg

#string formatting
name = 'Clinton'
color = 'blue'
msg = f'{name} loves the color {color}'
print(msg)