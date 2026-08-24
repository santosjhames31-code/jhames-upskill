package DSA;

class Node{
    int data;
    Node next;
}

class LinkedLists{
    Node top;

    void push(int data){
        Node node = new Node();
        node.data = data;
        node.next = top;
        top = node;
    }

    void display(){
        Node t = top;
        while(t != null){
            System.out.println(t.data);
            t = t.next;
        }
    }
    
    boolean isEmpty(){
        return top == null; 
    }

    int peek(){
        return top.data;
    }

    void pop(){
       
       if (isEmpty()) System.out.println("The Stacks is empty");
       else {
            int data = top.data;
            top = top.next;
       }
    }
    


}

public class Stacks_LinkedList{
    public static void main(String[] args) {
        
        

        LinkedLists ll = new LinkedLists();

        ll.push(2);
        ll.push(3);
        ll.push(4);
        
        ll.display();

    }
}