package book;
import java.util.*;

public class book {
    private
        String name;
        ArrayList<Author> authors = new ArrayList<Author>();
        double price;
        int qty = 0;


    public
        book(String name, Author author, double price) {
            this.name = name;
            this.authors.add(author);
            this.price = price;
        }

    
        book(String name, ArrayList<Author> authors, double price, int qty) {
            this.name = name;
            this.authors = authors;
            this.price = price;
            this.qty = qty;
        }


        book(String name, Author author, double price, int qty) {
            this.name = name;
            this.authors.add(author);
            this.price = price;
            this.qty = qty;
        }


        String getName() {
            return this.name;
        }

        void setName(String name) {
            this.name = name;
        }

        String getAuthors() {
            String out = "";
            for(int i = 0; i < this.authors.size(); i++) {
                out += authors.get(i).toString() + ", ";
            }

            return out;
        }

        void addAuthors(Author author) {
            this.authors.add(author);
        }

        double getPrice() {
            return this.price;
        }

        void setPrice(double price) {
            this.price = price;
        }

        int getQty() {
            return this.qty;
        }

        void setQty(int qty) {
            this.qty = qty;
        }
    


    @Override
    public String toString() {
        return "Book[" +
            " name='" + getName() + "'" +
            ", authors='" + getAuthors() + "'" +
            ", price='" + getPrice() + "'" +
            ", qty='" + getQty() + "'" +
            "]";
    }

}