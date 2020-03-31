
public class customer {
	private int ID;
	private String name;
	private int discount;
	
	public customer() {
		this.ID = ID;
		this.name = name;
		this.discount = discount;
	}
	
	public int getID() {
		return this.ID;
	}
	
	public String getName() {
		return this.name;
	}
	
	public int getDiscount() {
		return this.discount;
	}
	
	void setDiscount(int discount) {
		this.discount= 50;
	}
	
	public String toString() {
        return "Customer[" + "Name= " + this.getName() + ", ID= "  + this.getID() + ']';
	}
}
