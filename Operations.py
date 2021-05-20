import matplotlib.pyplot as plt

#elementary functions needed for the algorithm  

def Area(a,b,c):
    return (0.5*((b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])))
    #This is the area of triangle formula is in vector form and works for all triangles. 

def Left(a,b,c):
    return Area(a,b,c) > 0

def Collinear(a,b,c):
    return Area(a,b,c) == 0

def Intersection(a,b,c,d):
    return (Left(a,b,c)^Left(a,b,d)) and (Left(c,d,a)^Left(c,d,b))

def Point_int(a,b,c,d):
    t2 = ((a[0]-b[0])*(a[1]-c[1])-(a[0]-c[0])*(a[1]-b[1]))/((c[0]-d[0])*(a[1]-b[1])-(c[1]-d[1])*(a[0]-b[0]))
    [i1,i2]= [(1-t2)*c[0]+t2*d[0],(1-t2)*c[1]+t2*d[1]]
    return [i1,i2]

def Plot(a):
    p1x,p1y = zip(*p1)
    p2x,p2y = zip(*p2)
    x,y = zip(*a)
    plt.figure() 
    plt.plot(p1x,p1y)
    plt.plot(p2x,p2y)
    plt.plot(x,y)
    plt.fill(x,y,'m')
    plt.show()
    
def Plotb(p1,p2):
    p1x,p1y = zip(*p1)
    p2x,p2y = zip(*p2)

    plt.figure() 
    plt.plot(p1x,p1y)
    plt.plot(p2x,p2y)
    
def poly(ch):
    fhand =  open(ch)
    pol = []
    for line in fhand:
        x = line.split(',')
        y = []
        for i in x:
            i.rstrip('\n')
            i = float(i)
            y.append(i)
        pol.append(y)
    return pol

p1 = poly('input1')
p1.append(p1[0])
p2 = poly('input2')
p2.append(p2[0])

#union of polygon 
def union():
    pt_int = [int1[0][2],int1[1][2]]

    union = [pt_int[0]]
    i = p1.index(pt_int[0])
    p = p1[i-1]
    j = 1
    while p not in pt_int:
        union.append(p)
        j = j+1
        p = p1[i-j]

    union.append(p)

    k = p2.index(p)
    p = p2[k-1]
    j = 1
    while p not in pt_int:
        union.append(p)
        j = j+1
        p = p2[k-j]

    union.append(p)
    print('A union B')
    print(union)
    Plot(union)
    
    
#intersection
def intersection():
    pt_int = [int1[0][2],int1[1][2]]

    intersection = [pt_int[0]]
    i = p1.index(pt_int[0])
    p = p1[i+1]
    j = 1
    while p not in pt_int:
        intersection.append(p)
        j = j+1
        p = p1[(i+j)%len(p1)]

    intersection.append(p)

    k = p2.index(p)
    p = p2[k+1]
    j = 1
    while p not in pt_int:
        intersection.append(p)
        j = j+1
        p = p2[(k+j)%(len(p2))]
    
    intersection.append(p)
    print('A intersection B')
    print(intersection)
    Plot(intersection)
    
#A-B
def AminB():
    pt_int = [int1[0][2],int1[1][2]]

    aminusb = [pt_int[0]]
    i = p1.index(pt_int[0])
    p = p1[i-1]
    j = 1
    while p not in pt_int:
        aminusb.append(p)
        j = j+1
        p = p1[i-j]

    aminusb.append(p)

    k = p2.index(p)
    p = p2[k+1]
    j = 1
    while p not in pt_int:
        aminusb.append(p)
        j = j+1
        p = p2[(k+j)%(len(p2))]
    
    aminusb.append(p)
    print('A minus B')
    print(aminusb)
    Plot(aminusb)
    
#B-A

def BminA():

    pt_int = [int1[0][2],int1[1][2]]

    bminusa = [pt_int[0]]
    i = p1.index(pt_int[0])
    p = p1[i+1]
    j = 1
    while p not in pt_int:
        bminusa.append(p)
        j = j+1
        p = p1[(i+j)%len(p1)]

    bminusa.append(p)

    k = p2.index(p)
    p = p2[k-1]
    j = 1
    while p not in pt_int:
        bminusa.append(p)
        j = j+1
        p = p2[k-j]
    
    bminusa.append(p)
    print('B minus A')
    print(bminusa)
    Plot(bminusa)
    
int1 = []
count = 0
for i in range(len(p1)-1):
    for j in range(len(p2)-1):
        if Intersection(p1[i],p1[i+1],p2[j],p2[j+1]):
            a = Point_int(p1[i],p1[i+1],p2[j],p2[j+1])
            int1.append([i+1+count,j+1+count ,a])
            count=count+1
            #print(count)
            #print(int1)

#print(int1)
for isc in int1:
    p1.insert(isc[0],isc[2])
    p2.insert(isc[1],isc[2])

union()
intersection()
AminB()
BminA()