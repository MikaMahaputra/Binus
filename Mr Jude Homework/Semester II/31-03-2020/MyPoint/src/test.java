
public class test {
	public static void main(String[] args) {
		mypoint p1 = new mypoint(3, 4);
		mypoint p2 = new mypoint(5, 6);
		mypoint p3 = new mypoint();
		mypoint p4 = new mypoint(0, 4); 
		p3.setX(8);
		p3.setY(6);
		System.out.println("X is: " + p3.getX());
		System.out.println("Y is: " + p3.getY());
		System.out.println(p2);
		System.out.println(p3.distance(p4)); 
		System.out.println(p4.distance(p3)); 
		System.out.println(p1.distance(5, 6));
	}
}
