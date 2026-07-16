package abstraction_interface;

public class Main {
    
    public static void main(String[] args){
    
    Mage m = new Mage("Shaenna", "Fireball", 100, 70);
    Warrior w = new Warrior("Jhames", "Holy Sword", 50, 120, 130);
    
    m.attack();
    m.showStats();  
        System.out.println("");
    w.attack();
    w.showStats();
    
    }
}
