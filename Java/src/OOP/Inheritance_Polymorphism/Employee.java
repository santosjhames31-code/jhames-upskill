package OOP.Inheritance_Polymorphism;

public class Employee{

    private double hourlyRate;
    private double hoursWorked;
    static double fixedSalary = 130000;

    Employee(double hourlyRate, double hoursWorked){
        this.hourlyRate = hourlyRate;
        this.hoursWorked = hoursWorked;
    }

    double calculateSalary(){
        return hourlyRate * hoursWorked;
    }
}