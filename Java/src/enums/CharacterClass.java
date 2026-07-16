package enums;

public enum CharacterClass {

    WARRIOR("WARRIOR", "Arthur", 200, 170),
    MAGE("MAGE", "Merlin" ,300, 100),
    ARCHER("ARCHER", "Robin",100, 120);
            
    int aP, hP;
    String name, className;
    
    CharacterClass(String className, String name, int aP, int hP){
    this.aP = aP;
    this.hP = hP;
    this.name = name;
    this.className = className;
    }
    
    void introduce(){
    System.out.println("Name  : " + name);
    System.out.println("Class : " + className + " | ATK : " + aP + " | HP : " + hP);

    }
    
}
