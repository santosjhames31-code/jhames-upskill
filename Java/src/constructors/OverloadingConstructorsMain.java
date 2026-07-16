package constructors;

public class OverloadingConstructorsMain {
  
    public static void main(String[] args){
    
        EmployeeInfo employee1 = new EmployeeInfo("Jhames", "Male", "Filipino", "Bulacan", 19);
        EmployeeInfo employee2 = new EmployeeInfo("Shaenna", "Female", "Filipino", "Bulacan");
        EmployeeInfo employee3 = new EmployeeInfo("Laurente", "Female", "Spanish", 19);
        EmployeeInfo employee4 = new EmployeeInfo();
        
        System.out.println(employee1.name + ", " + employee1.sex + ", " + employee1.nationality + ", " + employee1.address + ", " + employee1.age);
        System.out.println(employee2.name + ", " + employee2.sex + ", " + employee2.nationality + ", " + employee2.address + ", " + employee2.age);
        System.out.println(employee3.name + ", " + employee3.sex + ", " + employee3.nationality + ", " + employee3.address + ", " + employee3.age);
        System.out.println(employee4.name + ", " + employee4.sex + ", " + employee4.nationality + ", " + employee4.address + ", " + employee4.age);

        
    }
    
}
