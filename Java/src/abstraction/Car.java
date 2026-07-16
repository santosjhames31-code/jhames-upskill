package abstraction;

public class Car extends Vehicles {
    
    Car(String vehicleType, int numberOfWheels){
        this.numberOfWheels = numberOfWheels;
        this.vehicleType = vehicleType;
    }

     void details(){
        System.out.println("Vehicle Type  : " + vehicleType);
        System.out.println("Wheels        : " + numberOfWheels);
    }
    
}
