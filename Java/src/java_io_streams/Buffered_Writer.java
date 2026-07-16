package java_io_streams;

import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.Scanner;
public class Buffered_Writer {

    public static void main(String[] args){

    try(BufferedWriter writer = new BufferedWriter(new FileWriter("Secretfile.txt"))){
        writer.write("Jhames");
        writer.newLine();
        writer.write("Andrew");
        writer.newLine();
        writer.write("Santos");
    }catch(IOException e){
    System.out.println("Error");
    }
    

        
    
    }
}
