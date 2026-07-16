package constructors;

public class Student {
    
    String firstName, lastName, year, course, section;
    float midtermGrade, finalGrade;
    
    Student(String firstName, String lastName, String year, String course, float midtermGrade, float finalGrade, String section){
    
        this.firstName = firstName;
        this.lastName = lastName;
        this.year = year;
        this.course = course;
        this.midtermGrade = midtermGrade;
        this.finalGrade = finalGrade; 
        this.section = section;
            
    }
    
    void introduce(){
        System.out.println("I am " + firstName + ", " + year  + " student from " + section);
    }
    
    void evaluateGrade(){
        float ave = (finalGrade + midtermGrade) / 2; 
        System.out.print("Average  : " + ave );
        
        System.out.print("\nStanding : ");
        if(ave < 75){
            System.out.print("Failed");
        }else if(ave < 90){
            System.out.print("Passed");
        }else if( ave < 95){
            System.out.print("With Honors");
        }else if(ave < 98){
            System.out.println("With High Honors");
        }else if(ave <= 100){
            System.out.print("With Highest Honors");
        }else{
            System.out.print("Invalid Grade");
        }
        System.out.println("");
    }
    
}
