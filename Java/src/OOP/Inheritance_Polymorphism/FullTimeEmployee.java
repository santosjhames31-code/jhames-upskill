package OOP.Inheritance_Polymorphism;

public class FullTimeEmployee extends Employee{
    
    FullTimeEmployee(double hourlyRate, double hoursWorked){
        super(hourlyRate, hoursWorked);
    }

    double calculateSalary(){
        return 150000;
    }

}
