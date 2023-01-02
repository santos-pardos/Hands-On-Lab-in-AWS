import junit.framework.*;

public class TestSub extends TestCase {

   public void testSub(){
      int sub = Calculator.sub(2,4);
      assertTrue(sub == -2);
   }
}
