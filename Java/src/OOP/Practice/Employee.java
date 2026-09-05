package OOP.Practice;

public class Employee {
    String name;
    double baseSalary;

    Employee(String name, double baseSalary){
        this.name = name;
        this.baseSalary = baseSalary;
    }
    
    double calculateSalary(){
        return baseSalary;
    }

    void displayInfo(){
        System.out.println("Salary : " + baseSalary);
    }

}

class Manager extends Employee{

    double bonus;

    Manager(String name, double baseSalary, double bonus){
        super(name, baseSalary);
        this.bonus = bonus;
    }

    @Override 
    double calculateSalary(){
        return super.calculateSalary() + bonus;
    }
    
    @Override
    void displayInfo() {
        System.out.println("Salary : " + calculateSalary());
    }

}

class SalesEmployee extends Employee{
    
    double commission, salesAmount;

    SalesEmployee(String name, double salary, double commission, double salesAmount){
        super(name, salary);
        this.commission = commission;
        this.salesAmount = salesAmount;
    }

    @Override 
    double calculateSalary(){
        return super.calculateSalary() + (commission*salesAmount);
    }

    @Override
    void displayInfo() {
        System.out.println("Salary : " + calculateSalary());
    }

}

class Main{
    public static void main(String[] args) {
      Employee emp = new Employee("Jhames", 120000);  
      emp.calculateSalary();
      emp.displayInfo();

      Manager manager = new Manager("Gian", 120000, 60000);
      manager.calculateSalary();
      manager.displayInfo();

      SalesEmployee sales = new SalesEmployee("Adley", 120000, 10000, 20);
      sales.calculateSalary();
      sales.displayInfo();

    }
}