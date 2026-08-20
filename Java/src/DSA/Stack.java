package DSA;

public class Stack {
    int[] arr = new int[5];
    int top = -1;

    void push(int element){
        if (isFull()) System.out.println("Stack already full");
        else{
            top++;
            arr[top] = element;
        }
    }
    
    boolean isFull(){
        return top == arr.length - 1;
    }

    int pop(){
        int rTop = arr[top];
        arr[top] = 0;
        top --;
        return rTop;
    }

    int getTop(){
        return arr[top];
    }

    void display(){
        for (int element : arr){
            System.out.println(element);
        }
    }

}


class Stack_Arrays{
    public static void main(String[] args) {
        Stack sa = new Stack();

        sa.push(12); 
        sa.push(2);
        sa.push(3);
        sa.push(4);
        sa.push(5);
        sa.pop();
        sa.pop();
        sa.push(6);
        sa.display();
        System.out.println("Top : " + sa.getTop());
    }
}



