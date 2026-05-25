public class Functions {

    public static int add(int firstNumber, int secondNumber){
int sum = firstNumber + secondNumber;
    return sum;
  }


public static boolean even(int number ){

if (number % 2 == 0){
    return true;
  }
else {
    return false;

  }
}

public static int subtract(int num){
int square = num * num;
    return square;

}

public static int convert(int celsius){
int fahrenheit = celsius * 9/5 + 32;

    return fahrenheit;


}

    public static void main(String[] args){
int firstNumber = 60;
    int secondNumber = 20;
    
System.out.println(add(firstNumber, secondNumber));

     int number = 6;
System.out.println(even(number));

    int num = 7;
System.out.println(subtract(num));

    int celsius = 60;
System.out.println(convert(celsius));
   }
 }
