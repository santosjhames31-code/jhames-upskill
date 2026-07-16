package datatype_conversion;

import java.util.Scanner;

public class Main {
  
    public static void main(String[] args){
    
        String num = "123";
        
        // string to integer
        int x = Integer.parseInt(num);
        
        // integer to string
        String s = String.valueOf(x);
           
        System.out.println(s+1);
        System.out.println(x+1);
        
        // Widening TypeCasting
        byte byt = 67;
        short sho = byt;
        int i = sho;
        long lon = i;
        float flo = lon;
        double doub = flo;
        
        // Narrowing TypeCasting
        double d = 123;
        float f = (float) d;
        long l = (long) f;
        int in = (int) l;
        short sh = (short) in;
        byte by = (byte) sh;
        
        // Primitive Data Types
        byte B;
        short S; 
        int I; 
        long L;
        float F;
        double D;
        
        // Non-Primitive Data Types
        String string;                              // String
        int[] arr = new int[1];                     // Array
        Scanner input = new Scanner(System.in);     // Class
        
        //Wrapper Class
        Integer intWrap;
    } 
    
}
