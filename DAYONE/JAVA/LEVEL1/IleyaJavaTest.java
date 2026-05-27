import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class IleyaJavaTest{

    @Test
    public void testgetEven(){

        int[] number = {45, 60, 3, 10, 9, 12};
        int result = IleyaJava.getEven(number);

        assertEquals(3, result);
    }
    
    @Test
    public void testgetOdd(){

        int[] numbers =  {45, 60, 3, 10, 9, 12};
        int result = IleyaJava.getOdd(numbers);

        assertEquals(3, result);
    }

    @Test
    public void testPalindrome(){
    
        int[] numb = {45, 0, 8, 0, 45};
        boolean result = IleyaJava.checkPalindrome(numb);
        
        assertTrue(result);
   }
     @Test
    public void testNotPalindrome(){
    
        int[] numb = {45, 0, 8, 0, 45};
        boolean result = IleyaJava.checkPalindrome(numb);
        
        assertFalse(result);
   }

}
