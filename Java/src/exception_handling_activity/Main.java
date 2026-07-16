package exception_handling_activity;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
   
    public static void main(String[] args){
    
        Scanner input = new Scanner(System.in);
        int num = 0;

       do{
            try{    
                System.out.print("Enter a number : ");
                num = input.nextInt();
                break;
            }catch(InputMismatchException e){
                input.nextLine();
                System.out.println("Invalid Data type, Please try again.");
            };
        }while(true);
            int square = num*num;
        System.out.println("Square : " + square);
        
    }
    
}
