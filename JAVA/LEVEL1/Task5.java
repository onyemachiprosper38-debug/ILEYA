import java.util.Scanner;

public class Task3{

    public static void main(String[] args){

Scanner myscanner = new Scanner(System.in);

System.out.println("Enter temperature in celsius ");
int celsius = myscanner.nextInt();


int fahrenheit = 0;

fahrenheit = celsius * 9 / 5 + 32;

System.out.println("The temperature is  " + fahrenheit );

   }

 }
