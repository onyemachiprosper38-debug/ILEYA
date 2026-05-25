import java.util.Scanner;

public class Task10{

    public static void main(String[] args){

Scanner myscanner = new Scanner(System.in);

System.out.println("Enter a number ");
int firstNumber = myscanner.nextInt();

System.out.println("Enter a number ");
int secondNumber = myscanner.nextInt();

System.out.println("Enter a number ");
int thirdNumber = myscanner.nextInt();


int sum = 0;

sum = firstNumber + secondNumber + thirdNumber;

int average = sum / 3;
System.out.println("The average of your three numbers is  " + average);

   }

 }
