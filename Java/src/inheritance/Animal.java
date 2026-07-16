package inheritance;

public abstract class Animal {
    
    String vertebrata;
    String name;
    String sound;
    
    void describe(){
        System.out.println("Name       : " + name);
        System.out.println("Sound      : " + sound);
        System.out.println("Vertebrata : " + vertebrata);   
    }
    
}
