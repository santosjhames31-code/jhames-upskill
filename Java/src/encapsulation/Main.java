package encapsulation;

import java.util.*;
import java.util.Scanner;

public class Main {

        static boolean hasLetter;
        static boolean hasDigit;
        static boolean hasSpecialCharacter;        
        static boolean hasUpperCase;
        static boolean hasLowerCase;
        static boolean validLength;

    public static void main(String[] args){
    
        Scanner input = new Scanner(System.in);
        String email;
        String password = "";
        int studentNumber;
        boolean isLoop = false;
        boolean proceed = true;
        
    do{    
    try{
        System.out.println("------- LOG IN --------");
        System.out.print("Email          : ");
        email = input.nextLine();
        
        boolean pass = false;
        while(!pass){
        System.out.print("Password       : ");
        password = input.nextLine();
  
            hasLetter = false;
            hasDigit = false;
            hasSpecialCharacter = false;        
            hasUpperCase = false;
            hasLowerCase = false;
            validLength = false;
        
            for(int i = 0; i < password.length(); i++){ 
            char c = password.charAt(i);

            if(password.length() >= 8)        validLength = true;
            if(Character.isLetter(c))         hasLetter = true;
            if(Character.isDigit(c))          hasDigit = true;
            if(Character.isUpperCase(c))      hasUpperCase = true;  
            if(Character.isLowerCase(c))      hasLowerCase = true;
            if(!Character.isLetterOrDigit(c)) hasSpecialCharacter = true;
            if(hasLetter && hasDigit && hasUpperCase && hasLowerCase && hasSpecialCharacter && validLength) pass = true; 
            
            }
            if(!pass){
            System.out.println("Password must be at least 8 characters long and include uppercase and lowercase letters, a number, and a special character.");
            System.out.println("--------------------------------------------------------------------------------------------------------------------------");
            }
        }
        System.out.print("Student Number : ");
        studentNumber = input.nextInt();
        System.out.print("Logged in successfully, Do you want to edit your attributes? [y/N] : ");
        char ch = input.next().charAt(0);
        input.nextLine();
        char upperCh = Character.toUpperCase(ch);
        
        User u = new User(email, password, studentNumber);
        
        switch(upperCh){
            case 'Y':
                
                
                System.out.println("What do you want to edit?");
                System.out.println("[1] Email");
                System.out.println("[2] Password");
                System.out.print("Select between numbers [1] & [2] : ");
                int choice = input.nextInt();
                input.nextLine(); 
                    switch(choice){
                        case 1:
                        do{ 
                            System.out.println("You must enter your password to proceed, thank you.");
                            System.out.print("Password : ");
                            String enteredPass = input.nextLine();
                                if(enteredPass.equals(u.getPassword())){
                                    System.out.println("Correct password!");
                                    System.out.println("--------------------------------------------------------------------------------------------------------------------------");
                                    System.out.print("Enter your new gmail : ");
                                    String newEmail = input.nextLine();
                                    u.setEmail(newEmail);
                                    System.out.println("Successfully changed email.");
                                    System.out.println("--------------------------------------------------------------------------------------------------------------------------");
                                    break;
                                }else{
                                    System.out.println("Incorrect Password, Please Try Again.\n");
                                }                                 
                 }while(true);
                        
                        break;     
                        case 2:
                            boolean isDone = false;
                            do{
                            System.out.print("Enter current password :");
                            String currentPass = input.nextLine();
                            
                                
                                    if(currentPass.equals(u.getPassword())){
                                        System.out.println("Correct Password.");
                                        
                                        do{
                                        System.out.println("--------------------------------------------------------------------------------------------------------------------------");  
                                        System.out.print("Enter new password : ");
                                        String newPass = input.nextLine();

                                            hasLetter = false;
                                            hasDigit = false;
                                            hasSpecialCharacter = false;        
                                            hasUpperCase = false;
                                            hasLowerCase = false;
                                            validLength = false;

                                            for(int i = 0; i < newPass.length(); i++){ 
                                            char c = newPass.charAt(i);

                                            if(newPass.length() >= 8)        validLength = true;
                                            if(Character.isLetter(c))         hasLetter = true;
                                            if(Character.isDigit(c))          hasDigit = true;
                                            if(Character.isUpperCase(c))      hasUpperCase = true;  
                                            if(Character.isLowerCase(c))      hasLowerCase = true;
                                            if(!Character.isLetterOrDigit(c)) hasSpecialCharacter = true;
                                            if(hasLetter && hasDigit && hasUpperCase && hasLowerCase && hasSpecialCharacter && validLength) isDone = true;
                                               
                                            }
                                            if(!isDone){
                                            System.out.println("Password must be at least 8 characters long and include uppercase and lowercase letters, a number, and a special character.");
                                            }else {
                                                u.setPassword(newPass);
                                                System.out.println("Password changed successfully.");
                                            }                            
                                        }while(!isDone);
                                        break;
                                    }
                                    else {
                                    proceed = false;
                                    System.out.println("Wrong password, Please Try Again.");                  
                                    System.out.println("--------------------------------------------------------------------------------------------------------------------------");
                                    
                                    }
                            }while(true);
                            break;
                        default:                            
                    }
                    break;
                    case 'N':
                        System.out.println("Thank you for using our system.");
                        proceed = false;
                        isLoop = true;
                        break;
                    default:
                        System.out.println("Please choose from options Y/N only, thank you.");
                        break;
                              
                }
                System.out.println("Email          : " + u.getEmail());
                System.out.println("Student number : " + u.getStudentNumber());
                System.out.println("Password       : " + u.getPassword());
                char c = 0;
                if(proceed){
                System.out.print("Do you want to proceed? [y/N]?");
                char cha = input.next().charAt(0);
                c = Character.toUpperCase(cha);
                input.nextLine();
                }
                
                switch(c){
                
                    case 'Y':
                        System.out.println("Loading...");
                        break;
                    case 'N':
                        System.out.println("Exiting program...");
                        isLoop = true;
                        break;
                    default:                
                }
                
            }catch(InputMismatchException e){
            input.nextLine();
            System.out.println("Invalid Data Type, Please try Again.");
            }catch(Exception e){
            input.nextLine();    
            input.nextLine();
            System.out.println("An Error Occurred");
            }
            }while(!isLoop);
        }
        
    }

