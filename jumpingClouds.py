# challenge link https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem 

def jumpingOnClouds(c):
    jumps = 0
    index=[]
    for i in range(len(c)):
        if c[i]==0:
            index.append(i)
    band=False
    cont = 0
    for i in range(len(index)-1):
        if index[i+1] == index[i]+2:
            jumps += 1
            band=False
            cont = 0
        elif index[i+1] == index[i] +1:
            cont = cont +1
            if band == True and cont==2:
                cont=0
                jumps -= 1
                band=False
            band=True
            jumps += 1
    return jumps
c=[0, 0, 1, 0, 0, 1, 0]
#c=[0, 0, 0, 1, 0, 0]
c=[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0 ,0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0]
print(jumpingOnClouds(c))
