
public class Policecar extends LandVehicle implements isEmergency {
	public Policecar(String name, int maxPassengers, int maxSpeed, int numWheels) {
		super(name, maxPassengers, maxSpeed, numWheels);
	}
	
	public void enterchase() {
		System.out.println("Affirmative, we're entering pursuit!");
	}
	
	public void endchase() {
		System.out.println("Ladies and gentlemen, we got him!");
	}
	
	public void soundSiren() {
		System.out.println("*Insert siren noises*");
	}

	public void setnumWHeels(int numWheels) {
		this.numWheels = numWheels;
	}
}