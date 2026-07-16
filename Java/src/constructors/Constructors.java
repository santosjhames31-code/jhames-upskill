package constructors;

import java.util.Scanner;

public class Constructors {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        boolean run = false;
        
        
        
        while(!run){
            
        try{
        System.out.print("First Name    : ");
        String firstName = input.nextLine();
        System.out.print("Last Name     : ");
        String lastName = input.nextLine();
        System.out.print("Year          : ");
        String year = input.nextLine();
        System.out.print("Course        : ");
        String course = input.nextLine();
        System.out.print("Midterm Grade : ");
        float midtermGrade = input.nextFloat();
        System.out.print("Final Grade   : ");
        float finalGrade = input.nextFloat(); 
        System.out.print("Section       : ");
        input.nextLine();
        String section = input.nextLine();
 
            Student s = new Student(firstName, lastName, year, course, midtermGrade, finalGrade, section);
            System.out.println("--------------------------------------------");
            s.introduce();
            s.evaluateGrade();
            break;
        }catch(Exception e){
            System.out.println("AN ERROR OCCURRED");
            input.nextLine();
            run = false;
            
            }
        }
    }
    
}
