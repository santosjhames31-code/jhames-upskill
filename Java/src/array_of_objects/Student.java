package array_of_objects;

public class Student {
    
    String name, section;
    int gradeLevel;
    
    Student(String name, String section, int gradeLevel){
        this.name = name;
        this.section = section;
        this.gradeLevel = gradeLevel;
    }
    
    void introduce(){
        System.out.println("Name        : " + name);
        System.out.println("Section     : " + section);
        System.out.println("Grade Level : " + gradeLevel);
    }
    
}
