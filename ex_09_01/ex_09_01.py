fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open('C:/Users/agdev/Desktop/py4e/ex_09_01/'+fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        
        # oldcount = di.get(w,0)
        # print(w,'old',oldcount)
        # newcount = oldcount +1
        # di[w] = newcount 
        # print(w,'new',newcount)

        # Esta linea es la versión one-line de las 5 líneas anteriores:
        di[w] = di.get(w,0) + 1

        # if w in di :
        #     di[w] = di[w] + 1
        # else:
        #     di[w] = 1

        # print(w, di[w])

print(di)

# Loop para encontrar la más común
largest = -1
theword = None

for k,v in di.items():intr
    # print(k,v)
    if v > largest:
        largest = v
        theword = k

print('Done:', theword, largest)
