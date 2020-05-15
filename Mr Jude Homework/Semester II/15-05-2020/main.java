
public class main {
	public static void main(String[] args) {
		
		System.out.println("Policecar: ");
		Policecar cop = new Policecar("Dodge Charger 5.7L", 4, 150, 4);
		cop.enterchase();
		cop.soundSiren();
		cop.endchase();
		System.out.println("The " + cop.getname() + " has " + cop.getnumWheels() + " wheels" );
	
	
		System.out.println("\nJeep: ");
		Jeep jp = new Jeep("Willys MB,", 4 ,65 ,4);
		jp.drive();
		jp.soundHorn();
		System.out.println("This is a " + jp.getname() +" it is the most popular vehicle for the US Army back in the Second World War!" );
		
		System.out.println("\nFrigate: ");
		Frigate ship = new Frigate("Sachsen Class", 1000, 33, 5800);
		ship.fireGun();
		System.out.println("The ship weighs " + ship.getDisplacement() + " tonnes");
		
		System.out.println("\n Hovercraft: ");
		Hovercraft hover = new Hovercraft("Mark 1 Hovervan",4, 30, 4, 190);
		hover.entersea();
		hover.enterland();
		System.out.println("The Hovervan weighs " + hover.getDisplacement());
	}
}
