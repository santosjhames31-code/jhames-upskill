package arraylist_of_objects_activity;

import java.util.*;
import java.io.IOException;

public class Main {
    
     public static void main(String[] args){ 
         
        Scanner input = new Scanner(System.in);
        int size;
        
        ArrayList <Student> studentList = new ArrayList<>();
        
        boolean isDone = false;
        
        outerLoop:
        do{
            try{
                
            System.out.println("====Student Registration Simulation====");
            System.out.print("First Name : ");
            String firstName = input.nextLine();
            System.out.print("Last Name  : ");
            String lastName = input.nextLine();
            System.out.print("Year       : ");
            int year = input.nextInt();
            input.nextLine();
            System.out.print("Course     : ");
            String course = input.nextLine();
            System.out.print("Section    : ");
            char c = input.next().charAt(0);
            c = Character.toUpperCase(c);
        
            studentList.add(new Student(firstName, lastName, year, course, c));
            System.out.println("Student added successfully!");
            innerLoop:
            while(true){
                
            System.out.print("Do you want to add another student [y/N]? ");
            char choice = input.next().charAt(0);
            char ch = Character.toUpperCase(choice);
            input. nextLine();
                switch(ch){
                    case 'Y':
                        System.out.println("");
                        break innerLoop;
                    case 'N':
                        System.out.println("");
                        break outerLoop;
                    default:
                        
                        System.out.println("\nPlease choose from options [y/N] only");
                        
                }
            }
            
        }catch(InputMismatchException e){
            input.nextLine();
            System.out.println("Invalid Data Type, Please try again.");
        }catch(Exception e){
                System.out.println("Error, Please try again.");
        }
              
        }while(!isDone);
        
        for(Student student : studentList) student.introduce();
            
    }
    
}
