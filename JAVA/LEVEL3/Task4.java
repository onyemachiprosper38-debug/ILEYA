import java.util.Scanner;
public class Task4 {

    public static void main(String[] arrgs){
Scanner myscanner = new Scanner(System.in);

System.out.println("Enter number ");
int number = myscanner.nextInt();

for(int count = 1; count <= 12; count++){
int table = number * count;

System.out.println(number + " x" + count + "=" + table);
  }
 }
}
