import java.util.Scanner;

public class Task4{

    public static void main(String[] args){

Scanner myscanner = new Scanner(System.in);

System.out.println("Enter number ");
int firstNumber = myscanner.nextInt();

System.out.println("Enter number ");
int secondNumber = myscanner.nextInt();

System.out.println("Enter number ");
int thirdNumber = myscanner.nextInt();

if (firstNumber > secondNumber && firstNumber > thirdNumber){
System.out.println("the largest " + " is" + firstNumber );
}

else if (secondNumber > firstNumber && secondNumber > thirdNumber){
System.out.println("the largest " + " is" + secondNumber);

}

else {
System.out.println("The largest number is " + thirdNumber);

    }
   }

 }
