package filehandling;

import java.io.*;
import java.util.ArrayList;

public class Main {

        public static void main (String[] args){

            File file = new File("Secretfile.txt");  
            ArrayList <String> list = new ArrayList<>();
            
                try(BufferedReader reader = new BufferedReader(new FileReader(file))){
                String line;
                while((line = reader.readLine()) != null){
                    System.out.println(line);
                    list.add(line);
                }
                
                }catch(IOException e){
                    System.out.println("Error");
                }
            
                try(FileWriter writer = new FileWriter(file)){
                String wordToEdit = "Santos";
                String word = "Uzumaki";
                for(String line:list){
                if(line.equals(wordToEdit))writer.write(word + "\n");
                else writer.write(line + "\n");
                }
                
                }catch(IOException e){
                    System.out.println("Error");
                }
                
        }

    }
