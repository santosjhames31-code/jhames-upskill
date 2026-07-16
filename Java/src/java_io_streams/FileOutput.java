package java_io_streams;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Scanner;

public class FileOutput {
    
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);
        
        try(FileOutputStream output = new FileOutputStream("Secretfile.txt", true)){
            String word = sc.nextLine();
            
            byte[] b = word.getBytes();
            output.write(b);
        }catch(IOException e){
            System.out.println("Error");
        }
        
        
        
    } 
    
}
