package assignment_2;

public class RunEmployee{
    public static void main(String[] args) {
        
        Employee e1 = new Employee();
        Employee e2 = new Employee("Gian", 1234);
        Employee e3 = new Employee("Adley", 67676, 70000);

        e1.computeSalary(8, 250);
        e2.computeSalary(10, 350);
        e3.computeSalary(8, 500);
         
        e1.updateSalary(500);
        e2.updateSalary(500, true);
        e3.updateSalary(1000, true);
        
        e1.displayInfo();
        e2.displayInfo();
        e3.displayInfo();
        
        int count = Employee.getEmployeeCount();
        System.out.println("Employee Count : " + count);
    }

}
