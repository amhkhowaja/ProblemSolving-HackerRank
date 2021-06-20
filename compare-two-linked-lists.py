def compare_lists(llist1, llist2):
    p1=llist1
    p2=llist2
    l1=[]
    l2=[]
    while p1.next!=None:
        l1.append(p1.data)
        p1=p1.next
    while p2.next!=None:
        l2.append(p2.data)
        p2=p2.next
    if l1==l2:
        return 1
    else:
        return 0        
