package hashmap_activity;

public class Student {
    static int studentSize;
    private String name, course, address, year;
    private int id;
    
     Student(String name, String course, String year, String address, int id){
        this.name = name;
        this.course = course;
        this.year = year;
        this.address = address;
        this.id = id;
    }
    
     static String courseSwitch(int i){
     
         String course = "Invalid";
         switch(i){
            case 1:
            course = "BSIT";
            break;
            case 2:
            course = "BSIS";
            break;
            case 3:
            course = "BSCS";
            break;
         }
        return course; 
     }
     
     static String yearSwitch(int i){
         String year = "Invalid";
         switch(i){
            case 1:
            year = "Freshmen";
            break;
            case 2:
            year = "Sophomore";
            break;
            case 3:
            year = "Junior";
            break;
            case 4:
            year = "Senior";
            break;
         }
         return year;
     }
     
     void printRecord(){
         System.out.println("ID      : " + id);
         System.out.println("Name    : " + name);
         System.out.println("Course  : " + course);
         System.out.println("Year    : " + year);
         System.out.println("Address : " + address);
     }
     
}
