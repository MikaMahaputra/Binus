
public class test {
	public static void main(String[] args)
    {
        mypoint p1 = new mypoint(1,9);
        mypoint p2 = new mypoint(4,5);

        mycircle c1 = new mycircle(p1,9);
        mycircle c2 = new mycircle(p2,2);

        System.out.println(c1.getRadius());

        System.out.println(c1.getArea());
        System.out.println(c2.getArea());

    }
}
