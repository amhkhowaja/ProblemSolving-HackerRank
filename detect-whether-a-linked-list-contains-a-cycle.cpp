bool has_cycle(SinglyLinkedListNode* head) {
    //Using Tortoise-Hare Algorithm:
    
    SinglyLinkedListNode* tortoise=head; // it is slower
    SinglyLinkedListNode* hare =head; //It is faster
    do {
        
        tortoise=tortoise->next;
        hare=hare->next->next;
        if (tortoise==NULL or hare ==NULL){
            return false;
        }
        if (tortoise ==hare ){
            return true;
        }
    }while(tortoise!=hare);
    return false;

}
