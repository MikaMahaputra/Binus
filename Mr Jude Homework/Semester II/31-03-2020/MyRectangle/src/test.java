
public class test {
	public static void main(String[] args)
    {
        mypoint p1 = new mypoint(1,3);
        mypoint p2 = new mypoint(3,7);

        myrectangle t1 = new myrectangle(p1,p2);

        System.out.println(t1.getArea());
        System.out.println(t1.getPerimeter());
        System.out.println(t1.toString());
    }
}
