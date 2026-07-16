package polymorphism;

public class Main {
    
    public static void main (String[] args){
        
        City smb = new SantaMaria();
        City mal = new Malolos();
        City mar = new Marilao();
       
        smb.cityName();
        smb.population();
        System.out.println("");
        
        mal.cityName();
        mal.population();
        System.out.println("");

        mar.cityName();
        mar.population();
        
    }
    
}
