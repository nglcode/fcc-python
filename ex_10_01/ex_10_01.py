fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open('C:/Users/agdev/Desktop/py4e/ex_10_01/'+fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        
        di[w] = di.get(w,0) + 1

# print(di)

tmp = list()
for k,v in di.items() :
    # print(k,v)
    newt = (v,k)
    tmp.append(newt)

# print(tmp)

tmp = sorted(tmp, reverse=True)
# print(tmp)

for v,k in tmp[:5] :
    print(k,v)