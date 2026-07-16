package recursive_methods;

public class Main {
   
    public static void main(String[] args){
    
    String[] week = {
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday", 
        "Saturday"
    };    
    
    weekDays(week, 5);
        
    }
    
    static void weekDays(String[] week, int i){

        if(week.length == i)return;

        System.out.println(week[i]);        
        weekDays(week, ++i);
        
    }
    
}
