package hashmap_activity;
import java.util.HashMap;
import java.util.Scanner;
public class Main {
    
    public static void main(String[] jhames){
        
        Scanner input = new Scanner(System.in);
        HashMap <Integer, Student> hm = new HashMap<>();
        System.out.println("=============================================================");
        System.out.println("**Student Management System**");
        System.out.println("=============================================================");

        do{
            try{                    
                System.out.print("Number of Students : ");
                Student.studentSize = Integer.parseInt(input.nextLine());
                System.out.println("=============================================================\n\n");

                break;
            }catch(NumberFormatException e){
                System.out.println("Invalid data type, please try again.");
            }catch(Exception e){
                System.out.println("Something went wrong...");
            }
           
        }while(true);
            
        for(int i = 0; i < Student.studentSize; i++){
            String name, address, year, course; 
            int id; 
            System.out.println("**Student Details** : Student# [" + (i+1) + "]" );
            do{ 
                try{
                    System.out.println("=============================================================");
                    System.out.print("Name  : "); 
                    name = input.nextLine();
                    System.out.println("=============================================================");
                    String[] n = name.trim().replaceAll(" ", "").split("");
                    boolean letter = true;
                    for(String c : n){
                        char ch = c.charAt(0);
                        if(!Character.isLetter(ch)) {
                            letter = false;
                            System.out.println("Invalid name, please try again.");
                            break;
                        }    
                    }
                    if(letter) break;
                }catch(StringIndexOutOfBoundsException e){
                    System.out.println("Invalid name, please try again.");
                }
            }while(true);
            
            do{
                try{
                    System.out.println("**Course List**");
                    System.out.println("=============================================================");
                    System.out.println("[1] BSIT");
                    System.out.println("[2] BSIS");
                    System.out.println("[3] BSCS");
                    System.out.print("Select your Course : ");
                    int choice = Integer.parseInt(input.nextLine());
                    course = Student.courseSwitch(choice);
                    if(course.equals("Invalid")) System.out.print("Please only select from options 1 to 3.");
                    System.out.println("=============================================================");
                    break;
                }catch(NumberFormatException e){
                    System.out.println("Invalid data type, please try again.");
                }
            }while(true);
            
            do{
                try{
                    System.out.println("**Year**");
                    System.out.println("[1] Freshmen");
                    System.out.println("[2] Sophomore");
                    System.out.println("[3] Junior");
                    System.out.println("[4] Senior");
                    System.out.print("Select your year : ");
                    int y = Integer.parseInt(input.nextLine());
                    year = Student.yearSwitch(y); 
                    if(!year.equals("Invalid")) break;
                    else {System.out.println("Please only select from options 1 to 4.");}
                }catch(NumberFormatException e){
                    System.out.println("Invalid data type, please try again.\n");
                }
            }while(true);
            
            do{
                try{
                System.out.println("=============================================================");    
                System.out.print("Address : ");
                address = input.nextLine();
                System.out.println("=============================================================");    
                break;
                }catch(Exception e){
                    System.out.println("Something went wrong...");
                }
            }while(true);
            
            do{
                try{
                    System.out.println("Enter your student ID, It must contain exactly 8 numbers.");
                    System.out.print("ID : ");
                    id = Integer.parseInt(input.nextLine());
                    String idArr = String.valueOf(id);
                    
                    if(!hm.containsKey(id)){    
                        
                        if(idArr.length() == 10) break;
                        else{System.out.println("ID must contain exactly 11 numerical characters, please try again.");}
                    
                    }else{System.out.println("ID already exists, please try enter a new one.");}
                    System.out.println("=============================================================\n");
                }catch(NumberFormatException e){
                    System.out.println("Invalid data type, please try again.");
                System.out.println("=============================================================\n");

                }
                
            }while(true);

            
            hm.put(id, new Student(name, course, year, address, id));
            System.out.println("");    
        
        }// End for loop

        for(int i: hm.keySet()){
        hm.get(i).printRecord();
        System.out.println("");
        }
        
    } 
}
        
  