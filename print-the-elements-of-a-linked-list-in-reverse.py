def reversePrint(llist):
    # Write your code here
    p=llist
    l=[]
    while(p!=None):
       l.append(p.data)
       p=p.next
    for i in range(len(l)-1, 0-1, -1):
        print(l[i])
