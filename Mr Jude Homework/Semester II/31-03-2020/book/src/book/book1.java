package book;

public class book1 {
    private
        String name;
        Author[] authors = new Author[100];
        double price;
        int qty = 0;


    public
        book1(String name, Author author, double price) {
            this.name = name;
            this.authors[0] = author;
            this.price = price;
        }
        
        book1(String name, Author author, double price, int qty) {
            this.name = name;
            this.authors[0] = author;
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
            for(int i = 0; i < this.authors.length; i++) {
                if(authors[i] == null) {
                    break;
                } else {
                    out += authors[i].toString() + ", ";
                }
            }

            return out;
        }

        void addAuthors(Author author) {
            int index = 0;
            for(int i = 0; i < this.authors.length; i++) {
                if(authors[i] == null) {
                    index = i;
                    break;
                }
            }
            authors[index] = author;
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
            "}";
    }

}