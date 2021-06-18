def reverse(llist):
    # Write your code here
    listaddresses=[]
    p=llist
    #Storing the addresses of each node in the list
    while(p!=None):
        listaddresses.append(p)
        p=p.next
    llist=listaddresses[len(listaddresses)-1]
        #Looping and linking the nodes again 
    
    for i in range(len(listaddresses)-1, -1,-1):
        listaddresses[i].next=listaddresses[i-1]
    listaddresses[0].next=None
    return llist
