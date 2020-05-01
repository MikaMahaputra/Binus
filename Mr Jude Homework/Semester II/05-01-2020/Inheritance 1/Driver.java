
public class Driver {
	public static void main (String[] args) {
		Circle C1 = new Circle (100, "blue" , false);
		Rectangle R1 = new Rectangle (10,20,"red",false);
		Square S1 = new Square (13, "green", false);
		
		System.out.println(C1.toString());
		System.out.println("C1 Area is : " + C1.getArea());
		
		System.out.println(R1.toString());
		System.out.println("R1 Area is :" + R1.getArea() + "R1 Perimeter is : " + R1.getPerimeter());
		
		System.out.println(S1.toString());
		System.out.println("S1 Area is: " + S1.getArea() + "S1 Perimeter is : " + S1.getPerimeter());
	}
}
