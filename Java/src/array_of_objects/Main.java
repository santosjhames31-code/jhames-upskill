package array_of_objects;

public class Main {
    
    public static void main(String[] args){
     
    Student[] s = new Student[3];
    
    s[0] = new Student("Jhames", "Mabait", 10);   
    s[1] = new Student("Shaenna", "Masungit", 10);   
    s[2] = new Student("Gian", "Magalang", 10);   

    for(int i = 0; i < s.length; i++){
        s[i].introduce();
        System.out.println("");
    }
    
    }
    
}
