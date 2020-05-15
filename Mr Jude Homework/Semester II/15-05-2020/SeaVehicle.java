public abstract class SeaVehicle extends vehicle implements isSeaVehicle {
	int displacement;
	
	public SeaVehicle(String name, int maxPassengers, int maxSpeed, int displacement) {
		super(name, maxPassengers, maxSpeed);
		this.displacement = displacement;
	}
	
	public int getDisplacement() {
		return displacement;
	}
	
	public void setDisplacement(int displacement) {
		this.displacement = displacement;
	}
	
	public void launch() {
		System.out.println("Boat launched and ready to go!");
	}
}
