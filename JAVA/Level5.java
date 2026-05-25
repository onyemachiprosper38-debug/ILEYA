public class Level5 {
    public static int [] prime(int[] array){

int temp = 0;

for(int count = 0; count < array.length; count++){
    for (int counter = 0; counter < array.length-2; counter++){
    temp = array[counter];
    array[counter] = array[counter+1];
    array[counter+1] = temp;
   }

 }
   for (int count = array.length-1; count < 0; count++){
   if (array[count]%2 != 0){
 }
}
   return array[count];
}
public static void main(String[] args){

int[] array = {5,9,3,6,2};
system.out.print(prime(array));

   }

 }

