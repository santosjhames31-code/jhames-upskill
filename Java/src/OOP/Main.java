package OOP;

class Cat{

    String name, breed;
    int age;
    
    Cat(String name, String breed, int age){
    this.name = name;
    this.breed = breed;
    this.age = age;
    }
    
    void introduce(){
        System.out.println("He / She is " +  name + "\n" + name + " is " + breed + " breed\n" + name + " is " + age + " years old");
    }
    
    void sayMeow(){
        System.out.println("Meow!");
    }
    
    void eat(){
        System.out.println(name + " is now eating...");
    }
}

public class Main {
    
    public static void main(String[] args) {
        Cat c = new Cat("Dave", "Persian", 21);
        c.eat();
        c.introduce();
        c.sayMeow();
    }
    
}
