import java.util.Scanner;

import java.util.random;

public class NumberApp{

    public static void main(String[] args){

Scanner myscanner = new Scanner(System.in);


for (int count = 0; count < 5; count++){
System.out.println("Guess number ");
int number = myscanner.nextInt();

if (number <= 100){
System.out.println("Correct Number");break;
}

else if (number > 100){
System.out.println("number is higher ");
}
   }
  }
}
