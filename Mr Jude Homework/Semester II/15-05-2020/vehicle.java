
public abstract class vehicle {
	private String name;
	private int maxPassengers;
	private int maxSpeed;
	
	public vehicle(String name, int maxPassengers, int maxspeed) {
		this.name = name;
		this.maxPassengers = maxPassengers;
		this.maxSpeed = maxSpeed;
	}
	
	public String getname() {
		return name; 
	}
	
	public void setname(String name) {
		this.name = name;
	}
	
	public int getmaxPassengers() {
		return maxPassengers;
	}
	
	public void setmaxPassengers(int maxPassengers) {
		this.maxPassengers = this.maxPassengers;
	}
	
	public int getmaxSpeed() {
		return maxSpeed;
	}
	
	public void setmaxSpeed(int maxSpeed) {
		this.maxSpeed = this.maxSpeed;
	}
}
