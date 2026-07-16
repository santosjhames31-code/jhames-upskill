package objectClass;

import constructors.Person;
import java.util.Scanner;

public class ObjectAndClass {
   
    public static void main(String[] args){
    
        Scanner input = new Scanner(System.in);
        Student student = new Student();
        
        System.out.print("Enter Grade : ");
        student.grade = input.nextFloat();

        System.out.println(student.grade);

        student.isPassed();
        
    }
    
}
