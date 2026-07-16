package array_of_objects_activity;

import java.util.Scanner;

public class Main {
 
    public static void main(String[] args){
        
        Scanner input = new Scanner(System.in);
        int size;
        
        System.out.println("====Student Registration Simulation====");
        System.out.print("Enter Number of Students : ");
        size = input.nextInt();
        input.nextLine();
            Student[] student = new Student[size]; 
        
            for(int i = 0; i < size; i++){
                    System.out.println("\nStudent #"+ (i+1));
                    System.out.print("First Name : ");      //first
                    String firstName = input.nextLine();    
                    System.out.print("Last Name  : ");      //last name
                    String lastName = input.nextLine();
                    System.out.print("Year       : ");      //year
                    int year = input.nextInt();
                    input.nextLine();
                    System.out.print("Course     : ");      //course
                    String course = input.nextLine();
                    System.out.print("Section    : ");      //section
                    char lowerSection = input.nextLine().charAt(0);
                    char  section = Character.toUpperCase(lowerSection);
                    
                    student[i] = new Student(firstName, lastName, year, course, section);
            }
            
            System.out.println("\nStudent Registration Record");
            for(int i = 0; i < size; i++){
                      student[i].introduce();  
            }
            
    }
    
}
