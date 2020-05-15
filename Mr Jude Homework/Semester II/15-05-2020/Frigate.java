
public class Frigate extends SeaVehicle {
	public Frigate(String name, int maxPassengers, int maxSpeed, int displacement) {
		super(name,maxPassengers, maxSpeed, displacement);
	}
	
	public void fireGun() {
		System.out.println("Firing main guns!");
	}
}
