package abstraction;

import java.time.LocalDate;
import java.time.LocalTime;
public class Main {
   
    public static void main (String[] args){
        LocalDate date = LocalDate.now();
        LocalTime time = LocalTime.now();
        Vehicles car = new Car("Car", 4);
        Motorcycle mot = new Motorcycle("Motorcycle", 2);
        
        Vehicles click = new hondaClick("Motor", 2, "HondaClick 125 v4", "Honda Motors", 2026);
        Vehicles civic = new hondaCivic("Car", 4, "11th-generation Honda Civic", "Honda Cars", 2021);
        
        System.out.println(date + " - " + time);
        click.details();
        System.out.println("");
        civic.details();

    }
    
}
