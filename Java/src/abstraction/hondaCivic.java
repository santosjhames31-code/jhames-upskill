package abstraction;

public class hondaCivic extends Car{
    String name;
    String manufacturer;
    int yearReleased;
    
    hondaCivic(String vehicleType, int numberOfWheels, String name, String manufacturer, int yearReleased){
        super(vehicleType, numberOfWheels);
        this.name = name;
        this.manufacturer = manufacturer;
        this.yearReleased = yearReleased;
    }
    
    void details(){
        super.details();
        System.out.println("Name          : " + name);
        System.out.println("Manufacturer  : " + manufacturer);
        System.out.println("Year Released : " + yearReleased);;
    }
    
}
