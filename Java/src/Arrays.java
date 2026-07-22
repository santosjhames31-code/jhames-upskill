import java.util.Scanner;
public class Arrays{

    public static void display(int[] arrNum){
        for (int num : arrNum) System.out.print(num + " ");
    }
    public static void odd(int[] arrNum){
        int count = 0;
        for(int num : arrNum) {
            if (num % 2 == 1) {
            System.out.print(num + " ");
            count++;
            }  
        }
        System.out.println("Odd : " + count);
    }
     public static void even(int[] arrNum){
        int count = 0;
        for(int num : arrNum) {
            if (num % 2 == 0 && num != 0){
            System.out.print(num + " ");
            count++;   
            } 
        }
        System.out.println("Even : " + count);
    }

    public static void reverse(int[] arrNum){
        for(int i = arrNum.length - 1; i >= 0; i--) System.out.print(arrNum[i] + " ");
    }
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int size;
        do{
            size = Integer.parseInt(sc.nextLine());
            if (size > 0) break;
        }while(true);
        
        int[] arrNum = new int [size]; 
        for(int i = 0; i < size; i++){
            System.out.print("Enter element at index [" + i + "] : ");
            arrNum[i] = Integer.parseInt(sc.nextLine());
        }
        int choice;
        do{
            System.out.println("");
            System.out.println("[1] Display");
            System.out.println("[2] Odd");
            System.out.println("[3] Even");
            System.out.println("[4] Reverse");   
            System.out.println("[5] Exit");  
            choice = Integer.parseInt(sc.nextLine());
            switch(choice){
                case 1: 
                    display(arrNum);
                break;
                case 2:
                    odd(arrNum);
                break;
                case 3: 
                    even(arrNum);
                break;
                case 4:
                    reverse(arrNum);
                break;
                case 5:
                    System.out.println("Exiting Program...");
                break;
                default:
                    System.out.println("Invalid Choice");

            }
        }while(choice != 5);
        

    }

}