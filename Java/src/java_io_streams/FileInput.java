package java_io_streams;

import java.io.FileInputStream;
import java.io.IOException;

public class FileInput {
   
    public static void main(String[] args){
    
        try(FileInputStream input = new FileInputStream("Secretfile.txt")){   
        int b;
            while((b = input.read()) != -1){
                System.out.print((char) b);
            } 
        }catch(IOException e){
            System.out.println("Error");
        }
        
    }
    
}
