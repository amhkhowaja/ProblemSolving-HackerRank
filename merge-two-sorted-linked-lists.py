def to_list(llist):
    p=llist
    l=[]
    while(p!=None):
        l.append(p.data)
        p=p.next
    return l
def to_LinkList(lst):
    head = SinglyLinkedListNode(lst[0])
    p=head
    for i in range(1,len(lst)):
        n=SinglyLinkedListNode(lst[i])
        p.next=n
        p=p.next 
    return head      
def mergeLists(head1, head2):
    p1=head1
    p2=head2
    l1=to_list(head1)
#    print(l1)
    l2=to_list(head2)
 #   print(l2)
    l3=l1+l2
    l3.sort()
 #   print(l3)
    llst=to_LinkList(l3)
    return llst
