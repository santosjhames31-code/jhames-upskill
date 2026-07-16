package arraylist_of_objects_activity;

public class Student {
    
    private String firstName, lastName, course;
    private char section;
    private int year;
    
    Student(String firstName, String lastName, int year, String course, char section){
        this.firstName = firstName;
        this.lastName = lastName;
        this.year = year;
        this.course = course;
        this.section = section;
    }
    
    void introduce(){
        System.out.println("\nFirst Name : " + firstName);    
        System.out.println("Last Name  : " + lastName);
        System.out.println("Year       : " + year);
        System.out.println("Course     : " + course);
        System.out.println("Section    : " + section);
    } 
    
}
    

