n=[1,1,2,3,5]
for i in range(4,10000000000):
    b=n[i]+n[i-1]
    n.append(b)
    if len(str(b))==1000:
        print(len(n))
        break
