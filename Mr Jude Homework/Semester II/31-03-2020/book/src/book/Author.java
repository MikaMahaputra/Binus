package book;

public class Author {
    private
        String name;
        String email;
        char gender;


    public Author(String name, String email, char gender) {
        this.name = name;
        this.email = email;
        this.gender = gender;
    }

    public String getName() {
        return this.name;
    }

    public String getEmail() {
        return this.email;
    }

    public char getGender() {
        return this.gender;
    }

    public void email(String email) {
        this.email = email;

    }


    @Override
    public String toString() {
        return "Author[" +
            " name='" + getName() + "'" +
            ", email='" + getEmail() + "'" +
            ", gender='" + getGender() + "'" +
            "]";
    }

}