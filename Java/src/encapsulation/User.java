package encapsulation;

public class User {
 
    private String email;
    private String password;
    private int studentNumber;
    
    
    User(String email, String password, int studentNumber){
        
        this.email = email;
        this.password = password;
        this.studentNumber = studentNumber;
        
    }
    
    void setEmail(String email){
        this.email = email;
    }
    
    String getEmail(){
        return email;
    }
    
    void setPassword(String password){
        this.password = password;
    }
    
    String getPassword(){
        return password;
    }
    
    int getStudentNumber(){
        return studentNumber;
    }
    
}
