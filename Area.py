import matplotlib as plt

#creating a node

class Node:
    def __init__(self,point,nxt):
        self.point =  point
        self.next = nxt
        
#creating a linked list 

class LinkedList:
    def __init__(self):
        self.head = None 
        
    def insert_at_beg(self,point):
        node = Node(point,self.head)
        self.head = node
        
    def prnt(self):
        if self.head is None:
            print('linked list is empty')
            return
    
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.point) +'-->'
            itr = itr.next
            
        print(llstr)
        
ll = LinkedList()

fhand =  open('input1')
for line in fhand:
    x = line.split(',')
    y = []
    for i in x:
        i.rstrip('\n')
        i = int(i)
        y.append(i)
    ll.insert_at_beg(y)
    
#Area of a triangle
def Area1(a,b,c):
    return abs(0.5*((b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])))

#Area of a polygon
def Area2(ll):
    add = 0
    p = ll.head
    a = p.next
    while a.next:
        add += Area1(p.point, a.point, a.next.point)#point p is fixed, the other two vertices are selected in sequence to find area
        a = a.next
    #print('The area of the above figure is:',add)
    return add 
    
s = Area2(ll)
s = str(s)
    
import numpy as np
import matplotlib.pyplot as plt


arr = []
p = ll.head
while p:
    arr.append(p.point)
    p = p.next
    
arr.append(arr[0]) #repeat the first point to create a 'closed loop'

xs, ys = zip(*arr) #create lists of x and y values

plt.figure()
plt.plot(xs,ys)
plt.axis('equal')
plt.title('Area of this figure is: '+s)
plt.show()