function getEven(number){
            int count = 0;
        for(let counter = 0; counter < number.length; counter++){
            if (number[counter] % 2 == 0) {
                count++;
        }
       }
            return count;
    }


    function getOdd(numbers){
        int count = 0;
    for(let counter = 0; counter < numbers.length; counter++){
        if (numbers[counter] % 2 != 0){
            count++;
        }
      }
        return count;
   }

    function checkPalindrome(int[] numb){
        let start = 0;
        let end = numb.length - 1;

        while (start < end){
            if(numb[start] != numb[end]){
                return false;
       }
        start++;
        end--;
     }
      return true;
   }

 

