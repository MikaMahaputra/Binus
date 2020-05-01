
public class Square extends Rectangle {

    public Square() {
        super();
    }

    public Square(double side) {
        super.setWidth(side);
        super.setLength(side);
    }

    public Square(double side, String color, boolean filled) {
        super.setWidth(side);
        super.setLength(side);
        super.setColor(color);
        super.setFilled(filled);
    }

    public double getSide() {
        return super.getLength();
    }

    public void setSide(double side) {
        super.setWidth(side);
        super.setLength(side);
    }

    public void setWidth(double side) {
        super.setWidth(side);
        super.setLength(side);
    }

    public void setLength(double side) {
        super.setWidth(side);
        super.setLength(side);
    }


    public String toString() {
        return "A square with the side of : " + this.getSide() + ", which is also a subclass of " + super.toString();
    }
}