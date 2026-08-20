package DSA;

class Node{
    int data;
    Node next;
}

class Stacks_LinkedList {
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
}


class Main{
    public static void main(String[] args) {
        Stacks_LinkedList sl = new Stacks_LinkedList();
        sl.push(1);

        sl.display();
    }
}
