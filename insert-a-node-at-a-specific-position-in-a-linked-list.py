#This Function will insert the node at specific position :
#HackerRank Problem Solved 

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    if llist is None:
        return SinglyLinkedListNode(data)
    x=0
    p=llist
    while(p.next!=None and x<position-1):
        p=p.next
        x+=1
    node=SinglyLinkedListNode(data)
    temp=p.next
    p.next =node
    node.next=temp
    return llist
  
