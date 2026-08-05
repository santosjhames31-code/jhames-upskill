package assignment_2;

class Employee{
    
    private String name; 
    private int id;
    private double hoursWorked, salary, ratePerHour; 
    static int employeeCount = 0;

    public Employee(){
        name = "N/A";
        id = 0;
        salary = 0;
        employeeCount++;
        System.out.println("Successufully Added!");
    }

    public Employee(String name, int id){
        this();
        this.name = name;
        this.id = id;
    }

    public Employee(String name, int id, double salary){
        this(name, id);
        this.salary = salary;
    }

    public void updateSalary(double amount){
        double initSalary = salary;
        salary += amount;
        System.out.println("==========================================================================================================================================");
        System.out.println("Congrats user " + id + " you succesfully updated your salary from PHP " + initSalary + " to PHP " + salary + " (+PHP " + amount + ")");
        System.out.println("==========================================================================================================================================");
    }

    public void updateSalary(double amount, boolean isPercentage){
        double initSalary = salary;
        String txt = null;
        if(isPercentage){
            salary += salary * (amount / 100);
            txt = (int) amount + "%";
        }else{
            salary += amount;
            txt = "PHP " + amount;
        }
        System.out.println("==========================================================================================================================================");
        System.out.println("Congrats user " + id + " you successfully updated your salary from PHP " + initSalary + " to PHP " + salary + " with additional " + txt);
        System.out.println("==========================================================================================================================================");
    }

    public double computeSalary(double hoursWorked, double ratePerHour){
        this.hoursWorked = hoursWorked;
        this.ratePerHour = ratePerHour;
        double grossPay = hoursWorked * ratePerHour;
        double tax = grossPay * 0.12;
        double netSalary = grossPay - tax;
        salary = netSalary;
        return netSalary;
    }

    public void displayInfo(){
        System.out.println("=====================================");
        System.out.println("ID           : " + id);
        System.out.println("Name         : " + name);
        System.out.println("Salary       : " + salary);
        System.out.println("Hours Worked : " + hoursWorked);
        System.out.println("RPH          : " + ratePerHour);
        System.out.println("=====================================");
    }

    public String getName(){
        return name;
    }
    
    public void setName(String name){
        this.name = name;
    }

    public int getID(){
        return id;
    }

    public void setID(int id){
        this.id = id;
    }

    public double getSalary(){
        return salary;
    }
    
    public void setSalary(double salary){
        this.salary = salary;
    }

    public double getHoursWorked(){
        return hoursWorked;
    }
    
    public void setHoursWorked(double hoursWorked){
        this.hoursWorked = hoursWorked;
    }
    
    public double getRatePerHour(){
        return ratePerHour;
    }
    
    public void setRatePerHour(double ratePerHour){
        this.ratePerHour = ratePerHour;
    }

    public static int getEmployeeCount(){
        return employeeCount;
    }


}