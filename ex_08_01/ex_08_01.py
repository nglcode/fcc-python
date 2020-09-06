han = open('C:/Users/agdev/Desktop/py4e/ex_08_01/mbox-short.txt')

for line in han:
    line = line.rstrip()
    # print('Line:', line)
    wds = line.split()
    # print('Words:',wds)
    if len(wds) < 3 or wds[0] != 'From': 
        # print('Ignore')
        continue
    print(wds[2])
