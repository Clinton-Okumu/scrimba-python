my_file = open('greetings.txt','r')
print(my_file.read(10))
print(my_file.readline())
print(my_file.readline())
line_by_line = my_file.readlines()
line_by_line1 = my_file.read().splitlines()
print('readlines: ',line_by_line)
print('splitlines: ',line_by_line1)
my_file.close()
