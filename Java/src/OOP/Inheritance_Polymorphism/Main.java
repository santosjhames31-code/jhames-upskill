package OOP.Inheritance_Polymorphism;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        
        ArrayList <Employee> empList = new ArrayList<>();
        empList.add(new Employee(80.67, 8));
        empList.add(new FullTimeEmployee(90,9));
        empList.add(new ContractEmployee(50,24));
        empList.add(new ContractEmployee(67, 12));
        
        for (Employee emp : empList){
            System.out.println(emp.calculateSalary());
        }
    }
}
