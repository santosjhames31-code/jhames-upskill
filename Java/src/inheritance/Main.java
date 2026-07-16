package inheritance;

public class Main {
    
    public static void main(String[] args){
    
        Dog d = new Dog("Mammal", "arf", "Browny");
        Cat c = new Cat("Mammal", "meow", "Ming");
        Cow cw = new Cow("Mammal", "moo", "BakangItim");
        
        d.describe();
        cw.describe();
        c.describe();
       
    }
    
}
