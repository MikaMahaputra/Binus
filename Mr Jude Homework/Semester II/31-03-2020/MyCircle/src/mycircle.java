
	public class mycircle {

	    private mypoint center;
	    private int radius = 1;

	    public mycircle(int x, int y, int radius) {
	        this.center = new mypoint(x, y);
	        this.radius = radius;
	    }

	    public mycircle(mypoint center, int radius) {
	        this.center = center;
	        this.radius = radius;
	    }

	    public int getRadius() {
	        return this.radius;
	    }

	    public void setRadius(int radius) {
	        this.radius = radius;
	    }

	    public mypoint getCenter() {
	        return this.center;
	    }

	    public void setCenter(mypoint center) {
	        this.center = center;
	    }

	    public int getCenterX() {
	        return this.center.getX();
	    }

	    public int getCenterY() {
	        return this.center.getY();
	    }

	    public void setCenterXY(int x, int y) {
	        this.center.setXY(x, y);
	    }

	    public double getArea() {
	        return Math.PI * radius * radius;
	    }

	    public String toString() {
	        return "Circle @ "+this.center+" radius="+this.radius;
	    }
	}   
