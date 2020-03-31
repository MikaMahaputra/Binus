
public class test {
    public static void main(String[] args)
    {
        mypoint p1 = new mypoint();
        mypoint p2 = new mypoint(6,9);
        mypoint p3 = new mypoint(4,2);

        mytriangle t1 = new mytriangle(p1, p2, p3);

        System.out.println(t1.getPerimeter());
        System.out.println(t1.getType());
        
    }

}
