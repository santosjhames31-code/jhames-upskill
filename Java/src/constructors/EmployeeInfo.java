
package constructors;

public class EmployeeInfo {
    
    String name, sex, nationality, address;
    int age;
    
     EmployeeInfo(){
    
        name = "N/A";
        sex = "N/A";
        nationality = "N/A";
        address = "N/A";
        age = 0;
            
    }
    
    EmployeeInfo(String name, String sex, String nationality, String address, int age){
    
        this.name = name;
        this.sex = sex;
        this.nationality = nationality;
        this.address = address;
        this.age = age;
            
    }
    
    EmployeeInfo(String name, String sex, String nationality, String address){
    
        this.name = name;
        this.sex = sex;
        this.nationality = nationality;
        this.address = address;
        age = 0;
            
    }
    
    EmployeeInfo(String name, String sex, String nationality, int age){
    
        this.name = name;
        this.sex = sex;
        this.nationality = nationality;
        address = "N/A"; 
        this.age = age;
            
    }
    
    
    
}
