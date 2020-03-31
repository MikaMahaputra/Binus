package book;

public class test {
    public static void main(String[] args) {
        Author A1 = new Author("Hans", "Hans@gmail.com", 'M');
        Author A2 = new Author("Hitler", "HitlerDidNothingWrong@gmail.com", 'M');

        book1 B2 = new book1("How to get ze flammenwerfer", A1, 59.99, 1945);
        
        System.out.println(B2.toString());

        B2.addAuthors(A2);

        System.out.println(B2.toString());
    }
    

}