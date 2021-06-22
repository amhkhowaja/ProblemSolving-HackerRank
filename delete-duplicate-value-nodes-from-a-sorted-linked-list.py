def removeDuplicates(llist):
    # Write your code here
    head=llist
    p=llist   
    #Strategy is removing the next node if it is equal to current node:
    while(p.next!=None):
        while(p.data==p.next.data ):
            if p.next.next!=None:
                p.next=p.next.next
            else:
                p.next=None
                break
        if p.next!=None:
            p=p.next
        else :
            break
    return head
