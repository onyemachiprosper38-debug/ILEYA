public class IleyaJava {

    public static int getEven(int [] number){
            int count = 0;
        for(int counter = 0; counter < number.length; counter++){
            if (number[counter] % 2 == 0) {
                count++;
        }
       }
            return count;
    }


    public static int getOdd(int [] numbers){
        int count = 0;
    for(int counter = 0; counter < numbers.length; counter++){
        if (numbers[counter] % 2 != 0){
            count++;
        }
      }
        return count;
   }

    public static boolean checkPalindrome(int[] numb){
        int start = 0;
        int end = numb.length - 1;

        while (start < end){
            if(numb[start] != numb[end]){
                return false;
       }
        start++;
        end--;
     }
      return true;


   }

 }
