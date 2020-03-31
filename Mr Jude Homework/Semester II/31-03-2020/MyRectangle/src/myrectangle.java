public class myrectangle {
	private float length;
	private float width;

	public myrectangle(){
        this.length = 1.0f;
        this.width = 1.0f;
    }
	
	public myrectangle(float length, float width) {
		this.length = length;
		this.width = width;
	}
	
	public float getLength() {
		return this.length;
	}
	
	public float getWidth() {
		return this.width;
	}
	
	void setLength(float length) {
		this.length = length;
	}
	
	void setWidth(float width) {
		this.width = width;
	}
	
	public double getArea() {
		return width*length;
	}
	
	public double getPerimeter() {
		return 2*width + 2*length;
	}
}