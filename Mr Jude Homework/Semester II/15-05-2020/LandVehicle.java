
public abstract class LandVehicle extends vehicle implements isLandVehicle {
	int numWheels;
	
	public LandVehicle(String name, int maxPassengers, int maxSpeed, int numWheels) {
		super(name, maxPassengers, maxSpeed);
		this.numWheels = numWheels;
	}
	
	public void drive() {
		System.out.println("You are currently driving");
	}
	
	public int getnumWheels() {
		return numWheels;
	}
	
	public void setnumWheels(int numWheels) {
		this.numWheels = numWheels;
	}
}
