import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
public class WarmUpTest{

	@Test
	public void testThatWarmUpAcceptsOnlyIntergerGreaterThanZero(){
	WarmUp warmUp = new WarmUp();
	String result = warmUp.WarmUpFunction(1);
	assertEquals(result,"enter a valid input");
	}

}