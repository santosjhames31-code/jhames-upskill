package enums;

public class Main {
   
    public static void main(String[] args){
    
        CharacterClass[] character = new CharacterClass[3];
        character[0] = CharacterClass.WARRIOR;
        character[1] = CharacterClass.MAGE;
        character[2] = CharacterClass.ARCHER;
    
        for(CharacterClass c : character){
            c.introduce();
            System.out.println("");
        }
    
    }
    
}
