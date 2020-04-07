
public class Customer {
	private String firstname;
	private String lastname;
	private Account account;
	
	public Customer(String f, String l) {
		this.firstname = f;
		this.lastname = l;
	}
	
	public String getFirstname() {
		return this.firstname;
	}
	
	public String getLastname() {
		return this.lastname;
	}
	
	public Account getAccount() {
		return this.account;
	}
	
	public void setAccount(Account acct) {
		this.account = acct;
	}
	
	public String toString() {
		return "Account[Name= " + getFirstname() + " " + getLastname() + ", " + getAccount() + "]";
	}

}
