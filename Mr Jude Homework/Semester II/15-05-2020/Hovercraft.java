public class Hovercraft extends LandVehicle implements isSeaVehicle {
	private int displacement;
	
	public Hovercraft(String name, int maxPassengers, int maxSpeed, int numWheels, int displacement) {
		super(name,maxPassengers,maxSpeed,numWheels);
		this.displacement = displacement;
	}
	
	public int getDisplacement() {
		return displacement;
	}
	
	public void setDisplacement(int displacement) {
		this.displacement = displacement;
	}
	
	public void launch() {
		System.out.println("Hovercraft launched and ready to go!");
	}

	public void setnumWHeels(int numWheels) {
		this.numWheels = numWheels;
	}
	
	public void enterland() {
		System.out.println("Land Ho, we're entering land!");
	}
	
	public void entersea() {
		System.out.println("Prepare to get wet we're entering sea!");
	}
}
