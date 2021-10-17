nothing = []

mate = open('mate.csv', 'r')
cut = mate.readlines()
for line in cut:
    meth = line.split(',')
    ilist = []
    for i in meth:
        ilist.append(i.strip())
    nothing.append(ilist)
print(nothing)
