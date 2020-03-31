public class invoice {
	private String id;
	private String desc;
	private int qty;
	private double unitprice;
	
	public invoice() {
		this.id = id;
		this.desc = desc;
		this.qty = qty;
		this.unitprice = unitprice;
	}
	public String getID() {
		return this.id;
	}
	
	public String getDesc() {
		return this.desc;
	}
	
	public int getQty() {
		return this.qty;
	}
	
	void setQty(int qty) {
		qty = 100;
	}
	
	public double getUnitPrice() {
		return this.unitprice;
	}
	
	void setUnitPrice(double unitprice) {
		this.unitprice= 69;
	}
	
	public double getTotal() {
		return unitprice*qty;
	}
	
	public String toString() {
        return "Invoice[" + "ID= " + this.getID() + ", Desc= " + this.getDesc() +", Quantity= " + this.getQty() + ", Unitprice= " + this.getUnitPrice() + ']';
	}
}