package OOP.Review;

public class Main {
    public static void main(String[] args) {
        
// Create a Chicken class (for ChickIT!) with fields name, price, spiceLevel. Write:
// applyDiscount(double percent) — reduces price, returns nothing
// describe() — returns a formatted String like "Spicy Wings - ₱150.00 (Level 3)"
// Overload applyDiscount to accept a flat peso amount instead of a percent
       Chicken ch = new Chicken();
       ch.name = "Jack Daniels";
       ch.price = 12.99;
       ch.spiceLevel = 3;  
       ch.applyDiscount(10);
       ch.describe();
    }
}

class Chicken{
 String name;
    double price;
    int spiceLevel;

    public void applyDiscount(){
        price = price - price * .50 ;        
    }

     public void applyDiscount(int amount){
        price = price - amount;      
    }

    public void describe(){
        System.out.println(name + " - PHP " + price + " - LEVEL " + spiceLevel);
    }

}