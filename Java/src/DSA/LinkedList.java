class Node{
    int data;
    Node next;
}

class LinkedList{
    Node head;

    void insert(int data){
        Node node = new Node();
        node.data = data;
        node.next = null;
        if(head == null) head = node;
        else{
            Node n = head;
            while(n.next != null){
                n = n.next;
            }   
            n.next = node;
        }
    }

    void display(){
        Node n = head;
        while (n != null){
            System.out.println(n.data);
            n = n.next;
        }
    }

    void insertStart(int data){
        Node node  = new Node();
        node.data = data;
        node.next = head;
        head = node;
    }

    void insertIndex(int index, int data){
        Node node = new Node();
        node.data = data;
        node.next = null;

        if(index == 0) insertStart(data);
        else{
            Node n = head;
            for (int i = 0; i < index -1; i++){
                n = n.next;
            }   
            node.next = n.next;
            n.next = node;
        }
    }

    void delete(int index){
        Node n = head;
        Node n1 = null;
            for(int i = 0; i < index - 1; i++){
                n = n.next;
            } 
            n1 = n.next;
            n.next = n1.next;
    }


}