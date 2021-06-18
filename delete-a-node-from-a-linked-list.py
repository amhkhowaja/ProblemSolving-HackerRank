def deleteNode(llist, position):
    # Write your code here
    x=0
    p=llist
    if position ==0:
        llist=p.next
    while(p.next!=None and x<position-1):
        p=p.next
        x+=1
    #temp=p.next
    p.next=p.next.next
    
    return llist
