
public class Account {
	private double balance;
	
	public Account(double balance) {
		this.balance = balance;
	}
	
	public double getBalance() {
		return balance;
	}
	
	public void setBalance(double balance) {
		this.balance = balance;
	}
	
	public boolean deposit(double amount) {
		if (amount > 0) {
			this.balance += amount;
			return true;
		}
		
		else {
			System.out.println("Invalid amount please try again");
			return false;
		}
	}
	
	public boolean withdraw(double amount) {
		if (this.balance > amount) {
			this.balance -= amount;
			return true;
		}
		else {
			System.out.println("Insufficient balance");
			return false;
		}
	}
	
	public String toString() {
        return "Balance= " + balance;
    }

}
