list = []
for i in range(int(input("number of commands: "))):
    what = input().split()
    print("command number:", i + 1)
    if what[0] == 'insert':
        list.insert(int(what[1]), int(what[2]))
    elif what[0] == 'remove':
        list.remove(int(what[1]))
    elif what[0] == 'append':
        list.append(int(what[1]))
    elif what[0] == 'sort':
        list.sort()
    elif what[0] == 'pop':
        list.pop()
    elif what[0] == 'reverse':
        list.reverse()
    elif what[0] == 'print':
        print(list)
