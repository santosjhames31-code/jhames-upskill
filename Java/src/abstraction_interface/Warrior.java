package abstraction_interface;

public class Warrior implements Role{
   
    String name;
    int hp;
    int mp;
    String attack;
    int pa;
    
    Warrior(String name, String attack, int mp, int hp, int pa){
    this.name = name;
    this.attack = attack;
    this.hp = hp;
    this.mp = mp;
    this.pa = pa;
    }

    public void attack(){
        System.out.println(attack);
    }
    
    public void showStats(){
        System.out.println("Name   : " + name);
        System.out.println("HP     : " + hp);
        System.out.println("MP     : " + mp);
        System.out.println("PA     : " + pa);
    }
    
    public String setName(String name){
        this.name = name;
        return name;
    }
    
    public void getName(){
        System.out.println(name);
    }
    
}
