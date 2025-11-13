import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.BeforeEach;

public class CheckOutTest{



@Test
public void testThatSubTotalWorks(){
CheckOutFunction checkOut= new  CheckOutFunction();
assertEquals(50,checkOut.subTotal(50,0));
}






}