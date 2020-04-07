
public class test {
	public static void main(String[] args) {
		Account a1 = new Account (200);
		Account a2 = new Account (600);
		
		a1.deposit(100);
		a2.deposit(200);
		
		Customer c1 = new Customer("Geralt", "Rivia");
		Customer c2 = new Customer("Yennefer", "Vengerberg");
		
		c1.setAccount(a1);
		c2.setAccount(a2);
		
		Bank b1 = new Bank ("Roach");
		System.out.println(b1.getnumberOfCustomers());
		
		b1.addCustomer(c1);
		b1.addCustomer(c2);
		System.out.println(b1.getnumberOfCustomers());
		
		System.out.println(c1.toString());
		System.out.println(c2.toString());
		
		a1.withdraw(250);
		a2.withdraw(500);
		System.out.println(c1.toString());
		System.out.println(c2.toString());		
	}
}
