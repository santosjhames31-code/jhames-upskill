package objectClass;

public class Student {
    
    static String name; 
    int id, gradeLevel;
    float grade, average;
    char section;
    
    void isPassed(){
    
        if(grade < 75) System.out.println("Failed");
        else System.out.println("Passed");
    }
    
}
