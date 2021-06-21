def count_elements(llist):
    p=llist
    x=0
    while(p.next!=None):
        x+=1
        p=p.next
    return x
def getNode(llist, positionFromTail):
    # Write your code here
    p=llist
    length=count_elements(llist)
    position=(length)-positionFromTail
    x=0
    while (p.next!=None and x!=position):
        p=p.next
        x+=1
    return p.data
  
  #Passed all Testcases
