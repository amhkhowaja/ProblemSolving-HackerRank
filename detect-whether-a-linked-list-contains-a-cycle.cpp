bool has_cycle(SinglyLinkedListNode* head) {
    //Using Tortoise-Hare Algorithm:
    
    SinglyLinkedListNode* tortoise=head; // it is slower(iterate by incrementing 1)
    SinglyLinkedListNode* hare =head; //It is twice as faster as tortoise (iterate by incrementing 2 places)
    
    do {
        tortoise=tortoise->next;
        if (hare->next!=nullptr){    // if hare.next is null then null.next would give an error
            hare=hare->next->next;
        }
        
        if (hare ==nullptr or hare->next==nullptr){
            return false;
        }
        else if (tortoise ==hare ){
            return true;
        }
    }while(tortoise!=hare);
    return false;

}
