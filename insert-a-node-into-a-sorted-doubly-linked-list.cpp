DoublyLinkedListNode* sortedInsert(DoublyLinkedListNode* llist, int data) {
    
    DoublyLinkedListNode * node=new DoublyLinkedListNode(data);
    DoublyLinkedListNode* p =llist;
    while(p->next!=nullptr){
        if (p==llist && data<=p->data){      //insertion in head
            node->next=p;
            p->prev=node;
            llist=node;
            return llist;
        }
        else if (data>=p->data && data<=p->next->data){ //insertion in between
            DoublyLinkedListNode* temp=p->next;
            p->next=node;
            node->prev=p;
            node->next=temp;
            temp->prev=node;
            return llist;
        }
        p=p->next;
    }
   //Insertion at the end
    p->next=node;
    node->prev=p;
    
    return llist;
    
    

}
