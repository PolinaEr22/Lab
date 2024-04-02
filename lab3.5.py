counter = 0
memory = 'world'
string = 'hello'
values = [0,2,4,6,8,10]

while counter != 10:
    if counter in values:
        print(string)
    else:
        string = string + ' ' + memory
        print(string)
    counter += 1
    if counter > 7:
        break
