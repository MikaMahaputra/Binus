public class mytriangle {

    private mypoint v1;
    private mypoint v2;
    private mypoint v3;

    public mytriangle(int x1, int y1, int x2, int y2, int x3, int y3) {
        this.v1 = new mypoint(x1, y1);
        this.v2 = new mypoint(x2, y2);
        this.v3 = new mypoint(x3, y3);
    }

    public mytriangle(mypoint v1, mypoint v2, mypoint v3) {
        this.v1 = v1;
        this.v2 = v2;
        this.v3 = v3;
    }

    public double getPerimeter() {
        return v1.distance(v2) + v1.distance(v3) + v2.distance(v3);
    }

    public String getType()
    {
        double d1 = v1.distance(v2);
        double d2 = v1.distance(v3);
        double d3 = v2.distance(v3);
        
        if (d1 == d2 && d2 == d3) {
            return "equilateral";
        }
        else if (d1 == d2 || d1 == d3 || d2 == d3) {
            return "isosceles";
        }
        return "scalene";
    }
    
    
    public String toString() {
        return "Triangle @ "+ v1 +", "+ v2 +", "+ v3;
    }
}   