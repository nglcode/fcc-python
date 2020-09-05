fh = open('C:/Users/agdev/Desktop/py4e/ex_07_01/mbox-short.txt')
print(fh)

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
